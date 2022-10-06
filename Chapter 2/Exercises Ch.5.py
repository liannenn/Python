import math
import random
import turtle

def sales_tax():
    
    sale_amt = float(input('Please enter the sale amount: ')) #Get sale amt + print it
    purchase_price = float(input('Your purchase price was:\t$\t     ')) #Get sale amt + print it
    
    taxes(purchase_price, sale_amt)
    
    # -------------------------------------------------------------------- #
    
def taxes(purchase_price, sale_amt):
    
    state_tax = (purchase_price * 0.05) #calc state tax
    county_tax = (purchase_price * 0.025) #calc county tax
    total_tax = (state_tax + county_tax)#calc total tax
    total_sale = (total_tax+sale_amt) #calc the total sale
    
    tax_amts(state_tax, county_tax, total_tax, total_sale)
    
    # -------------------------------------------------------------------- #
    
def tax_amts(state_tax, county_tax, total_tax, total_sale):

    print("Your state tax amount is:\t$\t", format(state_tax,'10.2f'))#Print state tax amt
    print("Your county tax amount is:\t$\t", format(county_tax,'10.2f'))  #Print county tax amt
    print("Your total tax is:\t\t$\t", format(total_tax,'10.2f'))  #Print total tax amt
    print("Your total sale is:\t\t$\t  ", format(total_sale,'10.2f'))  #Print total sale amt
    
    # ____________________________________________________________________ #
    
def calories():
    
    grams_carbs = int(input("How many grams of carbs did you consume? "))
    grams_fat = int(input("How many grams of fat did you consume? "))
    
    grams_to_calories(grams_carbs, grams_fat)
    
    # -------------------------------------------------------------------- #
       
def grams_to_calories(grams_carbs, grams_fat):
    
    fat_calories = grams_fat * 9
    gram_calories = grams_carbs * 4
    
    calories_consumed(fat_calories, gram_calories)
    
    # -------------------------------------------------------------------- #
    
def calories_consumed(fat_calories, gram_calories):
    
    print("Here is your calorie intake for the day.")
    print("You consumed", gram_calories, "calories worth of carbs today. Nice work...")
    print("You consumed", fat_calories, "calories worth of carbs today. Nice work...")
    
    # ____________________________________________________________________ #
    
def stadium_seating():
    
    class_A()
    
    # -------------------------------------------------------------------- #
    
def class_A():
    
    classAtickets = int(input("Enter the number of class A tickets sold: "))
    
    if classAtickets <= 0:
        classAtickets = int(input("Enter a valid number of class A tickets sold: "))
        
        class_B(classAtickets)
        
    else:   
        class_B(classAtickets)
        
    # -------------------------------------------------------------------- #
       
def class_B(classAtickets):
    
    classBtickets = int(input("Enter the number of class B tickets sold: "))
    
    if classBtickets <= 0:
        classBtickets = int(input("Enter a valid number of class B tickets sold: "))
        
        class_C(classAtickets, classBtickets)
        
    else:
        class_C(classAtickets, classBtickets)
        
    # -------------------------------------------------------------------- #
        
def class_C(classAtickets, classBtickets):
    
    classCtickets = int(input("Enter the number of class C tickets sold: "))
    
    if classCtickets <= 0:
        classCtickets = int(input("Enter a valid number of class C tickets sold: "))
        
        calculate_money(classAtickets, classBtickets, classCtickets)
        
    else:
        calculate_money(classAtickets, classBtickets, classCtickets)
       
    # -------------------------------------------------------------------- #
       
def calculate_money(classAtickets, classBtickets, classCtickets): 
    
    classAtickets = classAtickets * 20
    classBtickets = classBtickets * 15
    classCtickets = classCtickets * 10
    
    total_cash = classAtickets + classBtickets + classCtickets 
    
    print("The total income from the tickets is: $", total_cash)
    
    # ____________________________________________________________________ #
  
def paint_estimator():
    
    square_ft = int(input("Please enter the total square feet to be painted: "))
    paint_cost = int(input("How much is each gallon of paint: "))
    
    print("The cost breakdown to paint ", square_ft, " square feet is:")
    
    print("-----------------------------------------------------------")
    
    paint_estimator2(square_ft, paint_cost)
    
    # -------------------------------------------------------------------- #
    
def paint_estimator2(square_ft, paint_cost):
    
    paint_gallons = square_ft / 112
    paint_total = paint_gallons * paint_cost
    labor_total = (paint_gallons * 8) * 35
    
    paint_estimator3(paint_total, labor_total)
    
    # -------------------------------------------------------------------- #
    
def paint_estimator3(paint_total, labor_total):
    
    print("Total cost of paint: $", paint_total)
    print("Total labor cost: $", labor_total)
    
    total_total = paint_total + labor_total 
    
    print("Total cost of the job is: $", total_total)
    
    # ____________________________________________________________________ #
    
def math_quiz():
    
    get_numbers()
    
    # -------------------------------------------------------------------- #
    
def get_numbers():
    
    number1 = random.randint(1, 200)
    number2 = random.randint(1, 200)
    
    visual_math(number1, number2)

    # -------------------------------------------------------------------- #

def visual_math(number1, number2):
    
    print("Solve:")
    print(" ")
    print("\t", number1)
    print("+ \t", number2)
    add_answer = int(input("Answer:" ))
    
    answer = number1 + number2
    
    if add_answer == answer:
        print("Correct!")
        another = input("Do you want another problem? ")
        if another == "y":
            get_numbers()
                
    if add_answer != answer:
        print("Incorrect. The answer is: ", answer)
        another = input("Do you want another problem? ")
        if another == "y":
            get_numbers()
 
     # ____________________________________________________________________ #
     
    def game():
    choices()
        
    # ____________________________________________________________________ #
        
def choices():
    
    computerchoice = random.randint(1, 5)
    
    weaponofchoice = input("Type your weapon of choice (rock, paper, scissors, lizard, spock): ")
    print("You chose....", weaponofchoice)
    
    if computerchoice == 1:
        print("The computer chose....rock")
    if computerchoice == 2:
        print("The computer chose....paper")
    if computerchoice == 3:
        print("The computer chose....scissors")
    if computerchoice == 4:
        print("The computer chose....lizard")
    if computerchoice == 5:
        print("The computer chose....spock")
    
    if weaponofchoice == "rock" and computerchoice == 1:
        print("It's a tie!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
            
    if weaponofchoice == "paper" and computerchoice == 2:
        print("It's a tie!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
            
    if weaponofchoice == "scissor" and computerchoice == 3:
        print("It's a tie!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
            
    if weaponofchoice == "lizard" and computerchoice == 4:
        print("It's a tie!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
            
    if weaponofchoice == "spock" and computerchoice == 5:
        print("It's a tie!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
            
    if weaponofchoice == "rock" and computerchoice == 2:
        print("The computer wins!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
            
    if weaponofchoice == "scissors" and computerchoice == 1:
        print("The computer wins!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
            
    if weaponofchoice == "scissors" and computerchoice == 1:
        print("The computer wins!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
                        
    if weaponofchoice == "rock" and computerchoice == 5:
        print("The computer wins!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
                        
    if weaponofchoice == "paper" and computerchoice == 3:
        print("The computer wins!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
            
                        
    if weaponofchoice == "paper" and computerchoice == 4:
        print("The computer wins!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
                        
    if weaponofchoice == "scissors" and computerchoice == 5:
        print("The computer wins!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
                        
    if weaponofchoice == "lizard" and computerchoice == 1:
        print("The computer wins!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
                        
    if weaponofchoice == "lizard" and computerchoice == 3:
        print("The computer wins!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
                        
    if weaponofchoice == "spock" and computerchoice == 4:
        print("The computer wins!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
            
                
    if weaponofchoice == "spock" and computerchoice == 2:
        print("The computer wins!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
            
    if weaponofchoice == "spock" and computerchoice == 1:
        print("You win!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
                        
    if weaponofchoice == "spock" and computerchoice == 3:
        print("You win!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
                
    if weaponofchoice == "lizard" and computerchoice == 5:
        print("You win!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
            
    if weaponofchoice == "lizard" and computerchoice == 2:
        print("You win!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
                 
    if weaponofchoice == "scissors" and computerchoice == 4:
        print("You win!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
            
                        
    if weaponofchoice == "paper" and computerchoice == 5:
        print("You win!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
               
    if weaponofchoice == "paper" and computerchoice == 1:
        print("You win!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
            
    if weaponofchoice == "rock" and computerchoice == 3:
        print("You win!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
                        
    if weaponofchoice == "rock" and computerchoice == 4:
        print("You win!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
                    
    if weaponofchoice == "scissors" and computerchoice == 2:
        print("You win!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
                 

    # ____________________________________________________________________ #
def drawSnowman():
    drawBase()
    drawMidSection()
    drawHead()
    drawArms()
    drawFace()
    drawPipe()
    
def drawBase():
    turtle.penup()
    turtle.goto(0, -200)
    turtle.pencolor('green')
    turtle.fillcolor('light green')
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(100)
    
    
    turtle.end_fill()
    
    # -------------------------------------------------------------------- #
    
def drawMidSection():
    turtle.penup()
    turtle.goto(0,-25)
    turtle.pencolor('green')
    turtle.fillcolor('light green')
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(75)
    
    turtle.end_fill()
    
    # -------------------------------------------------------------------- #

    
def drawHead():
    turtle.penup()
    turtle.goto(0,115)
    turtle.pencolor('green')
    turtle.fillcolor('light green')
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(50)
    
    turtle.end_fill()
    
    # -------------------------------------------------------------------- #
    
def drawArms():
    turtle.width(2)
    turtle.penup()
    turtle.goto(55,50)
    turtle.pencolor('brown')
    turtle.left(45)
    turtle.pendown()
    turtle.forward(75)
    turtle.left(25)
    turtle.forward(25)
    turtle.goto(108.03,103.03)
    turtle.right(50)
    turtle.forward(25)
    turtle.goto(108.03,103.03)
    turtle.right(75)
    turtle.forward(25)
    turtle.penup()
    turtle.left(180)
    turtle.goto(-55, 50)
    turtle.pendown()
    turtle.forward(75)
    turtle.left(25)
    turtle.forward(25)
    turtle.goto(-98.02,111.44)
    turtle.right(50)
    turtle.forward(25)
    turtle.goto(-98.02,111.44)
    turtle.right(75)
    turtle.forward(25)
    
def drawFace():
    turtle.penup()
    turtle.goto(-25,175)
    turtle.pencolor('dark green')
    turtle.fillcolor('dark green')
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(2)
    turtle.end_fill()
    
    turtle.penup()
    turtle.goto(25,175)
    turtle.pencolor('dark green')
    turtle.fillcolor('dark green')
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(2)
    turtle.end_fill()
    
    turtle.penup()
    turtle.right(25)
    turtle.pencolor('brown')
    turtle.goto(-15, 145)
    turtle.pendown()
    
    turtle.forward(30)
    
def drawPipe():
    turtle.penup()
    turtle.pendown()
    turtle.color('green')
    turtle.goto(15.00,145.00)
    turtle.left(25)
    turtle.width(5)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(5)
    turtle.right(90)
    turtle.forward(5)
    turtle.right(90)
    turtle.forward(5)
    turtle.hideturtle()
    
    turtle.width(3)
    turtle.right(100)
    turtle.color('grey')
    turtle.forward(24)
    turtle.circle(9)
    turtle.forward(24)
    turtle.circle(9)
    turtle.forward(24)
    turtle.circle(9)
    turtle.forward(29)
    
    turtle.showturtle()
    turtle.penup()
    turtle.goto(0,200)
    
    turtle.pencolor('dark green')
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor('dark green')
    turtle.right(15)
    turtle.forward(-50)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(15)
    turtle.end_fill()
    
    turtle.begin_fill()
    turtle.left(180)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(40)
    turtle.end_fill()
    
