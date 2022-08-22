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
    print(format("Your state tax amount is:\t$\t", state_tax,'10.2f'))#Print state tax amt
    print(format("Your county tax amount is:\t$\t", county_tax,'10.2f'))  #Print county tax amt
    print(format("Your total tax is:\t\t$\t", total_tax,'10.2f'))  #Print total tax amt
    print(format("Your total sale is:\t\t$\t", total_sale,'10.2f'))  #Print total sale amt
    
def tip_tax_total():
    sale_amt = float(input("Please enter the sale amount: "))
    print("The sale was:\t\t\t$", sale_amt)
    tip_amt = (sale_amt*0.18)
    print("The tip amount is:\t\t$") print(format(tip_amt, '7.2f'))
    sales_tax2 = (sale_amt*0.07)
    print("The sales tax amount is: \t$", sales_tax2)
    total_bill = (tip_amt + sale_amt + sales_tax2)
    print("The total bill is: \t\t$", total_bill)
    
    