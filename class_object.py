#  instance variables

class Career(object):
    def __init__(self, name, occupation, age):
        self.name = name
        self.occupation = occupation
        self.age = age
      

#  When you create instances of the class Employees, each member will have access to the variables which were 
# initialized through the __init__ method.To illustrate, you can create or ‘instantiate’ new members of the class Employees:

person_1 = Career("CLODIA", "Engineer", 23)
person_2 = Career("SANDRA", "Accountant", 27)


#  print command to see how the instance variables interacted with members of the class Employees:
print(person_1.name, person_1.occupation, person_1.age)
print(person_2.name, person_2.occupation, person_2.age)
