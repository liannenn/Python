import coin

def main():
    #main receives no arguments
    #it creates an object using the Coin class in coin.py
    #it outputs the current state of the object using the get_sideup method
    #then passes the object to flip(coin_obj) to flip the coin
    #finally it outputs the new state of the object using the get_sideup method
    coinn = coin.Coin()
    coinn.toss()
    print(f"Your coin is currently showing: {coinn.get_sideup()}")
    
    coinn.toss()
    print("\nTossing your coin...\n")
    
    print(f"Your coin is now showing: {coinn.get_sideup()}")
    