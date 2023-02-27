DETAILED_ADMIN_HELP_MESSAGE = """

**Since you are an admin user, you can also tell me the following things in a private conversation:**
* **Delete [username]**: I will delete the user with that username from the database
* **Trigger attendance check**: I will ask everyone who has prompts activated if they are in the office today
* **Trigger lunch check**: I will sk everyone who has prompts activated what they are doing for lunch today
* **Trigger beers check**: I will ask everyone who has prompts activated if they are in for beers today
* **Give admin to [username]**: I will give the user with that username admin privileges
"""
DETAILED_HELP_MESSAGE = """
**Those are the most important commands that you can use to interact with me. You can only use them in our private conversation:**
* **Help**: I will show this message again
* **Helpshort:** I will show a shorter and more straightforward version of this message
* **Add me**: I will create a user for you if you do not have one already, you will need a user to be able to further interact with me
* **Delete me**: I will delete your user from the database including all your past and future office attendance records
* **Prompt me**: If you want me to ask you every day if you are in the office, what you're doing for lunch and if you're in for beers so you do not forget to inform me, tell me this (If you do not answer me, I will just assume that you are not in the office)
* **Do not prompt me**: If you don't want me to ask you the previous anymore, tell me this
* **I am in the office today**: I will store that you are in the office today so I can include you in the list when someone asks me who is in the office. You will need to tell me this before any of the things below
* **I am bringing lunch today**: I will store that you are bringing lunch today so I can include you in the list when someone asks me who brought lunch
* **I am eating out today**: I will store that you want to eat out today so I can include you in the list when someone asks me who wants to eating out
* **I am in for beers today**: I will store that you are in for beers today so I can include you in the list when someone asks me who is in for beers
* **I am not in the office today**: I will remove the indication that you are in the office today from my records, if people ask me who is in the office today, I will not include you in the list anymore
* **I am not bringing lunch today**: I will remove the indication that you are bringing lunch today from my records, if people ask me who brought lunch today, I will not include you in the list anymore
* **I am not eating out today**: I will remove the indication that you want to eat out today from my records, if people ask me who wants to eat out today, I will not include you in the list anymore
* **I am not in for beers today**: I will remove the indication that you are in for beers today from my records, if people ask me who is in for beers today, I will not include you in the list anymore

**Those commands are useful to be informed about what is going on in the office, you can use them both in our private conversation and in the office channel:**
* **Who is in the office today?**: I will show a list with the usernames of the people that are in the office today
* **Who brought lunch today?**: I will show a list with the usernames of the people that brought lunch today
* **Who eats out today?**: I will show a list with the usernames of the people that want to eat out today
* **Who is in for beers today?**: I will show a list with the usernames of the people that are in for beers today

**If you like to plan ahead, you can use the following commands in our private conversation to tell me what you are going to do in the future:**
* **I will go to the office on [dd/mm/yyyy]**: I will store on the given date's record that you will go to the office, this is the same as telling me **"I am in the office today"** but for a future date
* **I will bring lunch on [dd/mm/yyyy]**: I will store on the given date's record that you will bring lunch, this is the same as telling me **"I am bringing lunch today"** but for a future date
* **I will eat out on [dd/mm/yyyy]**: I will store on the given date's record that you will want to eat out, this is the same as telling me **"I am eating out today"** but for a future date
* **I will be in for beers on [dd/mm/yyyy]**: I will store on the given date's record that you will be in for beers, this is the same as telling me **"I am in for beers today"** but for a future date
* **I will not go to the office on [dd/mm/yyyy]**: I will remove the indication that you will go to the office from the record of the given date, this is the same as telling me **"I am not in the office today"** but for a future date
* **I will not bring lunch on [dd/mm/yyyy]**: I will remove the indication that you will bring lunch from the record of the given date, this is the same as telling me **"I am not bringing lunch today"** but for a future date
* **I will not eat out on [dd/mm/yyyy]**: I will remove the indication that you will want to eat out from the record of the given date, this is the same as telling me **"I am not eating out today"** but for a future date
* **I will not be in for beers on [dd/mm/yyyy]**: I will remove the indication that you will be in for beers from the record of the given date, this is the same as telling me **"I am not in for beers today"** but for a future date

**With those commands you can also ask me what is going to happen in the office in the future, you can use them both in our private conversation and in the office channel:
* **Who will be in the office on [dd/mm/yyyy]?**: I will show a list with the usernames of the people that will be in the office on the given date
* **Who will bring lunch on [dd/mm/yyyy]?**: I will show a list with the usernames of the people that will bring lunch on the given date
* **Who will eat out on [dd/mm/yyyy]?**: I will show a list with the usernames of the people that will want to eat out on the given date
* **Who will be in for beers on [dd/mm/yyyy]?**: I will show a list with the usernames of the people that will be in for beers on the given date
{admin_part}

**Remember that you can get a brief list of the most common commands you can use with me by saying "Helpshort"**
"""

SHORT_HELP_MESSAGE = """
**Here are the most common commands you can use in private:**
* **Help**
* **Add me**
* **Delete me**
* **Prompt me**
* **Do not prompt me**
* **I am in the office today**
* **I am bringing lunch today**
* **I am eating out today**
* **I am in for beers today**
* **I am not in the office today**
* **I am not bringing lunch today**
* **I am not eating out today**
* **I am not in for beers today**

**Those work both in private and in the office channel:**
* **Who is in the office today?**
* **Who brought lunch today?**
* **Who eats out today?**
* **Who is in for beers today?**

**If you want to know more, just say "Help"**
"""

BOT_START_MESSAGE = 'I just came to life!'
BOT_STOP_MESSAGE = 'I am going to commit seppuku, it was a pleasure to serve you'

CREATED_USER = 'I created a user for you! your channel_id is {channel_id} (store it just in case you have issues with me and need to contact my creator).\nIf you want me to ask you every day if you are in the office, tell me "Prompt me"\nIf you want to know what else I can do, just say "Help"'
USER_EXISTS = 'You already have a user!\nSay "Help" to see what I can do'

NO_PERMISSION = 'You do not have permission to perform that action'
INVALID_ACTION = 'This is an invalid action, say "Help" to see what I can do'
NO_BROADCASTS_TODAY = 'Broadcasts are not allowed today'

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

OFFICE_ATTENDANCE_CHECK = 'Hey {username}!, will you be in the office today?\nIf so, say "I am in the office today".\nIf you will not be in the office or you do not want anyone to know ignore this message\nRemember that you can always opt out of those messages by saying "Do not prompt me".'
LUNCH_CHECK = 'Hey {username}, what are you doing for lunch today?\nIf you are bringing lunch, say "I am bringing lunch today".\nIf you are eating out, say "I am eating out today".\nYou can ignore this message if you are not bringing lunch or eating out.\nRemember that you can always opt out of those messages by saying "Do not prompt me".'
BEERS_CHECK = 'Hey {username}, are you in for beers today?\nIf so, say "I am in for beers today".\nYou can ignore this message if you are not in for beers.\nRemember that you can always opt out of those messages by saying "Do not prompt me".'
