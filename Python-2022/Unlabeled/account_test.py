#Program 10-8
#import the bankaccount module
import bankaccount

def main(): #Program 10-8
#main accepts no arguments
#it takes input from the user for a starting balance
#it uses the BankAccount class in bankaccount.py to create
#an object savings, passing the starting balance
#it takes input from the user for a paycheck
#it uses for deposit() method to deposit a paycheck
#ot dosplaus the current balance using the get_balance() method
#it takes input from the user for a withdrawal and uses the width() method
#and outputs the final balance
    
    start_bal = input("Enter your starting balance: ")
    
    savings = bankaccount.BankAccount(start_bal)
    
    pay = input("Enter the amount of your paycheck deposit: ")
    savings.deposit(pay)
    print("Deposit successful\n")
    
    print(savings)
    
    cash = input("How much would you like to withdraw: ")
    
    while not withd:
        
        try:
            cash = float(cash)
            withd = True
        except:
            cash = input("Enter a valid amount to withdraw: ")
            print(savings)
                
    main()
    
        
        
    