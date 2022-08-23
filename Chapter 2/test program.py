#print_something receives no arguments
#it prints a message
def print_something():
    #print a message
    print("This is your message")
    
#another function recieves no arguments
#it just output two messages separated by a blank line
def another_function():
    print("This is message 1")
    print()
    print("This is message 2")
    
    turtle.penup()
    turtle.goto(-70,200)
    turtle.dot()
    turtle.write('Betelgeuse')
    turtle.pendown()
    turtle.goto(-40,-20)
    turtle.dot()
    turtle.write('Alnitka')
    turtle.goto(-90,-180)
    turtle.dot()
    turtle.write('Saiph')
    turtle.penup()
    turtle.goto(-40,-20)
    turtle.pendown()
    turtle.goto(0,0)
    turtle.dot()
    turtle.write('Alnitam')
    turtle.goto(40,20)
    turtle.dot()
    turtle.write('Mintaka')
    turtle.goto(80,100)
    turtle.dot()
    turtle.write('Meissa')
    turtle.goto(40,20)
    turtle.goto(120,-140)
    turtle.dot()
    turtle.write('Rigel')
    turtle.done()

