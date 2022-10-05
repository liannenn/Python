import random

def game():
    choices()
        
    # -------------------------------------------------------------------- #
        
def choices():
    
    computerchoice = random.randint(1, 5)
    
    weaponofchoice = input("Type your weapon of choice (rock, paper, scissors, lizard, spock): ")
    print("You chose....", weaponofchoice)
    
    if weaponofchoice ==  "rock":
        weaponofchoice1 == '1'
    
    if weaponofchoice ==  "paper":
        weaponofchoice1 == '2'
    
    if weaponofchoice ==  "scissors":
        weaponofchoice1 == '3'
    
    if weaponofchoice ==  "lizard":
        weaponofchoice1 == '4'
    
    if weaponofchoice ==  "spock":
        weaponofchoice1 == '5'
    
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
    
    if weaponofchoice == "rock" and computerchoice == "rock":
        print("It's a tie!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
            
    if weaponofchoice1 == "paper" and computerchoice == "paper":
        print("It's a tie!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
            
    if weaponofchoice1 == "scissor" and computerchoice == "scissor":
        print("It's a tie!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
            
    if weaponofchoice1 == "rock" and computerchoice == "rock":
        print("It's a tie!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
            
    if weaponofchoice1 == "lizard" and computerchoice == "lizard":
        print("It's a tie!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
            
    if weaponofchoice1 == "spock" and computerchoice == "spock":
        print("It's a tie!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
            
    if weaponofchoice1 == "rock" and computerchoice == "paper":
        print("The computer wins!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
            
    if weaponofchoice1 == "scissors" and computerchoice == "rock":
        print("The computer wins!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
            
    if weaponofchoice1 == "scissors" and computerchoice == "rock":
        print("The computer wins!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
                        
    if weaponofchoice1 == "rock" and computerchoice == "spock":
        print("The computer wins!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
                        
    if weaponofchoice1 == "paper" and computerchoice == "scissors":
        print("The computer wins!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
            
                        
    if weaponofchoice1 == "paper" and computerchoice == "lizard":
        print("The computer wins!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
                        
    if weaponofchoice1 == "scissors" and computerchoice == "spock":
        print("The computer wins!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
                        
    if weaponofchoice1 == "lizard" and computerchoice == "rock":
        print("The computer wins!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
                        
    if weaponofchoice1 == "lizard" and computerchoice == "scissors":
        print("The computer wins!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
                        
    if weaponofchoice1 == "spock" and computerchoice == "lizard":
        print("The computer wins!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
            
                
    if weaponofchoice1 == "spock" and computerchoice == "paper":
        print("The computer wins!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
            
    if weaponofchoice1 == "spock" and computerchoice == "rock":
        print("You win!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
                        
    if weaponofchoice1 == "spock" and computerchoice == "scissors":
        print("You win!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
                
    if weaponofchoice1 == "lizard" and computerchoice == "spock":
        print("You win!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
            
    if weaponofchoice1 == "lizard" and computerchoice == "paper":
        print("You win!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
                 
    if weaponofchoice == "scissors" and computerchoice == "lizard":
        print("You win!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
            
                        
    if weaponofchoice == "paper" and computerchoice == "spock":
        print("You win!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
               
    if weaponofchoice == "paper" and computerchoice == "rock":
        print("You win!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
            
    if weaponofchoice == "rock" and computerchoice == "scissors":
        print("You win!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
                        
    if weaponofchoice == "rock" and computerchoice == "lizard":
        print("You win!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()
                    
    if weaponofchoice == "scissors" and computerchoice == "paper":
        print("You win!")
        repeat = input("Play again? (y/n) ")
        if repeat == "y":
            choices()