def bug_collector():
    
    total = 0
    
    print("Welcome to Bug Masters bug collection system.") # print message
    
    for counter in range(1,6): # loop it for the amt of days
        
        print("Please enter a value for day", counter, end = '') # print the value
      
        amt = int(input(": ")) # get the value
        total = total + amt
        
    print("Great job, you collected", total, "bugs this week. You're the bug master!")
    
def distance_traveled():
    
    counter = 0
    
    print("Enter the speed of the vehicle in mph", end = '') # print the value
    speed = int(input(": ")) # get the value
    
    print("Enter how many hours the vehicle traveled", end = '') # print the value
    hours = int(input(": ")) # get the value

    print("Hours\t\tDistance Traveled")
    print("_________________________________")
        
    while counter < hours:
        
        counter += 1
        distance = counter * speed
        print(counter,"\t\t",distance)
        
def pennies():
    
    counter = 1 # define counter
    salary = 0.01
    
    print("How many days do you want to accure pennies?", end = '') # print the phrase
    
    days= int(input(": ")) # get the value
    print("Day\t\tSalary") # print day and salary
    print("---------------------------") # print seperator
    
    
    while counter < days:
        
        counter += 1
        salary = salary * 2
        print (counter,"\t\t", "$ ", salary)
        
def hogwarts_tuition():
    
    counter = 1
    tuition = 8000
    years = 5
    rate = 0.03
    
    for year in range(years): # loop it for the amt of years
        tuition *= rate + 1
        print((year + 1), "\t\t\t", tuition)
        
def population():
    
    counter = 1
    population = int(input("Enter the starting population: "))
    daily_growth = int(input("Enter the percent of daily growth: "))
    days = int(input("Enter the number of days to simulate: "))
    print(" ")
    print("Day \t\t\t Projected Population")
    print("----------------------------------------------")
        
    for day in range(days-1):
        #population = population * 30%
        counter += 1
        days += 1
        daily_growthh = daily_growth / 100
        
        population = population * daily_growthh + population
        
        
        print(counter, "\t\t\t", population)
        
def reverse_triangle():
        
    
    base = int(input("Enter the base size of the triangle: "))
    
    for row in range(base - 1, base):
        for column in range(row):
            print("*", end='')
            print()
            
def repeating_squares():
    
    import turtle
    
    TURTLE_START_Y = 250
    TURTLE_START_X = 250
    
    turtle.penup()
    turtle.goto(TURTLE_START_X, TURTLE_START_Y)