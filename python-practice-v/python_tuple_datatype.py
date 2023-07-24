# Tuple: is a collection of ordered (indexing) elements of different data type that are immutable
number = (1,4,"cunny", 8, "fruits")
print(number)

for n in number:
    if number.index(n) %2 ==0:
        print(n,": is Even")
    else:
        print(n, ": is Odd")
        
# number[2]="cyan" can't be change(immutable)
        

# using function to write the same code

def tuple_element(a,c,d,y,i):
    
    for n in tuple_element:
        if tuple_element.index(n) %2 ==0:
            print(n,": is Even")
        else:
            print(n, ": is Odd")
tuple_element(1,4,"cyan", 8, "fruits")  