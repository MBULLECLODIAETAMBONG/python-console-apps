
my_l = [1,2,3,2,4,5,3,4,2]
print(my_l.count(2))

numbers = int(input("Enter a number")), int(input("Enter a number")), int(input("Enter a number"))
my_list = []
c_list = my_list.append(numbers)

for num in numbers:
    question = str(input("identify the number that occur more than once! "))
    if numbers.count(num) >= 2:
        result = num
    
        if question == num:
            print("Correct", num,"occurs more than once")
        else:
            print("Wrong, Try again", num, "occurs more than once")
    

