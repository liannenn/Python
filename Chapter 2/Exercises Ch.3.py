import turtle

def turtleprog2():
    #set numbers as words
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600
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
        calc_min = amt_of_seconds / 60 # divide for number of minutes
        min_sec = amt_of_seconds % 1 # find the remaining seconds
        calc_min2 = format(calc_min, '.0f') # format for no decimals
        print("There are", calc_min2, "minute(s) and", min_sec, "second(s).") # print the minutes and seconds
        
    if amt_of_seconds >= 3600 and amt_of_seconds <= 86400: # determine whether or not to use the if
        calc_hour = amt_of_seconds / 3600 # divide to find the amount of hours
        hour_rem = calc_hour % 60 # find the remaining hours
        hour_sec = hour_rem % 1 # find the reminaining seconds
        calc_hour2 = format(calc_hour, '.0f') # format for no decimal places
        hour_rem2 = format(hour_rem, '.0f') # find the remaining hours
        print("There are", calc_hour2 , "hour(s),", hour_rem2 , "minute(s) and,", hour_sec , "second(s).")
    
    if amt_of_seconds >= 86400: # determine whether or not to use the if
        calc_days = amt_of_seconds / 86400 # divide to find the amount of days
        day_hours = calc_days % 86400 # find the remaining hours
        day_min = day_hours % 3600 # find the reminaining minutes
        day_sec = day_min % 60
        calc_days2 = format(calc_days, '.0f') # format for no decimal places
        print("There are", calc_days2 , "day(s),", day_hours , "hour(s),", day_min , "minute(s) and,", day_sec ,"second(s).")
        
    
def leap_year():
    year = int(input("Please enter a year: ")) # get the year
    
def sir_fix_alot():
    n = 1
    first = input("Reboot computer and try to connect. (y/n):")
    
    
    if first == 1:
        second = input("Reboot router and try to connect. (y/n):")
            
            
        if second == 1:
            third = input("Verify cables are are firmly attached. (y/n):")
                
            
            if third == 1:
                fourth = input("Move router to better location. (y/n):")
                    
                    
                if fourth == 1:
                    fifth = input ("Get a new router. (y/n):")
                        
                    if fifth ==1:
                        print ("Get a new router.")
                    
        else:
            print("Netflix and Chill.")
