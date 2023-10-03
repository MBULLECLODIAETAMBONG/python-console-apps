# DATE TIME IN PYTHON

import datetime 

#                           SECTION A DATE

#            1. To get the default date format 
print(datetime.date.today())   

"""
In python, we use the strftime() to formate date 

    %d is the day of the month
    %b is the abbreviation for the month
    %B is the full month name
    %Y is the 4 digit year
    %y is two digit year
    %a is the day of the week abbreviated
    %A is the day of the week
    %m is the month

"""

current_date = datetime.date.today()   # To get today's date


#               2.Getting today's date in word format
print(current_date.strftime('Please attend our event %A, %B %d in the year %Y'))

"""
strftime    and    strptime

The difference between strptime and strftime in Python is that strptime is 
used to convert a string to a datetime object, while strftime is to format the date
"""

#             3. Write a program that ask the user's date of birth and prints the output

# We specify the date format the user ought to enter so as to bypass our code from crashing 
birth_date = input("Please enter your date of birth (%d-%m-%Y): ")
birth_day = datetime.datetime.strptime(birth_date, "%d-%m-%Y").date()  # using the strptime because date_of_birth is a string and needs to be converted to date object
print("your birthday is ", birth_day.strftime("%d %B"))


# 4. To get someone's next birthday from a specific year
current_birthday = datetime.datetime.strptime("2-1-2023", "%d-%m-%Y").date()   # current birthday
today_date = datetime.date.today()
# Getting the difference in date
next_birthday = today_date - current_birthday
print(next_birthday.days)    # Getting the difference in days


print(today_date, datetime. timedelta(days=2))
print(today_date, datetime. timedelta(hours=4))


#                                SECTION B  TIME

"""
we also use the strftime() to formate time

    %H 	Hours (24 hr clock)
    %I 	Hours (12 hr clock)
    %p 	AM or PM
    %m 	Minutes
    %S 	Seconds

"""
print("getting date and time")
print(datetime.datetime.now())    # getting date and time

# using the strftime format to format time
current_time = datetime.datetime.now()    
print("Current Time in hrs and mins is:", datetime.datetime.strftime(current_time, "%H:%M"))    # getting date in hr and mins
print("Current Time in am or pm is:", datetime.datetime.strftime(current_time, "%H:%M%p"))    # getting date with am or pm


# Using timedelta": it is used to determine what the date of tomorrow or previous or future dates

print('USING timedelta to determine dates')

import datetime
today = datetime.date.today()
print('Today:', today)
yesterday = today - datetime.timedelta(days=1)
print('Yesterday:', yesterday)
tomorrow = today + datetime.timedelta(days=1)
print('Tomorrow:', tomorrow)
print('Time between tomorrow and yesterday:', tomorrow - yesterday)