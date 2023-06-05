name = str(input("Enter your name please: "))

#               PYTHON  METHODS

# for capitalization: upper()
print("for capitalization: upper()")
result = name.upper()
print(result)  #  output the uppercase of name


# for lowercase: lower()
print("for lowercase: lower()")
result = name.lower()
print(result)  #  output the uppercase of name

# for swap case: swapcase() 
print("for swap case: swapcase()")
result = name.swapcase()
print(result) 

# for length: len() 
print("for length: len() ")
result = len(name)
print(result)  

# for starts with: startwith()
print("for starts with: startswith() ")
result = name.startswith('m')
print(result)

# for ends with: endswith()
print("for start with: endswith() ")
result = name.endswith('e')
print(result)

# for split: endswith() which splits into a list
print("for split: endswith() which splits into a list ")
result = name.split()
print(result)

# for find: find()  which finds the position of a letter in a word
print("for find: find()  which finds the position of a letter in a word ")
result = name.find('l')
print(result)

# for alpha numeric: isalnum()  which returns True or False is word contains alphabet or numbers
print("for alpha numeric: isalnum()  which returns True or False is word contains letters or numbers ")
result = name.isalnum()
print(result)

# for alpha numeric: isalpha()  which returns True or False is word contains letters 
print("for alpha numeric: isalpha()  which returns True or False is word contains letters")
print(result)

# for alpha numeric: isnumeric)  which returns True or False is word contains numbers 
print("for alpha numeric: isnumeric()  which returns True or False is word contains numbers ")
result = name.isnumeric()
print(result)