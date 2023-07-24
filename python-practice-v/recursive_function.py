#     RECURSIVE FUNCTION

# A Recursive function is a function that calls itself. it can call itself again and again...

# write a function that cal the factorial of a number

from math import factorial
import math
import random
def  cal_factorial(n):
    
    if n >= 1:
        fac = n * factorial(n-1) 
        print(fac)
    else:
        print("enter a positive number")
        
cal_factorial(n = int(input("Enter any number so as to calculate the factorial: ")))

# Getting Random numbers using the randint() method
num = random.randint(25, 35)
print(num)


#  return statement does not output result for users to see as shown below

def number(x):
    if (x %2 ==0):
        return "EVEN"
        
    else:
        return "ODD"
        
number(x = int(input("Enter a Number: ")))