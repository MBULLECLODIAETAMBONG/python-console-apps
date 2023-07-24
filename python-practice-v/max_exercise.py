# Write a program in python that takes a list of numbers and returns the maximum number in the list

list_of_numbers = [1,2,3,4,5,9,35]

#f using the max() function to obtain the maximum number in the list:

max_number = max(list_of_numbers)
print("The maximum number in the list is: ", max_number)


# method 2 using a for loop

print("using an if elif statement")

num1 = int(input('Enter first number on the list: '))
num2 = int(input('Enter second number on the list: '))
num3 = int(input('Enter third number on the list: '))
total_numbers = [num1, num2, num3]
print(total_numbers)

# using an if elif statement
if(num1 > num2 and num1 > num3):
    print(num1, ": is the maximum number")
    
elif(num2 > num1 and  num2 > num3):
    print(num2, ": is the maximum number")

else:
    print(num3, ": is the maximum number")
