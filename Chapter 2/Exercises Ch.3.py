import turtle

def turtleprog2():
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
    angle = float(input("Enter the projectile's angle:"))
    force = float(input("Enter the launch force (1-10):"))
    
    distance = force * FORCE_FACTOR # calculate
    
    turtle.setheading(angle)
    turtle.forward(distance)
    
    else:
        print("You missed the target.")
    
    