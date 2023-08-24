"""""
 HANDLING EXCEPTION IN PYTHON

In Python, we catch exceptions and handle them using 'try'and 'except' code blocks.
the syntax is:

try:
    # code that may cause an exception
except ExceptionType:
    # code to handle the exception

"""""
# Write a program in python that does division of two numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
try: 
    result = num1 / num2
except Exception as e:
    print("Exception Type:", type(e)) # Getting the type of exception error
    result = None # Defining result
print("The division is:", result)