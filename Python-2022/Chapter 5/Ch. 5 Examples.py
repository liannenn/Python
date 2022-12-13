my_value = 10 #global variable
CONTRIBUTION_RATE = 0.05
DISCOUNT_PERCENT = 0.20
import random
import math

def message():
    
    print("I am Iron Man.") # prints "I am Iron Man."
    
    # -------------------------------------------------------------------- #
    
def main_5_2():
    
    print("I am inevitable.") # prints "I am inevitable."
    message() # prints message()
    print("Only one way to win...") # prints "Only one way to win ..."
    
    # ____________________________________________________________________ #
    
def acme_dryer(): # Program 5-3
    
    step1_ = 1
    step2_ = 2
    step3_ = 3
    step4_ = 4
    step5_ = 5
    goodbye_ = 0
    
    # acme dryer accepts no arguments
    # it prompts the user for an assempty step, validating 1-5
    
    print("Welcome to Acme Dryer disassembly.")
    step = int(input("Enter step # or 0 to exit: "))
    
    while step < 0 or step > 5:
        
        step = int(input("Enter step # or 0 to exit: "))    
    
    if step == step1_:
        step1()
        
    elif step == step2_:
        step2()
        
    elif step == step3_:
        step3()
    
    elif step == step4_:
        step4()
        
    elif step == step5_:
        step5()
    
    elif step == goodbye_:
        goodbye()
    
    
    # -------------------------------------------------------------------- #
    
def step1():
    
    print("Unplug the dryer and and move it away from the wall.")
    ans = input("Type 'yes' when done: ")
    if ans == 'yes':
        acme_dryer()
        
    # -------------------------------------------------------------------- #
        
def step2():
    
    print("Remove the six screws from the back of the dryer.")
    ans = input("Type 'yes' when done: ")
    if ans == 'yes':
        acme_dryer()
        
    # -------------------------------------------------------------------- #
        
def step3():
    
    print("Remove the back panel.")
    ans = input("Type 'yes' when done: ")
    if ans == 'yes':
        acme_dryer()
        
    # -------------------------------------------------------------------- #
    
def step4():
    
    print("Pull the top of the dryer straight up.")
    ans = input("Type 'yes' when done: ")
    if ans == 'yes':
        acme_dryer()
        
    # -------------------------------------------------------------------- #
    
def step5():
    
    print("Pull the front of the dryer off.")
    ans = input("Type 'yes' when done: ")
    if ans == 'yes':
        acme_dryer()
    
    # -------------------------------------------------------------------- #
        
def goodbye():
    
    print("Have a good day!")
    
    # ____________________________________________________________________ #
    
def bad_scope(): # Program 5-4
    #bad scope accepts no arguments
    #it calls procedure get_name() to get someone's name
    #then outputs a message using that name
    #NOTE: The scope of the variable "name" in get+name will not
    #allow this function to access that variable
    
    get_name()
    
    # -------------------------------------------------------------------- #
    
def get_name():
    
    name = input("Enter your name: ")
    print("Hello", name)
    
    # ____________________________________________________________________ #
    
def bird_calculator(): # Program 5-5
    
    texas()
    kansas()
    
    # -------------------------------------------------------------------- #
    
def texas():
    
    birds = 5000
    print("Texas has", birds, "birds.")
    
    # -------------------------------------------------------------------- #
    
def kansas():
    birds = 8000
    print("Kansas has", birds, "birds.")
    
    # ____________________________________________________________________ #
    
def pass_arg(): #Program 5-6
    #pass args accepts no arguments
    #it assigns value = 5
    # it calls show_double, passing value
    
    value = 5
    show_double(value)
    
    # -------------------------------------------------------------------- #
    
def show_double(number):
    #shows double accepts a value for number
    #it calculates that number *2 and prints the result
    
    result = number*2
    print(number, "* 2 =", result)
    
    # ____________________________________________________________________ #
    
def volume_conversion(): #Program 5-7
    intro() # PRINT INTRO
    cups_to_ounces() # PRINT CUPS_TO_OUNCHES
    
    
    # -------------------------------------------------------------------- #
    
def intro(): # def intro
    print("Welcome to the cups to fluid ounces conversion program.")
    print("For your reference, 1 cup = 8 fluid ounces.")
    
    # -------------------------------------------------------------------- #
    
def cups_to_ounces(): # def cups_to_ounces
    
    cups = int(input("Please enter the number of cups to convert to ounces: "))
    ounces =cups*8 # calc for ounches
    print(cups, "cup(s) is equal to", ounces, "fluid ounces.")
    # print the amt of cups being converted as well as the amt of ounces
    
    # ____________________________________________________________________ #

def show_sum(): # Program 5-8
    #show sum accepts no arguments
    #it outputs a message "The sum of 12 and 45 is"
    #it calls sum_of_numbers(num1, num2) passing the values 12 and 45
    
    print("The sum of 12 and 45 is", end='')
    
    sum_of_numbers(12, 45)
    
    # -------------------------------------------------------------------- #
    
def sum_of_numbers(num1, num2):
    
    total = num1 + num2
    print("", total)
    
    # ____________________________________________________________________ #
    
def get_name2(): # Program 5-9
    #get name accepts no arguments
    #it prompts the user for their first then last name
    #it calls reverse_name(first,last) passing values
    #for first and last
    
    first = input("Insert your first name: ")
    last = input("Insert your last name: ")
    reverse_name(first, last)

    # -------------------------------------------------------------------- #

def reverse_name(first, last):
    #reverse name accepts strings for first and last
    #it outputs the names in reverse order: last, first
    
    
    print(last, first)
    
    # ____________________________________________________________________ #
    
def get_value(): # Program 5-10
    #get value accepts no arguments
    #it assigns value = 99 and outputs the value
    #it passes value to change_me
    #it outputs a message showing the value of value in this function
    
    value = 99
    print("I just assigned the variable value: ", value)
    
    # -------------------------------------------------------------------- #
    
def change_me(value):
    #change me accepts an interger for value
    #it resassigns the value to 0
    #and outputs a message with the new value in this function
    
    value = 0
    
    #output the value in this function
    print("The value in the function change_me has been change to: ", value)
    
    # ____________________________________________________________________ #
    
def set_args(): # Program 5-11
    #set args accepts no arguments
    #it calls show_interest passing principal, rate, and periods as keywords
    show_interest(rate=0.01, periods=10, principal=10000.0)
    
    # -------------------------------------------------------------------- #

def show_interest(rate, periods, principal):
    #show interest accepts arguments for rate, periods, and principal
    #it calculates interest = principal*rate*periods
    #and outputs the result.
    
    interest = principal * rate * periods
    print("The simple interest will be $", format(interest, ',.2f'), sep='')
    
    # ____________________________________________________________________ #
    

def show_value(): # Program 5-13
    #show value recieves no arguments
    #it prints the value of global my_value
    global my_value
    
    my_value+=1
    
    print("The value of the gloval variable my_value is", my_value)
    
    # ____________________________________________________________________ #
    
def change_global(): #Program 5-14
    #change_global accepts no arguments
    #it changes the value of the gloval variable number
    #then calls global_variables_are_bad to print the variable
    
    global number
    number = int(input("What do you want to change the gloval to? "))
    global_variables_are_bad()
    
    # -------------------------------------------------------------------- #
    
def global_variables_are_bad():
    #global variables are bad accepts no arguments
    #it prints the value of the global variable number
    
    print("The value of the global variable number was changed in ", end='')
    print("change_global to the value of: ", number)
    
    # ____________________________________________________________________ #
    
def pay_me(): #Program 5-15
    #pay me accepts no arguments
    #it prompts the user for the gross pay and amount of bonuses
    #it calls show_pay, passing gross
    #and show_bonus, passing bonus
    bonus = float(input("Insert bonus pay: ", show_bonus(bonus)))
    gross = float(input("Insert gross pay: ",show_pay(gross)))
    
    show_pay(gross)
    show_bonus(bonus)
    
    # -------------------------------------------------------------------- #
    
def show_pay(gross):
    #show pay accepts a float for gross
    #it calculates the contribution = gross * the global constant
    #it outputs the contribution for gross pay
    
    contribution = gross * CONTRIBUTION_RATE
    print("Contribution for gross pay: ", contribution)
    
    
    # -------------------------------------------------------------------- #
    
def show_bonus(bonus):
    #show_bonus accepts a float for bonus
    #it calculates the contribution = bonus * the global constant
    #it outputs the cont for bonuses
    
    contribution = bonus * CONTRIBUTION_RATE
    
    print("Contribution for bonuses: ", contribution)
    
    # ____________________________________________________________________ #
    
def random_numbers(): #Program 5-16
    
    #random_numbers accepts no arguments
    #it generates a random intefer from 1-10
    #output the number to the user
    
    random1 = random.randint(1, 10)
    
    print("The random number is: ", random1)
    
    # ____________________________________________________________________ #
    
def random_numbers2(): #Program 5-18
    #random numbers 2 accepts no arguments
    #it loops 5 times outputting a new random integer for each iteration
    
    #loop 5 times
    
    for count in range(5):
        print(random.randint(1, 100))
        
    # ____________________________________________________________________ #
    
def dice():
    #dice accepts no arguments
    #it loops until the user enters "n" or "N" to stop
    #each iteration prints two random 6-sided die rolls
    #it prompts the user to roll again (/n)
    
    #randomize roll for 2 dice
    roll_1 = random.randint(1, 6) 
    roll_2 = random.randint(1, 6)
    
    #loop the dice
    while ans == "y" or ans == "Y": 
    
        print("Your rolls are:", roll_1, "and", roll_2)
        
        #prompt the user for another roll
        ans = print("Try your luck again? (y/n) : ")
        print()
        
    # ____________________________________________________________________ #
    
def coin_toss(): # Program 5-20
    #coin toss accepts no arguments
    #it sets three named constants for heads, tails, and tosses
    #it loops for 10 tosses using a random integer from 1 or 2 to determine
    #if the coin flip resulted in heads or tails, respectively
    tosses = 10
    heads = 1
    tails = 2
    
    for toss in range(tosses):
    
        flip = random.randint(1, 2)
    
        if flip == heads:
            print("Heads")
        if flip == tails:
            print("Tails")

    # ____________________________________________________________________ #
    
def total_ages(): #Program 5-21
    #def total ages accepts no arguments
    #it prompts the user for two ages and passes those values to calculate_ages()
    
    #get input from the user
    age1 = int(input("Please enter your age: "))
    age2 = int(input("Please enter the age of your best friend: "))
    
    #call calculate ages, passing age1 and age2 and assign the return value to total
    total = calculate_ages(age1, age2)
    
    #output the result
    print("\nTogether you are", total, "years old.")
    
     # -------------------------------------------------------------------- #
    
def calculate_ages(age1, age2):
    #calculate ages receives values for age1 and age2
    #it adds the two ages together
    #and returns the result
    
    #calculate the total age
    total_ages = age1 + age2
    
    #return the value 
    return total_ages

     # ____________________________________________________________________ #
     
def sale_price(): #Program 5-22
    #sale price accepts no arguments
    #it calls get regular price to get input from the user
    #calculates the sale price by taking the repair price and subtracting the
    #return result of discount
    #it outputs the sale price
    
    reg_price = get_regular_price()
    
    sale = reg_price - discount(reg_price)
    
    # -------------------------------------------------------------------- #
    
def get_regular_price():
    #get regular price accepts no arguments
    #it promopts the user to input the item's regular price
    #and returns that value

    price = ("Please enter the regular price of the item: ")
    return price
    
    # -------------------------------------------------------------------- #
    
def discount(price):
    #discount accepts an argument for the float price
    #it returns the discount price @ 20% off using
    #the global constant DISCOUNT_PERCENT
    
    return price * DISCOUNT_PERCENT

    # ____________________________________________________________________ #
    
def commission_rate(): #Program 5-23
    #comission rate accepts no arguments
    #it calls get_sales and get_advanced_pay
    #it calls deterine_comm_rate passing sales
    #it calculates the pay and outputs the pay
    #it determines if the pay is negative and outputs if the salesperson
    #the sale amount the salesperson must reimburse the company for
    
    
    #import the sales, advanced pay, and commission rate
    sales = get_sales()
    advanced = get_advanced_pay()
    com_rate = determine_com_rate(sales)
    
    #calculate the pay
    pay = ((sales * com_rate) - advanced + sales)
    pay = format(pay, ',.2f')
    
    print("\nThe total pay with commission is ", pay)
    
    # -------------------------------------------------------------------- #
    
def get_sales():
    #get sales accepts no arguments
    #it prompts the user to input the total monthly sales
    #and returns the monthly sales
    
    #prompt the user and input monthly sales
    sales = float(input("Please enter the amount of sales for the month: "))
    return sales
    
    # -------------------------------------------------------------------- #
    
def get_advanced_pay():
    #get advanced pay accepts no arguments
    #it prompts the user to enter any advanced pay, or 0 for none
    #it returns the advanced pay
    
    #prompt the user and input advanced pay
    advanced_pay = float(input("Please enter any advanced pay you received (0 for none): "))
    
    # -------------------------------------------------------------------- #
    
def determine_com_rate(sales):
    #determine comm rate accepts a float for sales
    #it calculates the commission rate for sales
    #and returns the calculate rate
    
    #define all the numbers
    n1 = 10000
    n2 = 10000
    n3 = 14999
    n4 = 15000
    n5 = 17999
    n6 = 18000
    n7 = 21999
    
    if sales > n1():
        rate = 0.10
        
    if sales >= n2 and sales <= n3():
        rate = 0.12
        
    if sales >= n4 and sales <= n5():
        rate = 0.14
        
    if sales >= n6 and sales <= n7():
        rate = 0.16
        
    else:
        rate = 0.16
        
    # ____________________________________________________________________ #
    
def get_name(): #string return example
    #get name accepts no arguments
    #it prompts the user for a name
    #and returns the name as a string
    
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    get_name = first_name, last_name
    
    return get_name

    # ____________________________________________________________________ #

def get_num():
    
    num = input("Please enter the number: ")
    return num
    validate_even(num)


    # -------------------------------------------------------------------- #
    
def validate_even(num): #boolean return example
    #validate even accepts an intefer for num
    #it tests if nuk is even and returns true
    
    if (num % 2) == 0:
        return True
    else:
        return False
    
    # ____________________________________________________________________ #

def square_root(): # Program 5-24
    import math
    x = int(input("Please enter a value to find the square root: "))
    squareroot = math.sqrt(x)
    print("The square root of", x, "is:", squareroot)
    
    
    # ____________________________________________________________________ #
    
def hypotenuse(): # Program 5-25
    sideA = int(input("Please enter the value of side A: "))
    sideB = int(input("Please enter the value of side B: "))
    
    hypot = math.hypot(sideA, sideB)
    
    print("The length of the hypoteneuse is: ", hypot)
    
    # ____________________________________________________________________ #
    
def area(radius):
    #area accepts an integer for radius
    #it calculates and returns the area of a circle
    return math.pi * radius **2

    # -------------------------------------------------------------------- #

def circumference(radius):
    #circumference accepts an argument for radius
    #it calculates and returns the radius of a circle
    
    return 2* math.pi * radius

    # -------------------------------------------------------------------- #
    
def area(width, length):
    #area accepts integers for width and length
    #it calculates and returns the area of a rectangle
    
    return width * length

    # -------------------------------------------------------------------- #
    
def perimeter(width, length):
    #perimeter accepts integers for width and length
    #it calculates and returns the perimeter of a rectangle
     
    return (width * 2) + (length *2)
