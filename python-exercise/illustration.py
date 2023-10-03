# What would the following for loop print on the third time it loops?


for steps in range(1,10,2):
    print(steps)
    

print("This is another program of turtle using while loop")

import turtle
Counter = 0
while Counter <= 5:
    turtle.backward(50)
    turtle.right(360/5)
    print(Counter)
    Counter += 1