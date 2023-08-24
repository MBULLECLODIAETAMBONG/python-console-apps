# BREAK STATEMENT: when the condition is satisfy, it terminates the remaining or entire process of a loop
# CONTINUE STATEMENT: terminates only the current iteration of the loop and moves to the preceding iterations

# examples: write a program that prints the first three  character of a word that has been input by a user

#  using the CONTINUE statement
#name  = str(input("Enter any word of your choice: "))
name  = ["mbulle", "sandra", "vivian", "Epolle"]
for x in name:
    if x=="vivian":      
        break
    else:
        print(x)
print("its over")

#  using the CONTINUE statement
name  = ["mbulle", "sandra", "vivian", "Epolle"]
for x in name:
    if x=="sandra":
        
        continue
    else:
        print(x)
print("its over")

list = [1,2,3,4,5,6,7,8,9,10]
for l in list:
    if l %2 ==0:
        break
    else:
        print(l,": is odd")
        
        
"""
EXERCISE 2: Write a program in a while loop that checks if a number is
less than 7 and and if is equal to 4 using a break and continue statement
"""

# BREAK STATEMENT

i = 0
while i < 7:
    print(i)
    if i == 4:
        print("Breaking from loop")
        break
    i += 1

# BREAK STATEMENT

print("This is a continue  statement")

list = [0,1,2,3,4,5,6]
for i in list:
    if i == 2 or i== 6:
            continue
        
    print(i)
    

    