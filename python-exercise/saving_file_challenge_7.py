"""
create a csv file 
Extra credit!  Ask your user to enter names and ages for 5 different guests, then save each name and age to your CSV file

"""
import csv

with open('protagonist.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Movie", "Protagonist"])
    writer.writerow([1, "Lord of the Rings", "Frodo Baggins"])
    writer.writerow([2, "Harry Potter", "Harry Potter"])





