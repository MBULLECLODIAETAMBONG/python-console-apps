# Python Program to Check Whether a Given Number is Even or Odd using Recursion
def check(number):
    if number % 2 == 0:
        return "The number is Even"
    else:
        return "The number is Odd"
result = check(
    int(input("Enter any number of your choice: "))
)
print(result)

# using print instead of return function to see the difference when using it
def check(number):
    if number % 2 == 0:
        print("The number is Even") 
    else:
        print( "The number is Odd")
check(
    int(input("Enter any number of your choice: "))
)