# There are several data types in python

# 1. STRING
print("Data Type STRING")
name = str(input("Enter your name: "))
if(len(name)>=5):
    print("You are Welcome", name,"!!!")
else:
    print("your name is too short", name)
    

#  2.  NUMBER

# a) INTEGER
print("Data Type INTEGER")
leap_year = int(input("Enter any year: "))
if(leap_year %4 ==0):
    print("The year", leap_year,"IS A leap year")
else:
    print("The year", leap_year, "IS NOT a leap_year")

#  b) FLOAT
number = float(input("Enter any float number: "))

print(number,"is a floating point number")

# C) COMPLEX NUMBER
a = 2 + 3j
b = 6 - 2j
result = a + b
print(result)


#   3.  DATE AND TIME
from datetime import datetime  # importing the datetime from the python library
say_time = (datetime.now())    #  outputs the date and time
print(say_time)

# making the datetime more readable
from time import strftime

#  strftime() Python – Datetime Format Tutorial
#  strftime() is a Python date method you can use to convert dates to strings.

simple_datetime = strftime('%Y-%m-%d %H:%M:%S')
print(simple_datetime)

#  BOOLEAN

first_name = str(input("Enter your first name: "))
last_name = str(input("Enter your last name: "))
if(first_name > last_name):
    print(first_name, "is greater than last name")
else:
    print(last_name, "is greater than first name")


