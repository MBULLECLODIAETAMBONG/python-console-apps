"""
How to save,read and write information in files

Use the open function to create and open a file
	myFile = open(fileName, accessMode) 
 
You must specify
 - file name
 - access mode 
"""

fileName = "my_python_file.txt" 
accessMode = "w" 
myFile = open(fileName, accessMode) 
myFile.write("Hi there!\n How are you")

myFile.close()

