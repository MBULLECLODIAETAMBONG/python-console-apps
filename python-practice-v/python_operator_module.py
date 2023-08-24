# mathematical operators in python using module

import operator

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

addition = operator.add(num1, num2)
print(addition)

subtraction = operator.sub(num1, num2)
print(subtraction)

division = operator.__truediv__(num1, num2)
print(division)

multiplication = operator.mul(num1, num2)
print(multiplication)

