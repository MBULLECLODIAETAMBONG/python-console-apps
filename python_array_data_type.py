#  ARRAYS: It is a collection of elements of the same data type and is mutable(changeable)

# we have to import array module before it is used

# NOTE: We either import array and use the "array.array()" method or we import array from array and use just "array()" method

print("using the array.array() method")
import array
numbers = array.array('i',[1,2,3,4,5,6,7,8,9])
print(numbers)

print("Using the array() method after using the 'from array import array'")
from array import array
numbers = array('i',[1,2,3,4,5,6,7,8,9])
print(numbers)

#  Array slicing
print(numbers[:3])
print(numbers[::2])  # slice from start to end while skipping every second element
print(numbers[3::2])  # slice from index 3 to end while skipping every second element

# inserting into arrays
insert_number = numbers.insert(4, 55)
print(numbers)

# using the append() method to add elements in an array
append_element = numbers.append(100)
print(numbers)

# using the remove() method or pop() method to remove elements in an array
remove_element = numbers.remove(1)
print(numbers)

# It deletes an element from an array by using it’s index, and if no index is provided, it removes the last element of the array
pop_element = numbers.pop(4)
print(numbers)

# using the reverse() method to reverse elements in an array
reverse_element = numbers.reverse()
print(numbers)

# using the len() method to get the size of an array
print("The length of the array call numbers is: ", len(numbers))

# using the extend() method to extent the elements in an array
extent_element = numbers.extend((0, -1, -2, -3, -4, -5))
print(numbers)

# using the index() method to find an index of an element in an array 
print("The index of 55 in the array is: ", numbers.index(55))

# count() method takes in an element as an argument and counts the occurrence of an element in the array.
occurrence = array('i',[1, 2, 30, 4, 5, 6, 30, 8, 30])
print("30 occurs: ", occurrence.count(30),"times")

# checking if an element in an array is odd or even
num1 = int(input('Enter first number on the list: '))
num2 = int(input('Enter second number on the list: '))
num3 = int(input('Enter third number on the list: '))
total_numbers = array('i', [num1, num2, num3])
print(total_numbers)

if (total_numbers[1] %2 ==0):
    print("The number is EVEN")
    
else:
    print("The number is ODD")

