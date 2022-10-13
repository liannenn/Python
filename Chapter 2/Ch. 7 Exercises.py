import random

def lottery():
    #lottery accepts no arguments
    #it prints Generating lotto numbers.
    #it saves the numbers and prints them
    
    lotto_numb1= random.randint(1,9)
    lotto_numb2= random.randint(1,9)
    lotto_numb3= random.randint(1,9)
    lotto_numb4= random.randint(1,9)
    lotto_numb5= random.randint(1,9)
    lotto_numb6= random.randint(1,9)
    lotto_numb7= random.randint(1,9)
    
    print("Generating lotto numbers. \n")
    

    print("Youre lotto numbers are:")
    print('\n', lotto_numb1, '\n', lotto_numb2, '\n', lotto_numb3, '\n',lotto_numb4,'\n', lotto_numb5,'\n', lotto_numb6,'\n', lotto_numb7)
    
def rainfall():
    #rainfall calculates the amount of rainfall within the month
    #it calculates the total rainfall, average, maximum, and minimum
    
    total = 0
    numbers = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']
    
    rainfall = []
    
    for num in numbers:
        print("Enter the rainfall for", num, end = '')
        value = int(input(": "))
        rainfall.append(value)
        
        total= total + value
        avg = total / 12
        
        
    maxrainfall = max(rainfall)
    minrainfall = min(rainfall)
    
    print("January had the least rain with", minrainfall, "inches.")
    print("December had the most rain with", maxrainfall, "inches.")
    print("Total rain for the year:", total," inches.")
    print("Average rain per month:", avg," inches.")
    
def charge_accts():
    #charge_accts accepts no arguments
    #it opens charge_accounts.txt
    
    content_list = []
    numb = []
    
    try:
        list = open('charge_accounts.txt', 'r')
        acc_numb = int(input("Enter an account number: "))
        content_list.append(list)
        numb.append(acc_numb)
        
        if numb in content_list:
            cont = input("\nThe account number is valid.\n\nCheck another account number? (y/n)")

            if cont == 'y' or 'Y':
                charge_accts()
            
        else:
            
            cont = input("\nThe number is invalid.\n\nCheck another account number? (y/n) ")
            if cont == 'y' or 'Y':
                charge_accts()
                
            
    except ValueError:
        cont = input("\nThe number is invalid, please only enter numbers.\n\nCheck another account number? (y/n) ")
        if cont == 'y' or 'Y':
            charge_accts()