* In private conversation:
  * `^Help$`: Show commands
  * `^Add me$`: Create a Person for the user
  * `^Delete me$`: Delete Person from database
  * `^Prompt me$`: Set Person wants_prompts to true
  * `^Do not prompt me$`: Set Person wants_prompts to false
  * `^I am (not )?([a-z ]+) today$`
    * not in the office: Delete the PersonAttendance for today
    * not bringing lunch: Set today's PersonAttendance brought_lunch to false
    * not eating out: Set today's PersonAttendance lunch_outside to false
    * not in for beers: Set today's PersonAttendance in_for_beers to false
    * in the office: Create a PersonAttendance for today
    * bringing lunch: Set today's PersonAttendance brought_lunch to true
    * eating out: Set today's PersonAttendance lunch_outside to true
    * in for beers: Set today's PersonAttendance in_for_beers to true
  * `^I will (not )?([a-z ]+) on ([0-9]{2}\/[0-9]{2}\/[0-9]{4})$`
    * not go to the office: Delete the PersonAttendance for the given date
    * not bring lunch: Set the given date's PersonAttendance brought_lunch to false
    * not eat out: Set the given date's PersonAttendance lunch_outside to false
    * not be in for beers: Set the given date's PersonAttendance in_for_beers to false
    * go to the office: Create a PersonAttendance for the given date
    * bring lunch: Set the given date's PersonAttendance brought_lunch to true
    * eat out: Set the given date's PersonAttendance lunch_outside to true
    * be in for beers: Set the given date's PersonAttendance in_for_beers to true
  * `^I will (not )?([a-z ]+) tomorrow$`
    * not go to the office: Delete the PersonAttendance for the given date
    * not bring lunch: Set the given date's PersonAttendance brought_lunch to false
    * not eat out: Set the given date's PersonAttendance lunch_outside to false
    * not be in for beers: Set the given date's PersonAttendance in_for_beers to false
    * go to the office: Create a PersonAttendance for the given date
    * bring lunch: Set the given date's PersonAttendance brought_lunch to true
    * eat out: Set the given date's PersonAttendance lunch_outside to true
    * be in for beers: Set the given date's PersonAttendance in_for_beers to true

* In private conversation (only for admins):
  * `^Delete ([a-z]+)$`: Delete Person from database
  * `^Trigger ([a-z]+) check$`
    * attendance: Trigger the attendance check for today
    * lunch: Trigger the lunch check for today
    * beers: Trigger the beers check for today
  * `^Give admin to ([a-z]+)$`: Set Person is_admin to true
* In private or group:
  * `^Who ([a-z ]+) today$`
    * is in the office: Show the usernames of today's PersonAssistances Persons
    * brought lunch: Show the usernames of today's PersonAssistances Persons with brought_lunch true
    * eats out: Show the usernames of today's PersonAssistances Persons with lunch_outside true
    * is in for beers: Show the usernames of today's PersonAssistances Persons with in_for_beers true
  * `^Who will ([a-z ]+) on ([0-9]{2}\/[0-9]{2}\/[0-9]{4})$`
    * be in the office: Show the usernames of the given date's PersonAssistances Persons
    * bring lunch: Show the usernames of the given date's PersonAssistances Persons with brought_lunch true
    * eat out: Show the usernames of the given date's PersonAssistances Persons with lunch_outside true
    * be in for beers: Show the usernames of the given date's PersonAssistances Persons with in_for_beers true
  * `^Who will ([a-z ]+) on tomorrow$`
    * be in the office: Show the usernames of the given date's PersonAssistances Persons
    * bring lunch: Show the usernames of the given date's PersonAssistances Persons with brought_lunch true
    * eat out: Show the usernames of the given date's PersonAssistances Persons with lunch_outside true
    * be in for beers: Show the usernames of the given date's PersonAssistances Persons with in_for_beers true
