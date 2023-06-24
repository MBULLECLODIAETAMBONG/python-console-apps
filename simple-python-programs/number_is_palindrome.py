# Python Program to Check if a Number is a Palindrome

# A Palindrome is a number that remains the same when it is reversed that is a number that reads the same forwards and backwards


num=int(input("Enter number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")