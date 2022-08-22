def personal_info():
    print("Jullian Tran")
    print("13812, Wichita, KS, 67235")
    print("316-993-1411")
    print("IT")
    
def total_purchase():
    item_1 = float(input('Please enter a price for your first item:')) #Get first item
    item_2 = float(input('Please enter a price for your second item:')) #Get second item
    item_3 = float(input('Please enter a price for your third item:')) #Get third item
    item_4 = float(input('Please enter a price for your fourth item:')) #Get fourth item
    item_5 = float(input('Please enter a price for your fifth item:')) #Get fifth item
    subtotal = (item_1 + item_2 + item_3 + item_4 + item_5)
    print('\nSubtotal:   $ ', subtotal) #Print subtotal
    tax = (subtotal * 0.07) #Gets tax total
    print('Tax:        $ ', tax)  #Print tax
    total = (subtotal + tax) #Gets total
    print('Total:      $ ', total)  #Print subtotal
    
def distance_traveled():
    speed = float(input('How fast are you driving?')) #Get speed
    mph1 = (speed*6)
    mph2 = (speed*10)
    mph3 = (speed*15)
    print('At', speed, "miles per hour you will travel", mph1," miles in 6 hours.")  #Print mph1
    print('At', speed, "miles per hour you will travel", mph2," miles in 10 hours.")  #Print mph2
    print('At', speed, "miles per hour you will travel", mph3," miles in 15 hours.")  #Print mph3
    
def sales_tax():
    sale_amt = float(input('Please enter the sale amount: ')) #Get sale amt + print it
    purchase_price = float(input('Your purchase price was:        $        ')) #Get sale amt + print it
    state_tax = (purchase_price * 0.05)
    county_tax = (purchase_price * 0.025)
    total_tax = (state_tax + county_tax)
    total_sale = (total_tax+sale_amt)
    print("Your state tax amount is:\t$\t", format(state_tax,'10.2f'))#Print state tax amt
    print("Your county tax amount is:\t$\t", format(county_tax,'10.2f'))  #Print county tax amt
    print("Your total tax is:\t\t$\t", format(total_tax,'10.2f'))  #Print total tax amt
    print("Your total sale is:\t\t$\t", format(total_sale,'10.2f'))  #Print total sale amt
    
def tip_tax_total():
    sale_amt = float(input("Please enter the sale amount: "))
    print("The sale was:\t\t\t$", sale_amt)
    tip_amt = (sale_amt*0.18)
    print("The tip amount is:\t\t$",tip_amt)
    sales_tax2 = (sale_amt*0.07)
    total_bill = (tip_amt+sale_amt+sales_tax2)
    sales_tax2 = format(sales_tax2, '.2f') # 
    print("The sales tax amount is: \t$", sales_tax2) # Print sales tax
    print("The total bill is: \t\t$", total_bill) # Print total bill
    
def temp_convertor():
    Celsius = float(input('Please enter the degrees in Celusis: ')) #Get temp in celsius
    F = 1.8 * float(Celsius) + 32
    print(Celsius, 'degrees celsuis is', F, 'degrees in fahrenheit.')
    
def cookie_monster():
    amt_of_cookies = float(input("How many cookies do you want to make? ")) #Amt of cookies 
    print("For", amt_of_cookies,"cookies you will need:") #
    converted_amt = (amt_of_cookies/24)
    sugar1 = (1.5*converted_amt)
    butter1 = (1* converted_amt)
    flour1 = (2.75* converted_amt)
    
    sugar2 = (.5* converted_amt)
    butter2 = (.3333*converted_amt)
    flour2 = (.9166*converted_amt)
    
    print(sugar1, "cup(s) ", sugar2, "ounces of sugar.")
    print(butter1, "cup(s) ", butter2, "ounces of butter.")
    print(flour1, "cup(s) ", flour2, "ounces of flour.")
    