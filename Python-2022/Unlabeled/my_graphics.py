import turtle #imports turtle
def square(x, y, width, color):
    #causes square to need an x, y, width,
    #and color
    # the x, and y are the lower left corner
    
    turtle.penup() # puts pen up
    turtle.goto(x, y) # makes it go to the x, and y given
    turtle.fillcolor(color) # begins to fill using color given
    turtle.pendown() # puts pen down
    turtle.begin_fill() # begins fill
    
    for count in range(4):  # makes turtle go 4 times
        turtle.forward(width) # makes turtle go forward width given
        turtle.left(90) # makes turtle take a 90 turn
    turtle.end_fill() # ends fill
    
def circle(x, y, radius, color):
    
    turtle.penup() # Raise the pen
    turtle.goto(x, y - radius) # Position the turtle
    turtle.fillcolor(color) # Set the fill color
    turtle.pendown() # Lower the pen
    turtle.begin_fill() # Start filling
     
    turtle.circle(radius) # Draw a circle
    turtle.end_fill() # End filling
    
def line(startX, startY, endX, endY, color):
    turtle.penup() # Raise the pen
    turtle.goto(startX, startY) # Move to the starting point
    turtle.pendown() # Lower the pen
    turtle.pencolor(color) # Set the pen color
    turtle.goto(endX, endY) # Draw a square
    
