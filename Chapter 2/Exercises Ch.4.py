def bug_collector():
    
    total = 0 # prime the accumulator 
    
    print("Welcome to Bug Masters bug collection system.") # print message
    
    for counter in range(1,6): # loop it for the amt of days
        
        print("Please enter a value for day", counter, end = '') # print the value
      
        amt = int(input(": ")) # get the value
        total = total + amt # increment the accumulator
        
    print("Great job, you collected", total, "bugs this week. You're the bug master!") # print total of bugs collected
    
def distance_traveled():
    
    counter = 0 # prime the acccumulator
    
    print("Enter the speed of the vehicle in mph", end = '') # print the value
    speed = int(input(": ")) # get the value
    
    print("Enter how many hours the vehicle traveled", end = '') # print the value
    hours = int(input(": ")) # get the value

    print("Hours\t\tDistance Traveled") # print the heading 
    print("_________________________________") # print the separator 
        
    while counter < hours: # set the while loop for when hours are greater than counter
        
        counter += 1 # increment the accumulator 
        distance = counter * speed # calculator the distance
        print(counter,"\t\t",distance) # print the counter and distance
        
def pennies():
    
    counter = 1 # define counter
    salary = 0.01 # set salary to calc for a percentage
    
    print("How many days do you want to accure pennies?", end = '') # print the phrase
    
    days= int(input(": ")) # get the value
    print("Day\t\tSalary") # print day and salary
    print("---------------------------") # print seperator
    
    
    while counter < days: # set the while for when days is greater than the counter
        
        counter += 1 # increment the accumulator 
        salary = salary * 2 # calculate the salary
        print (counter,"\t\t", "$ ", salary) # print the counter along with the salary
        
def hogwarts_tuition():
    
    counter = 1 # def counter
    tuition = 8000 # set tuition
    years = 5 # get years
    rate = 0.03 # set rate
    
    for year in range(years): # loop it for the amt of years
        tuition *= rate + 1 # calculate tuition
        print((year + 1), "\t\t\t", tuition) # print year, and tuition
        
def population():
    
    counter = 1 # def counter
    population = int(input("Enter the starting population: ")) # input population
    daily_growth = int(input("Enter the percent of daily growth: ")) # input daily growth
    days = int(input("Enter the number of days to simulate: ")) # input days
    print(" ") # print separator
    print("Day \t\t\t Projected Population") # print days and projected population
    print("----------------------------------------------") # print separator
        
    for day in range(days-1): # for loop for days - 1
        population = population * 30
        counter += 1 # increment the accumulator 
        days += 1 # increment days
        daily_growthh = daily_growth / 100 # calc daily growth
        
        population = population * daily_growthh + population # calc population
        
        
        print(counter, "\t\t\t", population) # print counter and population
        
def reverse_triangle():
        
    
    base = int(input("Enter the base size of the triangle: "))
    
    for row in range(base -1 , base ):
        for column in range(row):
            print("*", end='')
            print()
            
def stair_pattern():
    
    steps = int(input("Enter the number of stairs: "))
    
    for stairs in range(1, steps + 1):
        for column in range(stairs):
            print(" ", end='')
        print(" ")
            
def repeating_squares():
    
    import turtle # imports turtle
    
    squares =int(input("Enter the amount of squares you would like? ")) # inputs amt of squares
    
    counter = 1 # increment the accumulator
    TURTLE_START_Y = -40 # set turtle's starting y point
    TURTLE_START_X = -40 # set turtle's starting x point
    TURTLE_WRITE = 20 # set turtle's 1st writing distance
    
    NORTH = 90 # shortcut for noth
    SOUTH = 270 # shortcut for south
    EAST = 0 # shortcut for east
    WEST = 180 #shortcut for west
    
    turtle.penup() # set pen up 
    turtle.goto(TURTLE_START_X, TURTLE_START_Y) # move to turtle's starting x and y point

    
    
    while counter <= squares: # begin the while loop
        
        counter = counter + 1 # keep a running total until counter is greater than squares
        turtle.pendown() # set pen down to start writing
        turtle.forward(TURTLE_WRITE) # move turtle 
        turtle.setheading(EAST) # set turtle east
        
        turtle.forward(TURTLE_WRITE) # move turtle
        turtle.setheading(SOUTH) # set turtle south
        
        turtle.forward(TURTLE_WRITE) # move turtle
        turtle.setheading(WEST) # set turtle west
        
        turtle.forward(TURTLE_WRITE) # move turtle
        turtle.setheading(NORTH) # set turtle north
        
        TURTLE_WRITE = TURTLE_WRITE + 25 # set turtle_write so it changes the distance per square
        
def hypnotic_pattern():
    
    offset = 5
    import turtle # imports turtle
    
    swirlies =int(input("Enter the amount of swirlies you would like? ")) # inputs amt of squares
    
    counter = 1 # increment the accumulator
    TURTLE_START_Y = -40 # set turtle's starting y point
    TURTLE_START_X = -40 # set turtle's starting x point
    TURTLE_WRITE = 20 # set turtle's 1st writing distance
    
    NORTH = 90 # shortcut for noth
    SOUTH = 270 # shortcut for south
    EAST = 0 # shortcut for east
    WEST = 180 #shortcut for west
    
    turtle.penup() # set pen up 
    turtle.goto(TURTLE_START_X, TURTLE_START_Y) # move to turtle's starting x and y point

    
    
    while counter <= swirlies: # begin the while loop
        turtle.goto(TURTLE_START_X, TURTLE_START_Y)
        
        turtle.setheading(NORTH)
        turtle.forward(TURTLE_WRITE)
        
        turtle.setheading(WEST)
        turtle.forward(TURTLE_WRITE)
        
        turtle.setheading(SOUTH)
        turtle.forward(TURTLE_WRITE)
        
        turtle.setheading(EAST)
        turtle.forward(TURTLE_WRITE)
        
        
        
        
        TURTLE_WRITE = TURTLE_WRITE + 5
        