# A Dictionary are mutable data structures that allows the storage of key value pairs. 

# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

# The key value-pairs are separated by a colon 

# creating a dictionary of person
person = {
    "first_name" : "Mbulle",
    "last_name" : "Etah",
    "age" : 23
}
print(person)

# using the constructor dict() to create a dictionary
person2 = dict(
    first_name = "sandra",
    last_name = "Kang",
    status = "single",
    age = 30
)
print(person2)

# getting the data type
print(type(person2))

# getting a value
print(person2["first_name"])

# getting a value using the get() method
print(person2.get("age"))

# adding value into the dictionary
person2["contact"] = 56798763456
print(person2)

# getting all the keys in a dictionary
print(person2.keys())

# getting all the values in a dictionary
print(person2.values())

# getting all the items in a dictionary
print(person2.items())

# copying a dictionary
person2 = person.copy()
person2["career"] = "Computer Engineer"
print(person2)

# removing items using del
del(person2["age"])
print(person2)

# removing items using pop()
person2.pop("first_name")
print(person2)

# get the length
print(len(person2))

# removing all items from a dictionary using clear())
person2.clear()
print(person2)

# list of dictionary
identity = [
    {"name" : "Mbulle", "age" : 22},
    
    {"name" : "Nadesh", "age" : 20},
    
]
print(identity)

# Accessing item from the list of dict
print(identity[1]["name"])

# Getting the item via indexing
print(identity[1])

