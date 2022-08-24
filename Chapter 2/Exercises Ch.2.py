def personal_info():
    print("Jullian Tran") #print name
    print("13812, Wichita, KS, 67235") #print address
    print("316-993-1411") #print phone number
    print("IT") #print career
    
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
    mph1 = (speed*6) #calc speed per 6 hours
    mph2 = (speed*10) #calc speed per 10 hours
    mph3 = (speed*15) #calc speed per 15 hours
    print('At', speed, "miles per hour you will travel", mph1," miles in 6 hours.")  #Print mph1
    print('At', speed, "miles per hour you will travel", mph2," miles in 10 hours.")  #Print mph2
    print('At', speed, "miles per hour you will travel", mph3," miles in 15 hours.")  #Print mph3
    
def sales_tax():
    sale_amt = float(input('Please enter the sale amount: ')) #Get sale amt + print it
    purchase_price = float(input('Your purchase price was:        $        ')) #Get sale amt + print it
    state_tax = (purchase_price * 0.05) #calc state tax
    county_tax = (purchase_price * 0.025) #calc county tax
    total_tax = (state_tax + county_tax)#calc total tax
    total_sale = (total_tax+sale_amt) #calc the total sale
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
    print("For", amt_of_cookies,"cookies you will need:") #get amt of cookies
    
    
    orig_sugar=1.5
    orig_butter= 1
    orig_flour= 2.75

    sugar_cups = (amt_of_cookies * .5)//8 #Calc sugar cups

    sugar_oz = (amt_of_cookies * .5)%8 #Calc sugar oz
    
    sugar_oz = format(sugar_oz, '.2f') #Format sugar oz

    butter_cups = (amt_of_cookies * .3333)//8 #Calc butter cups

    butter_oz = (amt_of_cookies * .3333)%8 #Calc butter oz
    
    butter_oz = format(butter_oz, '.2f') #Format butter oz

    flour_cups = (amt_of_cookies * .9166)//8 #Calc flour cups

    flour_oz = (amt_of_cookies * .9166)%8 #Calc flour oz
    
    flour_oz = format(flour_oz, '.2f') #Format flour oz

    print(sugar_cups, "cup(s) ", sugar_oz, "ounces of sugar.") #Print amt of sugar cups and remaining ounces
    print(butter_cups, "cup(s) ", butter_oz, "ounces of butter.") #Print amt of butter cups and remaining ounces
    print(flour_cups, "cup(s) ", flour_oz, "ounces of flour.") #Print amt of flour cups and remaining ounces
    
def class_demopraphics():
    amt_of_females= float(input("Enter the number of females:")) #Get amt of females
    amt_of_males= float(input("Enter the number of males:")) #Get amt of males
    
    total_ppl= amt_of_females + amt_of_males #Gather total people
    
    female_perc= (amt_of_females/total_ppl) #Calc female amt
    male_perc= (amt_of_males/total_ppl) #Calc male amt
    
    females = (female_perc*100) #Multiply to get percent
    males = (male_perc*100) #Multiply to get percent
    
    femaless =format(females, '.2f') # Format 
    maless =format(males, '.2f') # Format
    
    print("The class consists of ", femaless ,"% females and", maless , "% males.") # Print the amount
    
def  tortuga_1():
    import turtle
    
    
def  tortuga_2():
    import turtle
    
    
    