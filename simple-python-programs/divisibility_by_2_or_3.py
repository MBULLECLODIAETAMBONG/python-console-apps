# Python Program to Print All Integers that Aren’t Divisible by Either 2 or 3

# def check_divisibility(numbers):
numbers = int(input("Enter a number: "))
for num in range(numbers):
    if (num % 2 !=0) and (num % 3 !=0):
        print(num)
