#   WHILE LOOP
#   write a program that does multiplication time table

print("THIS IS WHILE LOOP")
iterator=1
ask=int(input("enter a number"))
while iterator<=10:
    print(ask,"*",iterator,"=",ask * iterator)
    iterator += 1
    

print("THIS IS FOR LOOP")
ask2 = int(input("Enter a number: "))
for count in range(1, 11):
    print(ask2,"*",count,"=",ask2 * count)
  
    
    
 
# PYTHON METHODS

#     The append()
fruits = ["Apple", "Mangoes", "Pawpaw", "Pineapple"]
fruits.append("Banana")
print(fruits)

#   The remove()
fruits.remove("Mangoes")
print(fruits)

#    The insert()
fruits.insert(2, "Coconut")
print(fruits)

#    INDEXING AND SLICING

#       indexing
new_fruits = fruits[3]
print(new_fruits)

#      slicing
print("THIS IS SLICING")
name = "Cenderella"
for i in name:
    print(i)
   
    
