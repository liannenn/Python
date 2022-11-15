import random

#coin.py



class Coin:
    #a class should begin with the __init__() method
    #this method executes first, as an intitilaization fo the class
    #the (self) parameter is a generally accepted naming convention
    #for the paramter within a class, and is required
    
    #----------------------------Data Attributes-----------------------------#
    #initialize the data attribute with 'Heads' to indicate
    #the coin begins in a head's up position
    
    def _init_(self):
        self.__sideup = 'Heads'
    #----------------------------Instance Methods-----------------------------#
    #the toss method generates a random number in the range of 0 through 1
    #if the number is 0, sideup is assigned 'Heads'
    #if the number is 1, sideup is assigned 'Tails'
    
    def toss(self):
        if random.randint(0,1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'
    
    #get sideup method returns the current state of the coin
    #or the side that is facing up
            
    def get_sideup(self):
        
        return self.__sideup