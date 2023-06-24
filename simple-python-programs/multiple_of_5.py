# Python Program to Find Numbers which are Divisible by 7 and Multiple of 5 in a Given Range


# function definition
def divisibility(numbers):
    
    # creating an empty list so that we can append all the divisible and multiple numbers in the list
    all_numbers = []
    for num in range(numbers):
        # checking the condition
        if num % 7 == 0 and num % 5 ==0:
            # appending all numbers that satisfy the above condition
            all_numbers.append(num)
    return all_numbers

# function call
result = divisibility(
    int(input("Enter a number: "))
)
print(result)


# solution without using function

numbers = int(input("Enter a number: "))
for num in range(numbers):
    if num % 7 == 0 and num % 5 ==0:
        print(num)