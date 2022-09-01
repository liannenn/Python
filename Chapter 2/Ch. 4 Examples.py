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
    
    
