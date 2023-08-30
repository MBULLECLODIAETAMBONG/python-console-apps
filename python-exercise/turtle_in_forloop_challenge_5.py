"""
    Get turtle to draw an octagon 
Hint: to calculate the angle, you take 360 degrees and divide it by the number of sides of the shape you are drawing
Extra challenge: Let the user specify how many sides the object will have and draw whatever they ask
Double bonus challenge, add a nested loop to draw a smaller version of the object inside

"""

# first we import turtle bc its a module
import turtle

# An octagon has 8 sided shape, so we use a for loop

# using forward and right for octagon
for shape in range(8):
    turtle.forward(100)
    turtle.right(360/8) 
    # since the shapes are like circles because the need to close at the end, thus all complete 
    # shapes under goe 360 degree so to get the appropriate shape, we dived the 360 by the number of sides the shape has.
    
#  Note: In Turtle, forward goes with right while backward goes with left. Formula for all shapes = (360/number of sides of shape)

# using backward and left for octagon
print("OCTAGON SHAPE")
for shape in range(8):
    turtle.backward(100)
    turtle.left(360/8) 
    turtle.color('purple')
    turtle.shapesize(10) # size of the turtle
    
# for rectangle shape (360/4)
print("RECTANGLE SHAPE")
for shape in range(4):
    turtle.forward(100)
    turtle.left(360/4)
    
    
# for triangle shape (360/3
print("TRIANGLE SHAPE")
for shape in range(4):
    turtle.forward(100)
    turtle.left(360/3)


#     EXTRA CHALLENGE
print("EXTRA CHALLENGE")

# prompting the user to enter the number of sides for the shape they want
user = int(input("Enter the number of side for your shape: "))
for side in range (user):
    turtle.forward(100)
    turtle.right(360/user)
    for inner_side in range(user):
        turtle.forward(50)
        turtle.right(360/user)