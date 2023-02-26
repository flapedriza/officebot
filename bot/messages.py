ADMIN_HELP_MESSAGE = """

Since you are an admin user, you can also tell me the following things in a private conversation:
* **Add [username]**: Create a user for the given username
* **Delete [username]**: Delete the user from the database
* **Trigger attendance check**: Ask everyone who has prompts activated if they are in the office today
* **Trigger lunch check**: Ask everyone who has prompts activated what they are doing for lunch today
* **Trigger beers check**: Ask everyone who has prompts activated if they are in for beers today
* **Give admin to [username]**: Set the given user as an admin

"""
HELP_MESSAGE = """
When you are in a private conversation with me, you can tell me the following things:
* **Help**: Show this message
* **Add me**: Create a user for you
* **I am in the office today**: Create a record that indicates that you are in the office today
* **I am not in the office today**: Delete the record that indicates that you are in the office today
* **I will go to the office on [dd/mm/yyyy]**: Create a record that indicates that you will go to the office on the given date
* **I will not go to the office on [dd/mm/yyyy]**: Delete the record that indicates that you will go to the office on the given date
* **I am bringing lunch today**: Store on today's record that you brought lunch
* **I am not bringing lunch today**: Remove the indication that you brought lunch from today's record
* **I will bring lunch on [dd/mm/yyyy]**: Store on the given date's record that you will bring lunch
* **I will not bring lunch on [dd/mm/yyyy]**: Remove the indication that you will bring lunch from the record of the given date
* **I am eating out today**: Store on today's record that you will eat out
* **I am not eating out today**: Remove the indication that you will eat out from today's record
* **I will eat out on [dd/mm/yyyy]**: Store on the given date's record that you will eat out
* **I will not eat out on [dd/mm/yyyy]**: Remove the indication that you will eat out from the record of the given date
* **I am in for beers today**: Store on today's record that you are in for beers
* **I am not in for beers today**: Remove the indication that you are in for beers from today's record
* **I will be in for beers on [dd/mm/yyyy]**: Store on the given date's record that you will be in for beers
* **I will not be in for beers on [dd/mm/yyyy]**: Remove the indication that you will be in for beers from the record of the given date
* **Prompt me**: If you want me to ask you every day if you are in the office, what you're doing for lunch and if you're in for beers, tell me this (you can ignore the messages and I will just not store anything)
* **Do not prompt me**: If you don't want me to ask you anymore, tell me this
* **Delete me**: Delete your user from the database
{admin_part}

You can also ask me all of this both in the group and in a private conversation:
* **Who is in the office today?**: Show the usernames of the people that are in the office today
* **Who will be in the office on [dd/mm/yyyy]?**: Show the usernames of the people that will be in the office on the given date
* **Who brought lunch today?**: Show the usernames of the people that brought lunch today
* **Who will bring lunch on [dd/mm/yyyy]?**: Show the usernames of the people that will bring lunch on the given date
* **Who eats out today?**: Show the usernames of the people that will eat out today
* **Who will eat out on [dd/mm/yyyy]?**: Show the usernames of the people that will eat out on the given date
* **Who is in for beers today?**: Show the usernames of the people that are in for beers today
* **Who will be in for beers on [dd/mm/yyyy]?**: Show the usernames of the people that will be in for beers on the given date
"""

BOT_START_MESSAGE = 'I just came to life!'
BOT_STOP_MESSAGE = 'I am going to commit seppuku, it was a pleasure to serve you'

CREATED_USER = 'I created a user for you! your channel_id is {channel_id}.\nIf you want me to ask you every day if you are in the office, tell me "Prompt me"\nIf you want to know what I can do, just say "Help"'
USER_EXISTS = 'You already have a user!'

NO_PERMISSION = 'You do not have permission to perform that action'
INVALID_ACTION = 'This is an invalid action, say "Help" to see what I can do'

DELETED_USER = 'The user has been deleted!'
CANT_DELETE = 'I could not delete that user, probably because it does not exist'

UPGRADED_TO_ADMIN = '{username} has been upgraded to admin!'

CHECK_TRIGGERED = 'Sent the check to everyone that accepts prompts'

PROMPT_SETTINGS_CHANGED = 'From now on, I will {action}ask you every day if you are in the office, what you are doing for lunch and if you are in for beers'

DONT_HAVE_USER = 'I could not perform that action because you do not have a user, you can create one by telling me "Add me"'
NO_OFFICE_ASSISTANCE = 'You do not have any record that indicates that you are in the office that day, so I cannot do this'

DELETED_OFFICE_ASSISTANCE = 'I deleted the record that indicated that you were in the office on {date}'
ADDED_OFFICE_ASSISTANCE = 'I created a record that indicates that you are in the office on {date}'

UPDATED_ASSISTANCE_RECORD = 'I updated your office assistance record for {date}'

NO_ONE = 'It seems that no one {action} on {date}'
PEOPLE_LIST = 'The following people {action} on {date}:\n{people}'

OFFICE_ATTENDANCE_CHECK = 'Hey {username}, will you be in the office today?\nIf so, say "I am in the office today".\nRemember that you can always opt out of those messages by saying "Do not prompt me".'
LUNCH_CHECK = 'Hey {username}, what are you doing for lunch today?\nIf you are bringing lunch, say "I am bringing lunch today".\nIf you are eating out, say "I am eating out today".\nRemember that you can always opt out of those messages by saying "Do not prompt me".'
BEERS_CHECK = 'Hey {username}, are you in for beers today?\nIf so, say "I am in for beers today".\nRemember that you can always opt out of those messages by saying "Do not prompt me".'
