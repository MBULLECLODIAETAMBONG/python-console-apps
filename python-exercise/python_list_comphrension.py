# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.


# write a program that checks if letter "a" in the list of words

fruits = ["Banana", "Apple", "Plum", "Orange", "Pear", "Mangoes", "Lemon", "Coconut", "Pineapple", "Limes", "Pawpaw"]

for i in fruits:
    if "a" in i:
        print(i)

# returning the output in a list
result = []
for i in fruits:
    if "a" in i:
        result.append(i)
print(result)

# Using LIST COMPREHENSION TO WRITE THE ABOVE PROGRAM


print("This is list comprehension; the shorter syntax for creating a new list")

fruits = ["Banana", "Apple", "Plum", "Orange", "Pear", "Mangoes", "Lemon", "Coconut", "Pineapple", "Limes", "Pawpaw"]

new_list = [i for i in fruits if "a" in i ]
print(new_list)

# writing the above program as a function
print("This is a function")

# defining the function
def checking_letter(x):
    
    new_list2 = []  # assigning an empty list
    
    # using a for loop to loop through the list
    for i in x:
        if "a" in i:
            new_list2.append(i)
    return new_list2

# function call that is calling the function 
p= checking_letter(
    ["Banana", "Pear", "Plum"]
)
print(p)