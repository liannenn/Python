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
    
    necc_gross_hours = 40
    cash_earned = (hours_worked * hourly_pay_rate)
    
    if hours_worked >= necc_gross_hours:
        extra_hours= (necc_gross_hours - hours_worked)
        gross_pay = (extra_hours * 1.5)
        total = (gross_pay + cash_earned)
        print('$', total)
    else:
        print('$', cash_earned)