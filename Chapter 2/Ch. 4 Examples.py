def loop_example():
#loop accepts not arguments
#it takes input from the user for the number of loops
#and loops until it reaches the user input

    number = int(input("Enter the number of loops to run: "))
    counter = 1 #prime the accumulator
    keep_going = "y" #prime the sentinel to y
    
    while counter <= number:
        #run these lines of code
        print("This is loop number", counter)
        counter = counter + 1 #counter += 1
        keep_going = input("Keep going? (y/n)")
        
def commission():
    
    keep_going == "y" # label keep going as y    
    while keep_going == "y":
    
        sale = input("Enter the sale amount:") # input sale
        percent = input("Enter the commission rate:") # input percent
    
        calc = sale * percent # calc the sale and percent
    
    print("The commission is $", calc) # print the commission 
    
    keep_going = input("Do you want to calculate another? (y/n)")
    
def temperature():
    
    MAX_TEMP = "102.5"
    
    temp1 == MAX_TEMP # label keep going as
    while temp1 == MAX_TEMP:
    
        temp1 = input("Please enter the current substance temperature in degrees Celsius:")
    
    if temp1 >= MAX_TEMP:
        print("The temperature is too high.")
        print("Turn the thermostat down and wait for it too cool")
        print("Then wait 5 minutes and measure again.")
        
    print("The temperature is acceptable.")
    print("Measure again in 15 minutes.")

def loop_example2():
    # accepts no argumemts
    #it uses a for loop to loop 5 times
    #and outputs a number
    
    for item in range (5):
        print(item)
            
def loop_example3():
    #accepts no arguments
    #it uses a for loop to loop trough 1, 2, 3, 4
    #and outputs the loop
    
    for num in [1, 2, 3, 4]:
        print("I am holding the value", num)
        print("I will now release the value of num")
        print("...")
        
def simple_loop1():
    #accepts no arguments
    #it uses a for loop to loop trough 1, 2, 3, 4
    #and outputs the loop
    
    for num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        print(num)
        
def simple_loop2():
    #print odd numbers
    for num in [1, 3, 5, 7, 9]:
        print("I will output all odd numbers from 1-10")
        print(num)
        
def simple_loop3():
    for num in ['Steve', 'Tony', 'Thor', 'Wanda']:
        print(num)
        
def program4_4():
    for num in range (10): # range 1-10
        print(num) # print 
        
def hello_world_loop():
    for count in range(5): #print hello world five times
        print("Hello World!") # gives range something to right
        
def squares():
    print("Number Square")#print numbe and square
    print("------------------")
    print("\t")
    for num in range(1,11):
        square = num**2
        print(num, "\t", square)
        
def speed_convertor():
    print("KPH      MPH")#print numbe and square
    print("------------------")
    print("\t")
    for KPH in range(60+10):
        MPH = KPH *.06241
        print(KPH, "\t", MPH)
        
def user_squares1():
    squaresamt = int(input("How many squares?"))
    print("Number   Square")
    print("------------------")
    for squares in range(0,squaresamt):
        square = squaresamt**2
        print(squaresamt, "\t", square)
        
def user_squares2():
    squaresamt1 = int(input("How many squares?"))
    squaresamt2 = int(input("How many squares?"))
    print("------------------")
    for squares in range(squaresamt1, squaresamt2):
        print("Number   Square")
        square = squares**2
        print(squares, "\t", square)
        
def sum_numbers():
    MAX = 5 # define max
    print("This program calculates te sum of 5 numbers you will need.") # print 
    for counter in range(MAX): # choose the range for it
        number = int(input("Please enter a number: ")) # input MAX numbers
        total = total + number # calc
        print("The total of your", MAX, "numbers is", total) #print the total
        
def property_tax():
    #ask for lot number with 0 to end
    #calculate the portperty value
    #print the property tax
    #print again
    
    lot_numb = input("Please enter a lot number (enter 0 to end): ") # input the lot number
    prop_value = input("Please enter the property value:") # input the property value
    prop_calc = lot_numb * prop_value @ .0065
    print("Property tax: $", prop_calc)
    
    
def loop1():
    #loop 1 takes no arguments
    #it loops through 1- times calculating a running
    #total and outputs the total as it processes
    
    LOOP_END = 10 #named the constant for the max iteraitons
    counter = 1 #accumulator to create a counted loop
    total = 0 #variable for running total
    
    #start the loop
    while counter < LOOP_END:
        
        #increment the accumulator
        counter+=1 #this is the equivalent as counter = counter + 1
        
        #as long as counter < 10 these willl excute
        print("The loop has run", counter, "times.")
        total = total + counter
        
        #output a message witht he running total
        print("The total of numbers 1 - 10 for this iteration is: ", total)
        
        #the loop statements are over, so it will return to the while statement
        # to test the condition again.
        
def loop2(): #for loop example
    #loop 2 accepts noa rguments
    # it calculates a running total of numbers 1-10
    # and outputs the total
    
    LOOP_BEGIN = 1
    LOOP_END = 10
    total = 0
    
    for num in range(LOOP_BEGIN, LOOP_END +1): #for loop to iterate from 1 - 10
        #as long as values remain between 1 (LOOP_BEGIN) - 10 (LOOP_END), iterate
        
        total = total + num #keep a running total of all values from 1 - 10
        
        print('The loop has iterated', num, 'times.')
        print('The total for this iteration of all numbers 1-10 is: ', total)
        
        #loop staements are finished, return to the for loop start. If any numbers remain, continue.
        
def gross_pay():
    # gross pay accepts no arguments
    #it takes input frm the user in the form of hours worked and pay rate
    # it calculates and outputs the gross pay
    
    hours = int(input("Enter the number of hours worked for 1 week: ")) # get hours worked
    
    pay_rate = int(input("Enter the hourly rate: ")) # get pay rate
    
    gross_oay = hours * pay_rate
    
    #output gross play
    print("Gross pay: $", format(gross_pay, '.2f'), sep= '')
    
def retail_no_validation(): # Prgram 4-15
    #retail no validation accepts no arguments
    #it uses a string sentinel cariable to control the loop
    #it loops until the user no longer enters "y" or "Y" to continue
    # and outputs the retail price
    
    MARK_UP = 1.25 #named constant for makup percent
    another = 'y' #set the sentinel variable to loop
    
    #process through the loop
    while another == 'y' or another == "Y":
        #prompt the user for the wholesale price
        wholesale = float(input("Enter the wholesale cost: "))
        
        #calculate retail price
        retail - wholesale * MARK_UP
        
        #output the retail price
        print("Retail price: $", format(retail, ',.2f'), sep='')
        
        #Promopt to continue
        another = input ("Do you want another item?" +
                        "(Enter y for yes): ")
        
def retail_with_validation(): # Prgram 4-15
    #retail no validation accepts no arguments
    #it uses a string sentinel cariable to control the loop
    #it loops until the user no longer enters "y" or "Y" to continue
    # and outputs the retail price
    
    MARK_UP = 1.25 #named constant for makup percent
    another = 'y' #set the sentinel variable to loop
    
    #process through the loop
    while another == 'y' or another == "Y":
        #prompt the user for the wholesale price
        wholesale = float(input("Enter the wholesale cost: "))
        
        #check whether or not a positive number was used
        while wholesale < 0:
            wholesale = int(input("Enter the wholesale cost: "))
        
        #calculate retail price
        retail = wholesale * MARK_UP
        
        #output the retail price
        print("Retail price: $", format(retail, ',.2f'), sep='')
        
        #Promopt to continue
        another = input ("Do you want another item?" +
                        "(Enter y for yes): ")
        
def test_score_averages():

    student = int(input("How many students?"))
    tests_per = int(input("How man tests per student? "))
    print("---------------------------------------")
    
    for student in range(1, student + 1):
        total = 0.0
        print("Student number: ", student)
        print("---------------------------------------")
    for tests_per in range( 1, tests_per + 1):
        print("Test number: ", tests_per, end='')
        score = float(input(": "))
        total += score
        
        avg = total/test_per
        print("The average for student number", student, "is", format(avg_tests, '.2f'))
        print()

def rectangle_pattern():
    rows = int(input("Enter the number of rows to print: "))
    columns = int(input("Enter the number of columns to print: "))
    print()
    
    for row in range(rows):
        
        for column in range(columns):
            print("*", end='')
    print()

def triangle_pattern():
    
    base = int(input("Enter the base size of the triangle: "))
    
    for row in range(1, base + 1):
        for column in range(row):
            print("*", end='')
        print()
        
def new_range_example():
    
    for num1 in range(1,6):
        print('*')
        for num2 in range(num1):
            print("&")
            for num3 in range(num2):
                print("@")
                
def stair_pattern():
        
    steps = int(input("Enter the number of stairs: "))
    
    for stairs in range(1, steps + 1):
        for column in range(stairs):
            print(" ", end='')
        print("@")
        
def turtle_square():
    for x in range(4):
        turtle.forward(120)
        turtle.right(90)
        
def turtle_octagon():
    for x in range(8):
        turtle.forward(100)
        turtle.right(45)
        
def concentric_circles():
    num_circles = int(input("Enter the number of circles: "))
    STARTING_RADIUS = 20
    OFFSET = 10
    ANIMATION_SPEED = 0
    
    turtle.speed(ANIMATION_SPEED)
    
    radius = STARTING_RADIUS
    
    for circle in range(num_circles):
        turtle.circle(radius)

    xcor = turtle.xcor()
    ycor = turtle.ycor()

    turtle.ycor(OFFSET)
    radius = radius + OFFSET
    
    turtle.penup()
    turtle.goto(xcor, ycor)
    turtle.pendown()
    
def spiral_circles():
    
    NUM_CIRCLES = 36 #number of circles to draw
    RADIUS = 100 #radius of each circle
    ANGLE = 10 #angle to turn
    ANIMATION_SPEED = 0
    
    turtle.speed(ANIMATION_SPEED)
    turtle.color("blue")
    
    for x in range(NUM_CIRCLES):
        turtle.circle(RADIUS)
        turtle.left(ANGLE)
   
    