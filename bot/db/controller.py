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
                models.Person.assistances.any(models.PersonAssistance.day == today)  # type: ignore
            )
        elif skip_attending_today:
            statement = statement.where(
                ~models.Person.assistances.any(models.PersonAssistance.day == today)  # type: ignore
            )
        if skip_event is not None:
            event_to_skip = skip_event.value
            statement = statement.where(
                ~models.Person.assistances.any(
                    and_(
                        models.PersonAssistance.day == today,  # type: ignore
                        getattr(models.PersonAssistance, event_to_skip)  # type: ignore
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
    #   Actions for PersonAssistance model   #
    ##########################################

    #########
    # READ  #
    #########
    def get_person_assistance_for_date(
        self,
        person: models.Person,
        day: date
    ) -> Optional[models.PersonAssistance]:
        statement = select(models.PersonAssistance).where(
            models.PersonAssistance.person_id == person.id,
            models.PersonAssistance.day == day,
        )
        try:
            return self.session.exec(statement).one()
        except NoResultFound:
            return None

    def get_assistants_for_date(self, day: date) -> list[models.Person]:
        statement = select(models.PersonAssistance).where(models.PersonAssistance.day == day)
        assistants = self.session.exec(statement).all()
        return [assistant.person for assistant in assistants]

    def get_assistants_for_event(self, day: date, action: AssistanceEvent) -> list[models.Person]:
        statement = select(models.PersonAssistance).where(
            models.PersonAssistance.day == day,
            getattr(models.PersonAssistance, action.value),
        )
        assistants = self.session.exec(statement).all()
        return [assistant.person for assistant in assistants]

    #########
    # WRITE #
    #########

    def get_or_create_person_assistance_for_date(
        self,
        person: models.Person,
        day: date
    ) -> models.PersonAssistance:
        person_assistance = self.get_person_assistance_for_date(person, day)
        if person_assistance is not None:
            return person_assistance
        logger.info(f"Creating new person assistance for {person.username} on {day}")
        person_assistance = models.PersonAssistance(person_id=person.id, day=day)
        self.session.add(person_assistance)
        self.session.commit()
        self.session.refresh(person_assistance)
        return person_assistance

    def delete_person_assistance_for_date(self, person: models.Person, day: date) -> None:
        person_assistance = self.get_person_assistance_for_date(person, day)
        if person_assistance is None:
            logger.info(
                f"Can't delete person assistance for {person.username} "
                f"on {day} because it does not exist"
            )
            return
        logger.info(f"Deleting person assistance for {person.username} on {day}")
        self.session.delete(person_assistance)
        self.session.commit()

    def set_person_assistance_event(
        self,
        assistance: models.PersonAssistance,
        event: AssistanceEvent,
        value: bool
    ) -> None:
        logger.info(
            f"Setting {event} for {assistance.person.username} on {assistance.day} to {value}"
        )
        setattr(assistance, event.value, value)
        self.session.add(assistance)
        self.session.commit()
