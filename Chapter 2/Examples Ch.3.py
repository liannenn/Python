def demo_prog():

    value = int(input('Enter a value: '))
    mystery_number = 393

    #see if the value is == the mystery number
    if value == mystery_number:
        print("The values match")
    print('Have a nice day')
    
def demo_prog2():
    truth = bool(input('True or False: '))
    flag_var = True
    flag_var = False
    #see if the value is == the mystery number
    if flag_var:
        print('True!')
    else:
        print('False!')
        
def test_average():
    test_amt1 = float(input('Enter the first test score: ')) # Get first test score
    test_amt2 = float(input('Enter the second test score: ')) # Get second test score
    test_amt3 = float(input('Enter the third test score: ')) # Get third test score
    
    highscore = 95
    
    avg_score = (test_amt1 + test_amt2 + test_amt3)/3
    
    print('The average score is:', avg_score)
    
    if avg_score >= highscore:
        print("Congratulations!")
        print("That is a high score!")

def auto_repair_payroll():
    hours_worked = float(input('Enter amount of hours worked: ')) # Get amt of hours worked
    hourly_pay_rate = float(input('Enter hourly payrate: ')) # Get hourly pay rate
    
    necc_gross_hours = 40 #Amt of hours at least for gross pay
    cash_earned = (hours_worked * hourly_pay_rate) #Calc cash earned
    
    if hours_worked >= necc_gross_hours: #Decide whether or not to calc gross pay
        extra_hours= (necc_gross_hours - hours_worked) #Figure out how many extra hours if enough for gross pay
        gross_pay = (extra_hours * 1.5) #Calc amount of money
        total = (gross_pay + cash_earned) #Get total along with gross pay 
        print('$', total) #Print the total with gross pay
    else:
        print('$', cash_earned) #Print the total without gross pay
        
def even_number():
    #even number accepts no arguments
    #it takes inputs from the user
    #nd returns if the number was even
    
    number = int(input("Please enter an even number: "))
    
    #use modulus to determine if the number was even or odd
    
    if number %2 ==0:
        print("The number is even!")
        #you could then perform the calculation
    else:
        print("I said to enter an even number!")
        #do not perform the calculation
        
def password_verifier():
    
    password = input('Please enter the password: ') 
    
    if password == "prospero":
        print('Password accepted.')
    else:
        print('Password is invalid')
        
def sort_names(): 
    first_name = input('Enter the first name (last, first): ') #Gets first name
    second_name = input('Enter the second name (last, first): ') #Gets second name
    if first_name>=second_name:
        print("Here are the names, sorted alphabetically")
        print(first_name)
        print(second_name)
    else:
        print("Here are the names, sorted alphabetically")
        print(second_name)
        print(first_name)
        
def range_of_numbers():
    #range of numbers accepts no arguments
    #it will rompt th user for a number from 1 to 10
    #and output if the number is <>5
    #and output if the number is out of range
    
    #Get input from the user
    number = input("Enter a number from 1 to 10: ")
    
    #Check if the number is greater than 10
    if number > 10:
        print("Only enter numbers between 1 and 10")
    elif number <= 5:
        print("Your number was between 1 and 5")
    else:
        print("Your number was between 6 and 10")
        
def loan_qualifier():
    annual_salary = int(input("Enter your annual salary: "))
    years_at_job = int(input("Enter the number of years at your current job: "))
    if annual_salary >= 30000:
        print("Your salary qualifies.")
        if years_at_job >= 2:
            print("You qualify for the loan")
        else:
            print("You must have been on your current job for at least 2 years to qualify.")
    else:
        print("You must earn at least $30,000 per year to qualify.")