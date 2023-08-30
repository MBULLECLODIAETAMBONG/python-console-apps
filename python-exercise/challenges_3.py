"""
Calculate shipping charges for a shopper
Ask the user to enter the amount for their total purchase
If their total is under $50 add $10, otherwise shipping is free
Tell the user their final total including shipping costs and format the number so it looks like a monetary value
Don’t forget to test your solution with 
a value > 50
a value < 50
a value of exactly 50

"""

# prompting the user to enter total amount_purchase
amount_purchase = int(input("What is the total amount purchased? : "))

# checking the condition of purchase amount
if  amount_purchase < 50:
    shipping_fee = amount_purchase + 10
    print("your final total including shipping fee cost is ", shipping_fee,"$")
else:
    shipping_fee = amount_purchase
    print("your final total including shipping fee cost is ", shipping_fee,"$")