# Write a program in python to determine if a number is leap year or not

# function definition
def leap_year(year):
    
    # A leap year is a year divisible by 4
    if year % 4 == 0:
        print(year, "is a leap year")

    else:
        print(year, "is not a leap year")
        
leap_year(int(input("Enter a number: ")))
