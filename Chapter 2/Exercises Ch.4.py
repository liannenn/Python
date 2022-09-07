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
    
    start_pop = int(input("Enter the starting population: "))
    daily_growth = int(input("Enter the percent of daily growth: "))
    days = int(input("Enter the number of days to simulate: "))
        
    for day in range(days):
        counter += 1
        