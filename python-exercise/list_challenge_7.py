"""_
Ask the user to enter the names of everyone attending a party
Then return a list of the party guests in alphabetical order
This will require pulling together everything we have learned so far, so let’s walk through the thought process of idea to code

"""

# creating an empty list that will append the value the user will enter as names
lst = []
# initialing the variable name to an empty string
names = " "
# using a while loop since we don't known the number of people who attended the party
while names.capitalize() != "Done":
    # prompting the user to enter the names
    names = str(input("Enter the names of everyone attending a party: "))
    lst.append(names)  # appending the names in the empty list

# sorting the entire names in ascending order
lst.sort()
# using the for loop to loop through the list
for n in lst:
    print(n)




