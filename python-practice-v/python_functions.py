""""
FUNCTION: A Function is a block of code that performs a specific task

FUNCTION SYNTAX:

Function name
function body / statement
function return

"""
def add(a,c):
    return a + c
result = add(
    int(input("Enter a number: ")), 
    int(input("Enter second number: "))
    )

print(result)


# DICTIONARY IN PYTHON
name = {"mbulle": 987654, "yia": 45324, "toya":406789}
for dic in name:
    print(dic, name[dic])
    print(dic)
