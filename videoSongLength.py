'''
POTENTIAL TO DOS
-ideally the program would wait 1-3 seconds until it really quits, otherwise the user cannot see the "Thanks for using the program"

- TODO: some of it might be easier with "dateutil" third-party party library
https://dateutil.readthedocs.io/en/stable/ which is recommended e.g. on
https://realpython.com/lessons/date-time-arithmetic/. Especially the following is aussichtsreich:
"Computing of relative deltas between two given date and/or datetime objects;"

-Calculate Relations (ua wie oft 80-Jähriger gelebt, aber auch andere) (Units do not matter here)_TODO
Print how long video is watched in appropriate additonal Unit (80-Jähriger), sprich dass_
die größte Einheit die größer-gleich "bestimmter Wert" ist, also z.B. sobald mind X, ist eine bestimmte Einheit relevant
'''

from datetime import timedelta
import pyinputplus as pyip
import sys

#The welcome text is displayed.
print('''FOR HOW LONG A VIDEO OR SONG HAS BEEN PLAYED
Many videos and songs have been played millions of times. But for how long has each been played (e.g. weeks/months/years) if each time counts?
This calculator enables you to find it out!
''')

while True:
    #The user gives information about the song/video.
    input_number_played = pyip.inputInt(min = 1, max = 9999999999999999, prompt = 'How many times has the video or song been played? Please type the number (e.g. "1000") and press Enter >>> ')

    print("How long is the video or song? Please type the number of hours, minutes and seconds.")

    input_hours = pyip.inputInt(min = 0, max = 100, prompt = 'number of hours: >>> ' )
    input_minutes = pyip.inputInt(min = 0, max = 59, prompt= 'number of minutes: >>>' )
    input_seconds = pyip.inputInt(min = 0, max = 59, prompt = 'number of seconds: >>> ')
    
    '''
    The amount of hours, minutes and seconds of the song/video being played is calculated.
    '''
    time_input_delta = timedelta(hours = input_hours) + timedelta(minutes= input_minutes) + timedelta(seconds= input_seconds)
    time_input_muliplied_delta = time_input_delta *  input_number_played

    # (((TODO: I might change the folowing 6 variables with the
    # ~symbol change feature into "output_in_seconds" etc. as this is
    # probably a clearer name)))
    time_in_seconds = time_input_muliplied_delta / timedelta(seconds = 1)
    time_in_minutes = time_input_muliplied_delta / timedelta(minutes = 1)
    time_in_hours = time_input_muliplied_delta / timedelta(hours = 1)
    time_in_days = time_input_muliplied_delta / timedelta(days = 1)
    time_in_weeks = time_input_muliplied_delta / timedelta(weeks = 1)
    time_in_years = time_input_muliplied_delta / timedelta(days = 365)

    #TODO: For the seconds below it is not really necessary to make use of the "round"-funtion.
    #The full amount of time the song/video has been played is displayed for the user.
    print("---This video or song has been played for", round(time_in_years, 2), "years or", round(time_in_weeks, 2), "weeks or", round(time_in_days, 2), "days or", round(time_in_hours, 2), "hours or", round(time_in_minutes, 2), "minutes or", round(time_in_seconds, 2), "seconds.---")
    
    #The user can make another calculation or quit the program.
    print("Do you want to make another calculation or quit the program?")
    proceed_how = pyip.inputMenu(['AGAIN', 'QUIT'], lettered=True, numbered=False)
    
    if proceed_how == 'AGAIN':
        continue
    if proceed_how == 'QUIT':
        print("Thanks for using the program!")
        sys.exit()







