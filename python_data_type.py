# There are several data types in python

# 1. STRING

print("Data Type STRING")

name = str(input("Enter your name: "))
if(len(name)>=5):
    print("You are Welcome", name,"!!!")
else:
    print("your name is too short", name)

#         OUTPUTING THE TYPE OF DATA TYPE
print("Data Type is of : ",type(name))
    

#  2.  NUMBER

# a) INTEGER
print("Data Type INTEGER")
leap_year = int(input("Enter any year: "))
if(leap_year %4 ==0):
    print("The year", leap_year,"IS A leap year")
else:
    print("The year", leap_year, "IS NOT a leap_year")

#         OUTPUTING THE TYPE OF DATA TYPE
print("Data Type is of : ",type(leap_year))
    

#  b) FLOAT
number = float(input("Enter any float number: "))
print(number,"is a floating point number")

#         OUTPUTING THE TYPE OF DATA TYPE
print("Data Type is of : ",type(number))
    

# C) COMPLEX NUMBER
a = 2 + 3j
b = 6 - 2j
result = a + b
print(result)

#         OUTPUTING THE TYPE OF DATA TYPE
print("Data Type is of : ",type(result))
    


#   3.  DATE AND TIME

print("Data Type DATE AND TIME")

from datetime import datetime  # importing the datetime from the python library
say_time = (datetime.now())    #  outputs the date and time
print(say_time)

#         OUTPUTING THE TYPE OF DATA TYPE
print("Data Type is of : ",type(say_time))
    

# making the datetime more readable
from time import strftime

#  strftime() Python – Datetime Format Tutorial
#  strftime() is a Python date method you can use to convert dates to strings.

simple_datetime = strftime('%Y-%m-%d %H:%M:%S')
print(simple_datetime)

#  IF ELSE STATEMENT

first_name = str(input("Enter your first name: "))
last_name = str(input("Enter your last name: "))
if(first_name > last_name):
    print(first_name, "is greater than last name")
else:
    print(last_name, "is greater than first name")


#  BOOLEAN

print("DATA TYPE BOOLEAN")
      
bool_1 = str(input("Enter your first name: "))
bool_2 = str(input("Enter your last name: "))
result = bool_1 > bool_2
print(result)

#         OUTPUTING THE TYPE OF DATA TYPE
print("Data Type is of : ",type(result))
    

# LIST

print("Data Type LIST")
      
fruits = ["Mangoes", "Apple", "Pineapple", "Pawpaw"]
print(fruits[2])

# using python methods in list and other

# append() method
print("This is the append()")
fruits.append("Banana")
print(fruits)

#  remove() method
print("This is the remove()")
fruits.remove("Mangoes")
print(fruits)

#  replace() method
print("This is the insert()")
fruits.insert(2, "Coconuts")
print(fruits)

#  min() and max() method
print("The minimum fruit in the list of fruits is: ", min(fruits))
print("The maximum fruit in the list of fruits is: ",max(fruits))

#         OUTPUTING THE TYPE OF DATA TYPE
print("Data Type is of : ",type(fruits))
    

#    DICTIONARY

print("Data Type DICTIONARY")

phone_book = {
    "daddy": 67744234,
    "mummy": 97834524,
    "sandra": 8092334,
    "cunnel": 9082145
    }
print(phone_book)

# using the len() method to obtain the length of the dictionary
print(len(phone_book))

# clear() to remove all entries in the dictionary,
phone_book.clear()
print(phone_book)

# to delete the dictionary, we use the del method
del phone_book
print(phone_book)





























