# BREAK STATEMENT: when the condition is satisfy, it terminates the remaining or entire process of a loop
# CONTINUE STATEMENT: terminates only the current iteration of the loop and moves to the preceding iterations

# examples: write a program that prints the first three  character of a word that has been input by a user

#  using the CONTINUE statement
#name  = str(input("Enter any word of your choice: "))
name  = ["mbulle", "sandra", "vivian", "Epolle"]
for x in name:
    if x=="sandra":      
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

