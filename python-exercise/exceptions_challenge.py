"""
Write code to open and read a file
Allow the user to specify the file name
Add error handling to provide a suitable error message if the file specified by the user could not be found

"""
import csv
fileName = input("Enter the file name: ")

accessMode = "r"

try:

    open_File = open(fileName, accessMode) 
    open_File.read(fileName)
    
except: 
    print("sorry the file doesn't exist")

