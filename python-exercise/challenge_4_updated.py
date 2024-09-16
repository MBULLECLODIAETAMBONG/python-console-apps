"""
Calculate the total to charge for an order from an online store in Canada
Ask user what country they are from and their order total
If the user is from Canada, ask which province
If the order is from outside Canada do not charge any taxes
If the order was placed in Canada calculate tax based on the province
Alberta charge .05% General sales Tax (GST)
Ontario, New Brunswick, Nova Scotia charge .13% Harmonized sales tax
All other provinces charge .06% provincial sales tax + .05% GST tax
Tell the user the total with taxes for their order

"""
# prompting the user to enter their location
user_location = str(input("What's your location? : "))

# prompting the user to enter the price of products bought
price = int(input("enter the amount for what you've ordered: "))

# initializing the province
Alberta_charge = 5/100
Ontario = 13/100
New_Brunswick = 13/100
Nova_Scotia = 13/100
all_other_p = 11/100

# testing the condition
if user_location.capitalize() == "Canada":
    province = input("Which province are you from? : ")
    
    if province.capitalize() == "Alberta":
        total_price = Alberta_charge + price
        print("The total with taxes for for your order is ",total_price)
        
    elif province.capitalize() == "Ontario" or "New Brunswick" or "Nova_Scotia":
        total_price = Ontario + price or  New_Brunswick + price or Nova_Scotia + price
        print("The total with taxes for for your order is ",total_price)
        
    # elif province.capitalize() == "New Brunswick":
    #     total_price = New_Brunswick + price
    #     print("The total with taxes for for your order is ",total_price)
        
    # elif province.capitalize() ==  "Nova Scotia":
    #     total_price = Nova_Scotia + price
    #     print("The total with taxes for for your order is ",total_price)
        
    else:
        total_price = all_other_p + price
        print("The total with taxes for for your order is ",total_price)

    
else:
    print("The total with taxes for for your order is ",price)
    
