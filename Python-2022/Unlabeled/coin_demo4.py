#coin_demo4.py

import coin

def main():
    #main accepts no arguments
    #it creates an object my_coin using the Coin class in coin.py
    #it uses the get_sideup() method in the Coin class to display the starting state
    #it loops the 10 times, tossing the coin with the toss() method
    #and displaying the side again with the get_sideup() method
    
    counter = 1
    
    my_coin = coin.Coin()
    
    
    while counter <= 10:
    
        my_coin.toss()
        print('Toss', counter, ': ', my_coin.get_sideup())
        counter+=1