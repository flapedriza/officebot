from datetime import date
from typing import Optional

import schedule
from loguru import logger
from mmpy_bot import Plugin, Message

import config
from assets import messages
from db.controller import DataBaseController, AssistanceEvent


class AttendanceActionController:
    @classmethod
    def on_start(cls, plugin: Plugin) -> None:
        cls.broadcast_message_to_admins(plugin, messages.BOT_START_MESSAGE)
        cls.schedule_checks(plugin)

    def on_stop(self, plugin: Plugin) -> None:
        self.broadcast_message_to_admins(plugin, messages.BOT_STOP_MESSAGE)

    @classmethod
    def schedule_checks(cls, plugin: Plugin) -> None:
        logger.info('Scheduling checks...')
        schedule.every().day.at(config.ATTENDANCE_CHECK_TIME).do(
            cls.broadcast_message_to_promptable_people,
            plugin,
            messages.OFFICE_ATTENDANCE_CHECK
        )
        schedule.every().day.at(config.LUNCH_CHECK_TIME).do(
            cls.broadcast_message_to_promptable_people,
            plugin,
            messages.LUNCH_CHECK
        )
        schedule.every().day.at(config.BEERS_CHECK_TIME).do(
            cls.broadcast_message_to_promptable_people,
            plugin,
            messages.BEERS_CHECK
        )

    @staticmethod
    def broadcast_message_to_promptable_people(plugin: Plugin, message: str) -> None:
        week_day = date.today().weekday()
        if week_day == 5 or week_day == 6:
            logger.info('It is weekend, skipping broadcast...')
            return
        with DataBaseController() as db:
            people = db.get_promptable_people()
        for person in people:
            personalized_message = message.format(username=person.username)
            plugin.driver.create_post(person.channel_id, personalized_message)

    @staticmethod
    def broadcast_message_to_admins(plugin: Plugin, message: str) -> None:
        with DataBaseController() as db:
            people = db.get_admins()
        for person in people:
            personalized_message = message.format(username=person.username)
            plugin.driver.create_post(person.channel_id, personalized_message)

    @classmethod
    async def trigger_check(cls, plugin: Plugin, message: Message, check_type: str) -> str:
        messages_mapping = {
            'attendance': messages.OFFICE_ATTENDANCE_CHECK,
            'lunch': messages.LUNCH_CHECK,
            'beers': messages.BEERS_CHECK
        }
        message_to_broadcast = messages_mapping.get(check_type)
        if message_to_broadcast is None:
            return messages.INVALID_ACTION
        with DataBaseController() as db:
            person = db.get_person(message.sender_name)
            if person is None or not person.is_admin:
                return messages.NO_PERMISSION
        cls.broadcast_message_to_promptable_people(plugin, message_to_broadcast)
        return messages.CHECK_TRIGGERED

    @staticmethod
    async def get_help(message: Message) -> str:
        with DataBaseController() as db:
            person = db.get_person(message.sender_name)
            admin_part = ''
            if person is not None and person.is_admin:
                admin_part = messages.ADMIN_HELP_MESSAGE

        return messages.HELP_MESSAGE.format(admin_part=admin_part)

    @staticmethod
    async def add_user(message: Message) -> str:
        username = message.sender_name
        channel_id = message.channel_id
        with DataBaseController() as db:
            created, person = db.get_or_create_person(username, channel_id, False)
        if created:
            return messages.CREATED_USER.format(channel_id=channel_id)
        return messages.USER_EXISTS

    @staticmethod
    async def delete_user(message: Message, username: str) -> str:
        if username == 'me':
            username = message.sender_name

        with DataBaseController() as db:
            if username != message.sender_name:
                person = db.get_person(message.sender_name)
                if person is None or not person.is_admin:
                    return messages.NO_PERMISSION
            deleted = db.delete_person(username)
        if deleted:
            return messages.DELETED_USER
        return messages.CANT_DELETE

    @staticmethod
    async def add_admin(message: Message, username: str) -> str:
        with DataBaseController() as db:
            person = db.get_person(message.sender_name)
            if person is None or not person.is_admin:
                return messages.NO_PERMISSION
            new_admin = db.get_person(username)
            if not new_admin:
                return messages.DONT_HAVE_USER
            db.set_person_admin_status(new_admin, True)
        return messages.UPGRADED_TO_ADMIN.format(username=username)

    @staticmethod
    async def prompt_user(message: Message, wants_prompts: bool) -> str:
        username = message.sender_name
        with DataBaseController() as db:
            person = db.get_person(username)
            if person is None:
                return messages.DONT_HAVE_USER
            db.set_person_wants_prompts(person, wants_prompts)
        action = '' if wants_prompts else 'not '
        return messages.PROMPT_SETTINGS_CHANGED.format(action=action)

    @classmethod
    async def perform_date_action(cls, message: Message, delete: bool, action: str, day: Optional[date] = None) -> str:
        if day is None:
            day = date.today()
        match action:
            case 'in the office':
                return await cls._perform_in_office_action(message, delete, day)
            case 'bringing lunch':
                return await cls._perform_update_event_action(message, delete, AssistanceEvent.BROUGHT_LUNCH, day)
            case 'eating out':
                return await cls._perform_update_event_action(message, delete, AssistanceEvent.LUNCH_OUTSIDE, day)
            case 'in for beers':
                return await cls._perform_update_event_action(message, delete, AssistanceEvent.IN_FOR_BEERS, day)

        return messages.INVALID_ACTION

    @staticmethod
    async def _perform_in_office_action(message: Message, delete: bool, day: date) -> str:
        username = message.sender_name
        with DataBaseController() as db:
            person = db.get_person(username)
            if person is None:
                return messages.DONT_HAVE_USER
            if delete:
                db.delete_person_assistance_for_date(person, day)
                return messages.DELETED_OFFICE_ASSISTANCE.format(date=day)
            db.get_or_create_person_assistance_for_date(person, day)

        return messages.ADDED_OFFICE_ASSISTANCE.format(date=day)

    @staticmethod
    async def _perform_update_event_action(message: Message, delete: bool, event: AssistanceEvent, day: date) -> str:
        username = message.sender_name
        with DataBaseController() as db:
            person = db.get_person(username)
            if person is None:
                return messages.DONT_HAVE_USER
            person_assistance = db.get_person_assistance_for_date(person, day)
            if not person_assistance:
                return messages.NO_OFFICE_ASSISTANCE
            db.set_person_assistance_event(person_assistance, event, not delete)
        return messages.UPDATED_ASSISTANCE_RECORD.format(date=day)

    @classmethod
    async def get_list_of_people_for_action(cls, action: str, day: Optional[date] = None) -> str:
        if day is None:
            day = date.today()
        match action:
            case 'is in the office':
                return await cls._get_list_of_people_in_office(day)
            case 'brought lunch':
                return await cls._get_list_of_people_with_event(AssistanceEvent.BROUGHT_LUNCH, day)
            case 'eats out':
                return await cls._get_list_of_people_with_event(AssistanceEvent.LUNCH_OUTSIDE, day)
            case 'is in for beers':
                return await cls._get_list_of_people_with_event(AssistanceEvent.IN_FOR_BEERS, day)

        return messages.INVALID_ACTION

    @staticmethod
    async def _get_list_of_people_in_office(day: date) -> str:
        with DataBaseController() as db:
            assistants = db.get_assistants_for_date(day)
        if not assistants:
            return messages.NO_ONE.format(action='is in the office', date=day)
        people = '\n'.join([f'* {assistant.username}' for assistant in assistants])
        return messages.PEOPLE_LIST.format(action='are in the office', date=day, people=people)

    @staticmethod
    async def _get_list_of_people_with_event(event: AssistanceEvent, day: date) -> str:
        with DataBaseController() as db:
            assistants = db.get_assistants_for_event(day, event)
        event_pretty = event.value.replace('_', ' ')
        if not assistants:
            return messages.NO_ONE.format(action=event_pretty, date=day)
        people = '\n'.join([f'* {assistant.username}' for assistant in assistants])
        if not people:
            return messages.NO_ONE.format(action=event_pretty, date=day)
        return messages.PEOPLE_LIST.format(action=event_pretty, date=day, people=people)
