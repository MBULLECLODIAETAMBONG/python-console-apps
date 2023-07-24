#  A  Set is a collection of unordered and unindexed elements of different data types with no duplicate members

# create a set
fruits_set = {"Apple", "Orange", "Coconut", "Plum"}
print(fruits_set)

# getting the index of element in the set generates a typeerror because set is unordered ie no indexing or slicing
# print(fruits_set[2]    generates a typeerror because set is unordered ie no indexing or slicing

# add() method
fruits_set.add('Mangoes')
print(fruits_set)

# remove() method
fruits_set.remove("Apple")
print(fruits_set)

# No duplicate of members or elements
fruits_set.add("Orange")
print(fruits_set)

# A set can take any data types being int, float, string ...
fruits_set.add("4")
print(fruits_set)

# checking if something is in a set
print("Apple" in fruits_set)

print(len(fruits_set))

# clear() method
fruits_set.clear()
print(fruits_set)

# del() method
del fruits_set

