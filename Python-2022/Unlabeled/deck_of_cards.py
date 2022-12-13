import random

counter = 0

def card_dealer_main(): #Program 9-1
    #card dealer main accepts no arguments
    #it calls create_deck to generate a deck of cards
    #and takes input from the user for the number of cards to deal
    #it then calls deal_cards to deal the number of cards to the user
    
    
    number = int(input("How many cards do you wish to deal? "))
    
    create_deck(number)
    
def create_deck(number):
    #create deck accepts no arguments
    #it generates a dictionary with the name of the card as the key
    #and the point calue of the card as the value
    #and returns the dictionary of cards
    
    deck_dictionary = {'Ace of Spades' : 1, '2 of Spades' : 2, '3 of Spades' : 3,
            '4 of Spades' : 4, '5 of Spades' : 5, '6 of Spades' : 6,
            '7 of Spades' : 7, '8 of Spades' : 8, '9 of Spades' : 9,
            '10 of Spades' : 10, 'Jack of Spades' : 10, 'Queen of Spades' : 10,
            'King of Spades' : 10,
            
            'Ace of Hearts' : 1, '2 of Hearts' : 2, '3 of Hearts' : 3,
            '4 of Hearts' : 4, '5 of Hearts' : 5, '6 of Hearts' : 6,
            '7 of Hearts' : 7, '8 of Hearts' : 8, '9 of Hearts' : 9,
            '10 of Hearts' : 10, 'Jack of Hearts' : 10, 'Queen of Hearts' : 10,
            'King of Hearts' : 10,
            
            'Ace of Clubs' : 1, '2 of Clubs' : 2, '3 of Clubs' : 3,
            '4 of Clubs' : 4, '5 of Clubs' : 5, '6 of Clubs' : 6,
            '7 of Clubs' : 7, '8 of Clubs' : 8, '9 of Clubs' : 9,
            '10 of Clubs' : 10, 'Jack of Clubs' : 10, 'Queen of Clubs' : 10,
            'King of Clubs' : 10,
            
            'Ace of Diamonds' : 1, '2 of Diamonds' : 2, '3 of Diamonds' : 3,
            '4 of Diamonds' : 4, '5 of Diamonds' : 5, '6 of Diamonds' : 6,
            '7 of Diamonds' : 7, '8 of Diamonds' : 8, '9 of Diamonds' : 9,
            '10 of Diamonds' : 10, 'Jack of Diamonds' : 10, 'Queen of Diamonds' : 10,
            'King of Diamonds' : 10}

    deal_cards(deck_dictionary, number)

def deal_cards(deck_dictionary, number):
    #deal cards accepts deck as a dictionary and number as an integer
    #it verifies number isn't reater than the deck size
    #if it is, it sets number to the length of the deck size to not
    #exceed the maximum index
    #it randomly selects and removes a key/value from the deck
    #it prints the card and calculates the value of the hand
    #after all cards have been dealt, it outputs the total value of the hand
    
    #deck_for = deck_dictionary.keys()
    
    #deck = []
    #you received the dictionary of cards
    #loop then number of times the user sspecified
    #randomly getting a card
    #and acculmulating the key value of that card
    #to get the total of the hand.
    
    deck = ''
    
    print("Here is your hand:\n")
    
    counter = 0
    while counter <= number:
    
        counter +=1
    
        card = random.choice(list(deck_dictionary))
        
        print(card)
        
        deck+=card
        
        value = deck_dictionary.pop(card)
        
        true_value = 0
        
        
    
    for key, value in deck_dictionary.items:
        
        true_value = true_value + value
        
    
    print("Your hand has has the value: ", value)
    
    