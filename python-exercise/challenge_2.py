"""
Write a program that:
Ask a user to enter the deadline for their project
Tell them how many days they have to complete the project
For extra credit, give them the answer as a combination of 
weeks & days (Hint: you will need some of the math functions from the module on numeric values)

"""
import datetime

# Prompting the user to enter project's deadline
project_deadline = input("What's your project's deadline (%d-%m-%Y): ")

# converting the date the user enter from string object to date
project_deadline_converted = datetime.datetime.strptime(project_deadline, "%d-%m-%Y").date()

# Getting current date
current_date = datetime.date.today()

# current_date_converted = datetime.datetime.strptime(str(current_date), "%d-%m-%Y").date()

days_left = project_deadline_converted - current_date 

print("You have", days_left.days, "days")




# Testing: Getting the current time 
today_date = datetime.datetime.now()
print("The date of today is :", today_date)


# Dealing with different time zone 

# 1. Getting EST time zone
 

# we import from datetime datetime, timedelta and timezone
from datetime import datetime, timedelta, timezone

# we specify the timezone by assigning a timezone which takes the timedelta with its hours different to a variable
EST_timezone = timezone(timedelta(hours=-6))

# we get the current time of the default zone

# we get the time 
EST_time = datetime(2023, 11, 20, 20, 0, 0, tzinfo=EST_timezone)
print("The Eastern Standard Time now is :", EST_time )









