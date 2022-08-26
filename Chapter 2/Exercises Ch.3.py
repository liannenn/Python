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
    
    if answer == I: # print lunes
        print("I.")
    else: # print martes
        if answer ==II:
            print("II.")
        else: #  print miércoles
            if answer ==III:
                print("III.")
            else: # print jueves
                if answer ==IV:
                    print("IV.")
                else: # print viernes
                    if answer ==V:
                        print("V.")
                    else: # print sábado
                        if answer ==VI:
                            print("VI.")
                        else: # print  domingo
                            if answer ==VII:
                                print("VII.")
                            else: # print  domingo
                                if answer ==VIII:
                                    print("VIII.")
                                else: # print  domingo
                                    if answer ==IX:
                                        print("IX.")
                                    else: # print  domingo
                                        if answer ==X:
                                            print("X.")
                                        else:
                                            print("Error.")
                                            
def color_mixer():
                                              