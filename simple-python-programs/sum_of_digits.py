# Python Program to Find Sum of Digits of a Number

number = int(input("Enter a number: "))
sum = 0
# for num in number:
while number >0:
    digit = number %10
    sum = sum + digit
    number = number//10
print(sum)