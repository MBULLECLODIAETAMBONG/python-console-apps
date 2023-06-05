#  Converting an integer to a string
num = 2
print(str(num))

#      Strings Formatting and Strings method

name = str(input("Enter your name please: "))
age  = int(input("What's your age please: "))

#  1. Concatenation 

print("for Concatenation,we have: ")

result = "Hello, my name is " + name + " and am " + str(age) + " years old"
print(result)

#  2. Argument By Positioning (placeholder)

print("Argument By Positioning (placeholder),we have:")

result = "Hello, my name is {n} and am {a} years old".format(n=name, a=age)
print(result)

#   3. f-string

print("for f-strings,we have:")

result = f"Hello, my name is {name} and am {age} years old"
print(result)


