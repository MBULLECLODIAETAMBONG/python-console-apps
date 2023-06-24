# Python Program to Check Whether a Number is Positive or Negative

# define the function
def check_number(number):
    
    # using while loop to check if number is different from zero
    while (number != 0):
        
        # using the if else statement to verify a positive and a negative number
        if number >= 1:
            return "The Number is Positive"
        else:
            return "The Number is Negative"
        
# Function call ie calling the function
result = check_number(
    int(input("Enter a number: "))
)
print(result)