import random

def isnumber(): #numberic program
    #isnumber accepts no arguments
    #isnumber checks whether or not an input is a number
    #isnumber prints "False" if it isn't and "True" if it is
    
    
    
    if string.isnumeric():
    #runs if its only numeric
        print("True")
    else:
    #runs if string.isnumeric deems in not just numerals
        print("False")

#---------------------------------------------------------------------------------------------#

def repitition_op():
    
    numbers = [1,2,3] * 3
    
    for num in numbers:
        print(numbers)
    
#---------------------------------------------------------------------------------------------#
    
def indexing():
    
    numbers = [5, 2, 7, 3, 9]
    
    len(numbers)
    print(numbers[0])
    print(numbers[4])
    print(numbers[5]) #crashes - list index out of range(4)
    print(numbers[-1])
    
    
        
#---------------------------------------------------------------------------------------------#        
        

def sales_list(): #Program 7-1
    #sales_list accepts no arguments
    #it creates a list NUM_DAYS long
    #and loops to accept input from the user
    #adding that input to the list
    
    NUM_DAYS = 5
    sales = [0] * NUM_DAYS
    index = 0
    
    
    print("Enter the sales for each day")
    
    while index < NUM_DAYS:
        print("Day #", index+1, end = '')
        value = input(":")
        sales[index] = float(input())
        
        index +=1
        
    print("Here are the values you entered:")
    for sale in sales:
        print(value)
        
#---------------------------------------------------------------------------------------------#
        
def concatenating_lists():
    list1 = [1, 2, 3, 4]
    list2 = [5, 6, 7, 8]
    list3 = list1 + list2
        
    print(list3)
    
    girls = ['Sue', 'Jane', 'Mary']
    boys = ['Joe', 'John', 'Sam']
    all_names = girls + boys
    
    print(all_names)
    
#---------------------------------------------------------------------------------------------#
    
def list_slicing():
    days = ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']
    
    mid_days = days[1:3]
    print(mid_days)
    
    weekends = days[4:6+1]
    print(weekends)
    
    weekends = days[4:6+1]
    

#---------------------------------------------------------------------------------------------#
    
def in_list(): #Program 7-2
    #in list accepts no arguments
    #it creates a list of part numbers
    #V45, V65, VF750, VFR1100, VTX1300
    #and prompts the user for a string to search for
    #and prints if the list contains the search string
    
    
    list = ['V45', 'V65', 'VF750', 'VFR1100', 'VTX1300']
    
    item = input("Enter a string to search for: ")
    if item in list:
        print("Part number", item, "was found in the list of part numbers.")
    else:
        print("Part was not found.")
        
#---------------------------------------------------------------------------------------------#
        
def list_append():#Program 7-3
    #list append accepts no arguments
    #it creates an empty list
    #and loops to append the list with input from the user
    #then prompts the continue
    
    namelist = []
    redo = 'y'
    
    name = input("Enter a name: ")
    namelist.append(name)
    cont = input("Add another name? (y to continue) ")
    if cont == 'y':
        list_append()
    else:
        for name in namelist:
            print(name)
        print(name)
        
#---------------------------------------------------------------------------------------------#
def list_index(): #Program 7-4
    #list index accepts no arguments
    #it creates alist of three food items
    #and prompts the user to replace one of the items
    #it searches the list for the index of the item
    #and prompts the user with a replacement food
    
    foods = ['Burger', 'Pizza', 'Hotdog']
    
    search = input("Enter the string to search for: ")
    
    try:
        if food.index(search) >=0:
            index = food.index(search)
            new_food = print("Item found. Enter a new food item: ")
            foods[index] = new_food
            
    except:
        print()
        print(search, "was not found in the list. Check your spelling and try again.")
        print("\nHere is the list: ", foods)
        
#---------------------------------------------------------------------------------------------#
    
def list_insert(): #Program 7-5
    #list_insert accepts no arguments
    #it prints the original list of three names
    #it inserts a name in a list of names
    #at a specific index and prints the new list
    
    name_list = ['Bruce', 'Steve', 'Tony']
    print("Here is the list before the insert method: ", name_list)
    
    name_list.insert(3, 'Sam')
    print("Here is the lest after the insert method: ", name_list)
    
#---------------------------------------------------------------------------------------------#
  
def list_sorting():
    
    jenny = [8, 6, 7, 5, 3, 0, 9]
    
    print(jenny)
    
    jenny.sort()
    
    print(jenny)
    
#---------------------------------------------------------------------------------------------#
    
def list_remove(): #Program 7-4
    #list index accepts no arguments
    #it creates alist of three food items
    #and prompts the user to remove one of the items
    #it removes the item from the list
    #or outputs a message if it doesn't exist
    
    foods = ['Burger', 'Pizza', 'Hotdog']
    
    search = input("Enter the string to search for: ")
    
    try:
        foods.remove(search)
        
        print("\nItem removed.\n")
        
    except:
        print()
        print(search, "was not found in the list. Check your spelling and try again.")
        print("\nHere is the list: ", foods)
        