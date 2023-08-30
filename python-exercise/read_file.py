"""
Write a program that will print the names and ages of the guests in the guest list file you created in the last module

If you didn’t do the last challenge, you can just create a 
file to read using Notepad that contains names and ages 

"""
# Firstly we import the csv module
import csv

# we  initialize the file we already created to a variable
fileName  = "protagonist.csv"

# we initialize the accessMode to be 'r' since we want read the file
accessMode = "r"

# we use the 'with'keyword with the open() method in order to open the file we want to read
with open(fileName, accessMode) as csvFile:
    data_file = csv.reader(csvFile)   # we use the csv.reader() method to read the file
    for row in data_file:             # using a for loop to loop through the data file (file)
        print(row)