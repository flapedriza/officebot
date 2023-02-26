from mmpy_bot import Bot, Settings

import config
from plugins import OfficeAttendancePlugin

bot = Bot(
    settings=Settings(
        MATTERMOST_URL=config.MATTERMOST_URL,
        MATTERMOST_PORT=config.MATTERMOST_PORT,
        MATTERMOST_API_PATH=config.MATTERMOST_API_PATH,
        BOT_TOKEN=config.BOT_TOKEN,
        BOT_TEAM=config.BOT_TEAM,
    ),
    plugins=[OfficeAttendancePlugin()]
)

bot.run()
