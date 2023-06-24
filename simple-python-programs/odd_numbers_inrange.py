# Python Program to Print All Odd Numbers in a Range

# define the function
def odd_numbers(numbers):
    
    # define the range using a for loop
    for num in range(numbers):
        
        # checking if the number is odd
        if num % 2 != 0:
          print(num)
odd_numbers(
    int(input("Enter a number:"))
)

#   solution without function
for num in range(0,20):
    if num % 2 != 0:
        print(num)