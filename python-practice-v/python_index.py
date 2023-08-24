# write a program in python that returns the index 
name = "Am Called Clodia the Engineer from COLLEGE OF TECHNOLOGY"
print(name[0:16])

# concatination
# can't concatenate a sting to an integer, can only concatinate a string to a string
print("concatination of strings in python")
new_name = name + ", Am "+ str(23)
print(new_name)

# write a program that request a user to enter a number and checks if a number the user entered is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")
    

# write a program tha stores monthly expenses in a list and finds out the total expenses for all months

monthly_expenses = [3000, 1000, 5000, 2000]
counter = 0
for m in monthly_expenses:
    counter = counter + m
print("monthly expenses = ", counter, "frs")
