# write a program that checks if letter "a" in the list of words

word = ["Banana", "Apple", "Plum", "Orange", "Pear", "Mangoes", "Lemon", "Coconut", "Pineapple", "Limes", "Pawpaw"]

for i in word:
    if "a" in i:
        print(i)

# returning the output in a list
result = []
for i in word:
    if "a" in i:
        result.append(i)
print(result)

