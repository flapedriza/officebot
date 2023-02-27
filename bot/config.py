import os

MATTERMOST_URL = os.getenv('MATTERMOST_URL', 'http://localhost')
MATTERMOST_PORT = int(os.getenv('MATTERMOST_PORT', 8065))
MATTERMOST_API_PATH = os.getenv('MATTERMOST_API_PATH', '/api/v4')
BOT_TOKEN = os.getenv('BOT_TOKEN', '')
BOT_TEAM = os.getenv('BOT_TEAM', 'testeam')
DB_PATH = '/data/database.db'
ECHO_DB_ACTIONS = True
DATE_FORMAT = '%d/%m/%Y'
ATTENDANCE_CHECK_TIME = '07:00'
LUNCH_CHECK_TIME = '12:30'
BEERS_CHECK_TIME = '17:00'
BROADCASTS_NOT_ALLOWED_DAYS = [5, 6]
