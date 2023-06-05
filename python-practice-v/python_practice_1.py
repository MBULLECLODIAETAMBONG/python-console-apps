x, y = int(input("Enter a number for x : ")), int(input("Enter a number for y : "))
print("x is:", x, "y is:", y)
print("x is =", y, "and", "y is =", x)  


#  method 2: using a third variable or a temporary variable which is the better method      

print("method 2: using a third variable or a temporary variable which is the better method")
x, y = int(input("Enter a number for x : ")), int(input("Enter a number for y : "))
swap = x
x = y
y = swap

print(x, y)

                                                                                                                                    
                                                                                                                                    