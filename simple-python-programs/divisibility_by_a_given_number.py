# Python Program to Print All Numbers in a Range Divisible by a Given Number


def check_divisibility(number):
    divisible_number = int(input("Enter the number you want to check the divisibility: "))
    for num in range(number):
        if num % divisible_number == 0:
            print(num)

check_divisibility(int(input("Enter a number: ")))
