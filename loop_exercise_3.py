# Write a Python program that uses a while loop to repeatedly prompt the user to enter positive numbers, 
# and stops when the user enters -1

# assigning num to zero
num = 1
while(num > -1):
    num2 = int(input("Enter a positive number: "))
# checking if number entered  is greater than -1
    if(num2 > -1):
# prompts the user to enter another positive number
        input("Enter a positive number: ")
    else:
        break
        
