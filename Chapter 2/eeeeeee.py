import cellphone
import pickle

def main(): #Program 10-16
    #main receives no arguments
    #it opens a file called celphones.dat
    #and loops until the user enters a 'n' to continue
    #each iteraation of the loop the user is prompted
    #to enter phone data: manufacturer, model, and retail price (validated as a float)
    #an object is created using the CellPhone class in cellphone.py
    #with the attributes manufact, model, and retail_price
    #the object is pickled to the file cellphones.dat
    
    