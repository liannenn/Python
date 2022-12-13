#Program 10-2 - coin_demo1.py

import coin

def main():
    #coin main accepts no arguments
    #it uses the Coin class to create an object
    
    #create an object from the Coin class
    my_coin = coin.Coin()
    
    #display the side of the coin that is facing up
    
    print('This side is up: ', my_coin.get_sideup())
    
    #toss the coin
    print('Tossing the coin...')
    my_coin.toss()
    
    #display the side of the coin that is facing up
    print('This side is up: ', my_coin.get_sideup())
    
#call the function to flip the coin
main()