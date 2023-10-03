import turtle

turtle.color("purple")
turtle.circle(360)

# using range to draw in python 

for steps in range(4): 
	turtle.forward(100) 
	turtle.right(90)
	turtle.backward(90)
 

for steps in range(6): 
    turtle.forward(100) 
    turtle.right(360/6)
    for more_steps in range(6): 
        turtle.forward(10) 
        turtle.right(360/6)


for steps in range(5):	
			turtle.forward(100)
			turtle.right(90)
			for moresteps in range(4):
				turtle.forward(50)
				turtle.right(90)



