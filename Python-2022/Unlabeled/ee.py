import random

#comments to explain your class
#more comments to explain your class

class CookieCutter:
    #a class should begin with the __init__() method
    #it receives two arguments for name and number
    
    #---------------Data Attributes-----------#
    def __init__(self, name, number):
        #the '(self)' is referring to itself
        #all of your intial attributes
        
        self.name = name
        self.number = number
        
    #---------------Data Attributes-----------#
    #change name changes the name attribute
    #change number changes the number attribute
    
    def change_name(self, name):
        self.name = name
        
    def change_number(self, number):
        self.number = number