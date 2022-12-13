#coin_demo5
import coin

def coin_demo5():
    #main accepts no arguments
    #it creates an object my_coin using the Coin class in coin.py
    #it uses the get_sideup() method in the Coin class to display the starting state
    #it loops the 10 times, tossing the coin with the toss() method
    #and displaying the side again with the get_sideup() method
    
    counter = 1
    
    
    my_coin1 = coin.Coin()
    
    my_coin3 = coin.Coin()
    
    my_coin3 = coin.Coin()
    
    
    print("Here are your coins after tossing them...")
    
    while counter <= 3:
    
        my_coin1.toss()
        my_coin2.toss()
        my_coin3.toss()
        
        print('Toss', counter, ': ', my_coin1.get_sideup())
        print('Toss', counter, ': ', my_coin2.get_sideup())
        print('Toss', counter, ': ', my_coin3.get_sideup())
        counter+=1
    