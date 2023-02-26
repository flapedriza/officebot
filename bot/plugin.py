import re
from datetime import datetime
from typing import Optional

from mmpy_bot import Plugin, listen_to, Message

import config
from action_controller import ActionController


class OfficeBotPlugin(Plugin):
    def __init__(self) -> None:
        self.action_controller = ActionController()
        super().__init__()

    def on_start(self) -> None:
        self.action_controller.on_start(self)

    def on_stop(self) -> None:
        self.action_controller.on_stop(self)

    @listen_to(r'^Help$', re.IGNORECASE, direct_only=True)
    async def help(self, message: Message) -> None:
        response = await self.action_controller.get_help(message)
        self.driver.create_post(message.channel_id, response)

    @listen_to(r'^Add me$', re.IGNORECASE, direct_only=True)
    async def add_me(self, message: Message) -> None:
        response = await self.action_controller.add_user(message)
        self.driver.create_post(message.channel_id, response)

    @listen_to(r'^Delete ([a-z]+)$', re.IGNORECASE, direct_only=True)
    async def delete_user(self, message: Message, username: str) -> None:
        response = await self.action_controller.delete_user(message, username)
        self.driver.create_post(message.channel_id, response)

    @listen_to(r'^Give admin to ([a-z]+)$', re.IGNORECASE, direct_only=True)
    async def set_admin(self, message: Message, username: str) -> None:
        response = await self.action_controller.add_admin(message, username)
        self.driver.create_post(message.channel_id, response)

    @listen_to(r'^Trigger ([a-z]+) check$', re.IGNORECASE, direct_only=True)
    async def trigger_check(self, message: Message, check_type: str) -> None:
        response = await self.action_controller.trigger_check(self, message, check_type)
        self.driver.create_post(message.channel_id, response)

    @listen_to(r'^Prompt me$', re.IGNORECASE, direct_only=True)
    async def prompt_me(self, message: Message) -> None:
        response = await self.action_controller.prompt_user(message, True)
        self.driver.create_post(message.channel_id, response)

    @listen_to(r'^Do not prompt me$', re.IGNORECASE, direct_only=True)
    async def do_not_prompt_me(self, message: Message) -> None:
        response = await self.action_controller.prompt_user(message, False)
        self.driver.create_post(message.channel_id, response)

    @listen_to(r'^I am (not )?([a-z ]+) today$', re.IGNORECASE, direct_only=True)
    async def today_action(self, message: Message, not_match: Optional[str], action: str) -> None:
        delete = not_match is not None
        response = await self.action_controller.perform_date_action(message, delete, action)
        self.driver.create_post(message.channel_id, response)

    @listen_to(r'^I will (not )?([a-z ]+) on ([0-9]{2}\/[0-9]{2}\/[0-9]{4})$', re.IGNORECASE, direct_only=True)
    async def future_action(self, message: Message, not_match: Optional[str], action: str, action_date: str) -> None:
        delete = not_match is not None
        action_conversion = {
            'go to the office': 'in the office',
            'bring lunch': 'bringing lunch',
            'eat out': 'eating out',
            'be in for beers': 'in for beers',
        }
        action = action_conversion.get(action, action)
        action_date_object = datetime.strptime(action_date, config.DATE_FORMAT).date()
        response = await self.action_controller.perform_date_action(message, delete, action, action_date_object)
        self.driver.reply_to(message, response)

    @listen_to(r'^Who ([a-z ]+) today$', re.IGNORECASE, needs_mention=True)
    async def list_people_action(self, message: Message, action: str) -> None:
        response = await self.action_controller.get_list_of_people_for_action(action)
        self.driver.create_post(message.channel_id, response)

    @listen_to(
        r'^Who will ([a-z ]+) on ([0-9]{2}\/[0-9]{2}\/[0-9]{4})$',
        re.IGNORECASE,
        needs_mention=True
    )
    async def list_people_action_date(self, message: Message, action: str, action_date: str) -> None:
        action_conversion = {
            'be in the office': 'is in the office',
            'bring lunch': 'brought lunch',
            'eat out': 'eats out',
            'be in for beers': 'is in for beers',
        }
        action = action_conversion.get(action, action)
        action_date_object = datetime.strptime(action_date, config.DATE_FORMAT).date()
        response = await self.action_controller.get_list_of_people_for_action(action, action_date_object)
        self.driver.create_post(message.channel_id, response)
