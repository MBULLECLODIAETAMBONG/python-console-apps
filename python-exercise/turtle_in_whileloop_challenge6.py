"""
Create an etch a sketch program
Have the user enter a pen color, a line length, and an angle
Use turtle to draw a line based on their specifications
Let them specify new lines over and over until they enter a line length of 0. 
When the user specifies a line length of 0 stop drawing.

"""
# first we import turtle
import turtle

# prompting the user to enter the color of the turtle they want
color = input("Enter the pen's color: ")

# prompting the user to enter the number of shape 
line_length = int(input("Enter the line length: "))
angle = int(input("Enter the angle off the shape you want: "))
counter = 0
while counter < 5:
    turtle.forward(line_length)
    turtle.right(angle)
    counter = + 1
    