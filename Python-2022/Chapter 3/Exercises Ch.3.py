import turtle

def turtleprog2():
    #set numbers as words
    TARGET_LLEFT_X = 150
    TARGET_LLEFT_Y = 250
    TARGET_WIDTH = 25
    FORCE_FACTOR = 30
    PROJECTILE_SPEED = 1
    NORTH = 90
    SOUTH = 270
    EAST = 0
    WEST = 180
    
    #make my target
    turtle.penup()
    turtle.goto( TARGET_LLEFT_X, TARGET_LLEFT_Y)
    turtle.pendown()
    turtle.setheading(EAST)
    turtle.forward(TARGET_WIDTH)
    turtle.setheading(SOUTH)
    turtle.forward(TARGET_WIDTH)
    turtle.setheading(WEST)
    turtle.forward(TARGET_WIDTH)
    turtle.setheading(NORTH)
    turtle.forward(TARGET_WIDTH)
    turtle.penup()
    
    #set turtle up
    turtle.goto( 0, 0)
    turtle.setheading (EAST)
    turtle.showturtle()
    turtle.speed(PROJECTILE_SPEED)
    
    #turtle angle, force
    angle = float(input("Enter the projectile's angle:")) # get prohectile's angle
    force = float(input("Enter the launch force (1-10):")) # recieve launch force
    
    distance = force * FORCE_FACTOR # calculate
    
    turtle.setheading(angle) # set angle turtle goes
    turtle.forward(distance) # set distance turtle goes
    
    if (turtle.xcor() >= TARGET_LLEFT_X and
        turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and
        turtle.ycor() >= TARGET_LLEFT_Y and
        turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
        print("Target hit!")
    else:
        print("You missed.")
    
def day_convertor():
    
    Lunes=1
    Martes=2
    Miércoles=3
    Jueves=4
    Viernes=5
    Sábado=6
    Domingo=7
    
    answer = float(input("Choose a number from 1 to 7: ")) #Get desired value
    
    if answer == Lunes: # print lunes
        print("Lunes.")
    else: # print martes
        if answer ==Martes:
            print("Martes.")
        else: #  print miércoles
            if answer ==Miércoles:
                print("Miércoles.")
            else: # print jueves
                if answer ==Jueves:
                    print("Jueves.")
                else: # print viernes
                    if answer ==Viernes:
                        print("Viernes.")
                    else: # print sábado
                        if answer ==Sábado:
                            print("Sábado.")
                        else: # print  domingo
                            if answer ==Domingo:
                                print("Domingo.")
                            else: # print the error
                                print("Error.")
                                
def roman_numerals():
    answer = float(input("Choose a number from 1 to 10: ")) #Get desired value from 1-10
    
    I=1
    II=2
    III=3
    IV=4
    V=5
    VI=6
    VII=7
    VIII=8
    IX=9
    X=10
    
    if answer == I: # print I
        print("I.")
    else: # print II
        if answer ==II:
            print("II.")
        else: #  print III
            if answer ==III:
                print("III.")
            else: # print IV
                if answer ==IV:
                    print("IV.")
                else: # print V
                    if answer ==V:
                        print("V.")
                    else: # print VI
                        if answer ==VI:
                            print("VI.")
                        else: # print  VII
                            if answer ==VII:
                                print("VII.")
                            else: # print  VIII
                                if answer ==VIII:
                                    print("VIII.")
                                else: # print  IX
                                    if answer ==IX:
                                        print("IX.")
                                    else: # print  X
                                        if answer ==X:
                                            print("X.")
                                        else: # print error
                                            print("Error.")
                                            
def color_mixer():
    
    colorinp = input("Choose a primary color: ") #Get 1st desired color
    colorinp2 = input("Choose a 2nd primary color: ") #Get 2nd desired color
    if (colorinp == "red" or colorinp =="blue" or colorinp =="yellow" and
        colorinp2 == "red" or colorinp2 =="blue" or colorinp2 =="yellow"):
        print("Your color selections are good...")
   
        if ( colorinp2 == "blue" and  colorinp == "red" or colorinp2 == "red" and colorinp == "blue" ):
            print("Your color is: purple.") # print if purple
                
        if ( colorinp2 == "red" and  colorinp == "yellow" or colorinp2 == "yellow" and colorinp == "red" ):
            print("Your color is: orange.") # print if orange
                
        if ( colorinp2 == "yellow" and  colorinp == "blue" or colorinp2 == "blue" and colorinp == "yellow" ):
            print("Your color is: green.")    # print if green
    else:
        print("Error.") #print error if primary color isnt given

def hot_dog():
    
    hotdog_pack = 10
    hotdogbun = 8
    
    amt_of_ppl = int(input("Amount of people attending: ")) # get amt of people attending
    amt_of_hotdogs = int(input("Amount of hotdogs per person: ")) #get amt of hotdogs per person
    
    hotdogs = (amt_of_ppl*amt_of_hotdogs) # calc amt of hotdogs needed
    
    amtofhotdogs = (hotdogs/hotdog_pack) # calc amt of hot dog packs needed
    amtofhotdogs2 = (hotdogs%hotdog_pack) # calc amt of extra hot dogs
    
    amtofbuns = (hotdogs/hotdogbun) # calc amt of bun packs needed
    amtofbuns2 = (hotdogs%hotdogbun) # calc amt of extra buns
    
    print("You will need", amtofhotdogs, "pack(s) and", amtofhotdogs2, "remaining.")
    print("You will need", amtofbuns, "pack(s) and", amtofbuns2, "remaining.")
    
def time_calculator():
    
    amt_of_seconds = int(input("Amount of seconds: ")) # get the amount of seconds needed
    
    if amt_of_seconds >= 60 and amt_of_seconds <= 3600: # determine whether or not to use the if
        calc_min = amt_of_seconds // 60 # divide for number of minutes
        min_sec = amt_of_seconds % 60 # find the remaining seconds
        calc_min2 = format(calc_min, '.0f') # format for no decimals
        print("There are", calc_min2, "minute(s) and", min_sec, "second(s).") # print the minutes and seconds
        
    if amt_of_seconds >= 3600 and amt_of_seconds <= 86400: # determine whether or not to use the if
        calc_hour = amt_of_seconds // 3600 # divide to find the amount of hours
        
        hour_rem = calc_hour % 60 # find the remaining hours
        hour_sec = hour_rem / 1 # find the reminaining seconds
        calc_hour2 = format(calc_hour, '.0f') # format for no decimal places
        hour_rem2 = format(hour_rem, '.0f') # find the remaining hours
        print("There are", calc_hour2 , "hour(s),", hour_rem2 , "minute(s) and,", hour_sec , "second(s).")
    
    if amt_of_seconds >= 86400: # determine whether or not to use the if
        
        days1 = (amt_of_seconds // 86400)
        days2 = (amt_of_seconds % 86400)
        hours1 = (days2 // 3600)
        hours2 = (hours1 % 3600)
        minutes1 = (hours2 % 60)
        seconds = minutes1
        print("There are", days1 , "day(s),", hours2 , "hour(s),", minutes1 , "minute(s), and", seconds, "second(s)")
        
def leap_year():
    year = int(input("Please enter a year: ")) # get the year
    check1_1 = year/100
    check1_2 = year/400
    check1_3 = year/4
    
    if (check1_1.is_integer()) and (check1_2.is_integer()):
        print(year, "is a leap year. There are 29 days in the month of February.")
    
    if (check1_3.is_integer()):
        print(year, "is a leap year. There are 29 days in the month of February")
        
    else:
        print(year, "is not a leap year. There are 28 days in the month of February.")
    
def sir_fix_alot():
    first = input("Reboot computer and try to connect. (y/n):")
    
    
    if first == "n":
        second = input("Reboot router and try to connect. (y/n):")
            
            
        if second == "n":
            third = input("Verify cables are are firmly attached. (y/n):")
                
            
            if third == "n":
                fourth = input("Move router to better location. (y/n):")
                    
                    
                if fourth == "n":
                    print("Get a new router.")
                    
    else:
        print("Netflix and Chill.")
            
def can_we_just_eat():
    
    vegetarian = input("Is anyone in your party a vegetarian? (y/n)")
    vegan = input("Is anyone in your party a vegan? (y/n)")
    lactose = input("Is anyone in your party gluten intolerant? (y/n)")

    print("Here are your restaraunt choices: ")
    
    if vegetarian == "y" and vegan == "y" and lactose == "y":
        print("Corner Café")
        print("Chef's Kitchen")
        print("Main Street Pizza Company")
    if vegetarian == "y" and vegan == "y" and lactose != "y":
        print("Corner Café")
        print("Chef's Kitchen")
    if vegetarian == "y" and vegan == "y" and lactose == "y":
        print("Corner Café")
        print("Chef's Kitchen")
 
def turtleprog2():
    #set numbers as words
    TARGET_LLEFT_X = 150
    TARGET_LLEFT_Y = 250
    TARGET_WIDTH = 25
    FORCE_FACTOR = 30
    PROJECTILE_SPEED = 1
    NORTH = 90
    SOUTH = 270
    EAST = 0
    WEST = 180
    
    #make my target
    turtle.penup()
    turtle.goto( TARGET_LLEFT_X, TARGET_LLEFT_Y)
    turtle.pendown()
    turtle.setheading(EAST)
    turtle.forward(TARGET_WIDTH)
    turtle.setheading(SOUTH)
    turtle.forward(TARGET_WIDTH)
    turtle.setheading(WEST)
    turtle.forward(TARGET_WIDTH)
    turtle.setheading(NORTH)
    turtle.forward(TARGET_WIDTH)
    turtle.penup()
    
    #set turtle up
    
    turtle.goto( 0, 0)
    turtle.setheading (EAST)
    turtle.showturtle()
    turtle.speed(PROJECTILE_SPEED)
    
    #turtle angle, force
    angle = float(input("Enter the projectile's angle:")) # get prohectile's angle
    force = float(input("Enter the launch force (1-10):")) # recieve launch force
    
    distance = force * FORCE_FACTOR # calculate
    
    turtle.setheading(angle) # set angle turtle goes
    turtle.forward(distance) # set distance turtle goes
    
    if (turtle.xcor() >= TARGET_LLEFT_X and
        turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and
        turtle.ycor() >= TARGET_LLEFT_Y and
        turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
        print("Target hit!")
        
    elif angle > 70:
      print('You missed the target.  Try using less angle.')

    elif angle < 65:
      print('You missed the target.  Try using more angle.')

    elif (turtle.xcor() < 100 and turtle.ycor() < 250):
      print("You missed the target.  Try using more force.")

    elif (turtle.xcor() > 125 and turtle.ycor() > 275):
      print("You missed the target.  Try using less force.")

    else:
      print("You're so close!")

