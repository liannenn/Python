my_value = 10 #global variable

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
    
    # bad scope accepts no arguments
    # it calls procedure get_name() to get someone's name
    # then outputs a message using that name
    # NOTE: The scope of the variable "name" in get+name will not
    # allow this function to access that variable
    
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
    
    gross = int(input("Insert gross pay: "))
    bonus = int(input("Insert bonus pay: "))
    
    show_pay(gross)
    show_bonus(bonus)
    
    # -------------------------------------------------------------------- #
    
def show_pay(gross):
    #show pay accepts a float for gross
    #it calculates the contribution = gross * the global constant
    #it outputs the contribution for gross pay
    
    # -------------------------------------------------------------------- #
    
def show_bonus(bonus):
    #show_bonus accepts a float for bonus
    #it calculates the contribution = bonus * the global constant
    #it outputs the contribution for bonuses