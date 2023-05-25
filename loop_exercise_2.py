# Write a program that takes a list of numbers and returns the sum of all the even numbers in the list.

# method 1: prints each even number and outputs the result immediately

numbers = [1,2,3,4,5,6,7,8,9,10]
# assigning sum to zero
sum = 0
for num in numbers:
    if(num %2 ==0):
# Sums each even number to sum 
        sum = sum + num
        print(sum)
  
        
        
print(" THIS IS METHOD 2") 
# method 2: takes a list of numbers and returns the sum of all the even numbers in the list.

numbers = [1,2,3,4,5,6,7,8,9,10]
# assigning sum to zero
sum=0
for num in numbers:
    if (num %2==0) :
# Sums each even number to sum 
        sum += num
print("The sum of all the even numbers in the list is: ", sum)


    