# Newton’s Second Law of motion is expressed in the formula F = m × a where F is force,
# m is mass, and a is acceleration. Assume that the user knows the mass of an object and the
# force on that object but wants to obtain the object’s acceleration a. Write a program that
# prompts the user to enter the mass in kilograms (kg) and the force in Newtons (N). The user
# should enter both values on the same line separated by a comma. Calculate the acceleration
# using the above formula and display the result to the user.

mass = int(input("Enter the mass in kg:  and enter the force in Newtons: ")) #.split(",")
Force = int(input("Enter the force in Newtons: "))
# From newton's Second Law of Motion " Force = mass * acceleration "
acceleration = Force / mass
print("The acceleration is: ", acceleration)

