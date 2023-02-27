import enum
from datetime import date
from typing import Optional

from loguru import logger
from sqlalchemy import and_
from sqlalchemy.exc import NoResultFound
from sqlmodel import Session, select

from db import models
from db.engine import engine


class AssistanceEvent(enum.Enum):
    BROUGHT_LUNCH = "brought_lunch"
    LUNCH_OUTSIDE = "lunch_outside"
    IN_FOR_BEERS = "in_for_beers"


class DataBaseController:
    def __enter__(self) -> "DataBaseController":
        self.session = Session(engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:  # type: ignore
        self.session.close()

    def __init__(self, session: Optional[Session] = None) -> None:
        self.session = session  # type: ignore

    def __del__(self) -> None:
        if self.session:
            self.session.close()

    ################################
    #   Actions for Person model   #
    ################################

    #########
    # READ  #
    #########
    def get_person(self, username: str) -> Optional[models.Person]:
        statement = select(models.Person).where(models.Person.username == username)
        try:
            return self.session.exec(statement).one()
        except NoResultFound:
            return None

    def get_admins(self) -> list[models.Person]:
        statement = select(models.Person).where(models.Person.is_admin)
        return self.session.exec(statement).all()

    def get_promptable_people(
        self,
        only_attending_today: bool = False,
        skip_attending_today: bool = False,
        skip_event: Optional[AssistanceEvent] = None
    ) -> list[models.Person]:
        if only_attending_today and skip_attending_today:
            raise ValueError("Can't have both only_attending_today and skip_attending_today")
        statement = select(models.Person).where(models.Person.wants_prompts)
        today = date.today()
        if only_attending_today:
            statement = statement.where(
                models.Person.attendances.any(models.PersonAttendance.day == today)  # type: ignore
            )
        elif skip_attending_today:
            statement = statement.where(
                ~models.Person.attendances.any(models.PersonAttendance.day == today)  # type: ignore
            )
        if skip_event is not None:
            event_to_skip = skip_event.value
            statement = statement.where(
                ~models.Person.attendances.any(
                    and_(
                        models.PersonAttendance.day == today,  # type: ignore
                        getattr(models.PersonAttendance, event_to_skip)  # type: ignore
                    )
                )
            )

        return self.session.exec(statement).all()

    #########
    # WRITE #
    #########
    def get_or_create_person(
        self, username: str, channel_id: str, is_admin: bool = False
    ) -> tuple[bool, models.Person]:
        person = self.get_person(username)
        if person is not None:
            logger.info(f"Person with username {username} already exists")
            return False, person
        logger.info(f"Creating new person with username {username}")
        person = models.Person(username=username, channel_id=channel_id, is_admin=is_admin)
        self.session.add(person)
        self.session.commit()
        self.session.refresh(person)
        return True, person

    def delete_person(self, username: str) -> bool:
        person = self.get_person(username)
        if person is None:
            logger.info(f"Can't delete person with username {username} because it does not exist")
            return False
        logger.info(f"Deleting person with username {username}")
        self.session.delete(person)
        self.session.commit()
        return True

    def set_person_admin_status(self, person: models.Person, is_admin: bool) -> None:
        logger.info(f"Setting admin status for {person.username} to {is_admin}")
        person.is_admin = is_admin
        self.session.commit()

    def set_person_wants_prompts(self, person: models.Person, wants_prompts: bool) -> None:
        logger.info(f"Setting wants prompts for {person.username} to {wants_prompts}")
        person.wants_prompts = wants_prompts
        self.session.commit()

    ##########################################
    #   Actions for PersonAttendance model   #
    ##########################################

    #########
    # READ  #
    #########
    def get_person_attendance_for_date(
        self,
        person: models.Person,
        day: date
    ) -> Optional[models.PersonAttendance]:
        statement = select(models.PersonAttendance).where(
            models.PersonAttendance.person_id == person.id,
            models.PersonAttendance.day == day,
        )
        try:
            return self.session.exec(statement).one()
        except NoResultFound:
            return None

    def get_attendants_for_date(self, day: date) -> list[models.Person]:
        statement = select(models.PersonAttendance).where(models.PersonAttendance.day == day)
        attendants = self.session.exec(statement).all()
        return [attendant.person for attendant in attendants]

    def get_attendants_for_event(self, day: date, action: AssistanceEvent) -> list[models.Person]:
        statement = select(models.PersonAttendance).where(
            models.PersonAttendance.day == day,
            getattr(models.PersonAttendance, action.value),
        )
        attendants = self.session.exec(statement).all()
        return [attendant.person for attendant in attendants]

    #########
    # WRITE #
    #########

    def get_or_create_person_attendance_for_date(
        self,
        person: models.Person,
        day: date
    ) -> models.PersonAttendance:
        person_attendance = self.get_person_attendance_for_date(person, day)
        if person_attendance is not None:
            return person_attendance
        logger.info(f"Creating new person attendance for {person.username} on {day}")
        person_attendance = models.PersonAttendance(person_id=person.id, day=day)
        self.session.add(person_attendance)
        self.session.commit()
        self.session.refresh(person_attendance)
        return person_attendance

    def delete_person_attendance_for_date(self, person: models.Person, day: date) -> None:
        person_attendance = self.get_person_attendance_for_date(person, day)
        if person_attendance is None:
            logger.info(
                f"Can't delete person attendance for {person.username} "
                f"on {day} because it does not exist"
            )
            return
        logger.info(f"Deleting person attendance for {person.username} on {day}")
        self.session.delete(person_attendance)
        self.session.commit()

    def set_person_attendance_event(
        self,
        attendance: models.PersonAttendance,
        event: AssistanceEvent,
        value: bool
    ) -> None:
        logger.info(
            f"Setting {event} for {attendance.person.username} on {attendance.day} to {value}"
        )
        setattr(attendance, event.value, value)
        self.session.add(attendance)
        self.session.commit()
