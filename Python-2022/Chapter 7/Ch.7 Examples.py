import random
import matplotlib

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
     
#---------------------------------------------------------------------------------------------#
        
def usingindex():
    
    my_list = [1, 2, 3, 4, 5]
    
    del my_list[2]
    
    print(my_list)
    
    print("Lowest Value: ", min(my_list))
    
    print("Highest Value: ", max(my_list))
    
#---------------------------------------------------------------------------------------------#
    
def copyinglists():
    
    list1 = [1, 2, 3, 4]
    list2 = []
    
    for element in list1:
        list2.append(element)
    
    list2.append(5)
    
    print(list1)
    print(list2)
    
#---------------------------------------------------------------------------------------------#

def list_total(): #Program 7-8
    #list total accepts no arguments
    #it creates a list of numbers [2, 4, 6, 8, 10]
    #and loops to accumulate the total of all numbers
    #in the list
    
    total = 0
    
    numbers = [2, 4, 6, 8, 10]
    
    for num in numbers:
    
        total += num
        
    
    print("The sum of", numbers, "is: ", total)
        
#---------------------------------------------------------------------------------------------#

def list_avg(): #Program 7-9
    #list total accepts no arguments
    #it creates a list of numbers [2, 4, 6, 8, 10]
    #and loops to accumulate the total of all numbers
    #in the list
    
    total = 0
    
    numbers = [2, 4, 6, 8, 10]
    
    for num in numbers:
    
        total += num
        
        truetotal = total/len(numbers)
        
    
    print("The average of", numbers, "is: ", truetotal)
        
#---------------------------------------------------------------------------------------------#

def list_function(): # Program 7-10
    #list function accepts no arguments
    #it creates a list [2, 4, 6, 8, 10]
    #it passes the list to get_total
    #it prints the returned total
    
    list = [2, 4, 6, 8, 10]
    
def get_total(list):

    for num in numbers:

        total += num
    
    print("The total of", list, "is: ", total)
    
#---------------------------------------------------------------------------------------------#

def list_return(): #Program 7-11
    #list return accepts no arguments
    #it calls get_values to create a list reference
    #and outputs the numbers in the list
    
    list = []
    y = '1'
    
    while cont.lower() == 1:
    
        number = input("Input a number: ")
        cont = input("Do you want to enter another number? (y/n) ")
        
        list.append(number)
        
    print("You entered the numbers: ", list)
    
#---------------------------------------------------------------------------------------------#
    
def test_calc(): #Program 7-12
    #test calc accepts no arguments
    
    try:
        
        scores = get_scores()
        
        lowest = min(scores)
        
        print("Drops the lowest score of", lowest)
        
        scores.remove(lowest)
        
        total = get_total(scores)
        average_score = total / len(scores)
        
        print("\nThe average score, with", lowest, "dropped from the score, is", 
            format(average_score, ',.2f'))
        
    except Exception as err:
            print(err)
            
def get_scores():
    scores = []
    again = 'y'
        
    while again.lower() == 'y':
        try:
            score = float(input("Enter a score: "))
        except:
            print("Please enter a valid score.\n")
        else:
            scores.append(score)
                    
        again = input("Enter another score? (y/n:: ")
        print()
    return scores
        
#---------------------------------------------------------------------------------------------#

def list_writelines(): #Program 7-13
    #list writelines accepts no arguments
    #it writes the entire contents of a list
    #to the file cities.txt
    
    cities = ['Kansas City', 'Lawrence', 'Wichita', 'Manhattan']
            
    try:
        #open the file
        outfile = open('cities.txt', 'w')
        
        #write the list to the file
        outfile.writelines(cities)
        
        #close the file
        print("All data written to cities.txt")
        outfile.close()
        
    except Exception as err:
        print(err)
        
#---------------------------------------------------------------------------------------------#

def list_read(): #Program 7-15
    #list read accepts no arguments
    #it reads from cities.txt and aggregates the data
    #to the list cities, stripping the \n from each
    
    try:
        #open the file
        infile = open('cities.txt', 'r')
        
        #read the contents to a list
        cities = infile.readlines()
        
        #close the file
        infile.close()
        
    except:
        print("error reading from the file.")
        
    #initialize index
        index = 0
        
    #strip the newline and reassign it to the list
        while index < len(cities):
            cities[index] = citiex[index].rstrip('\n')
            index += 1
        print("Here is the information read from cities.txt.")
        print(cities)
        
#---------------------------------------------------------------------------------------------#

def list_write_numbers(): #Program 7-16
    #list write numbers accepts no arguments
    #it saves a list of integers [1, 2, 3, 4, 5, 6, 7]
    #to the file numerlist.txt
    
    #create the list
    numbers = [1, 2, 3, 4, 5, 6, 7]
    
    #open the file
    outfile = open('numberlist.txt', 'w')
    
    #loop to write the numbers to the list
    for number in numbers:
        outfile.write(str(number) + '\n')
    #close the fie
    outfile.close()
    print('All numbers saved to numberlist.txt')
    
        
#---------------------------------------------------------------------------------------------#

def list_read_numbers(): #Program 7-17
    #list read numbers accepts no arguments
    #it reads integers from the file numberslist.txt
    #and aggregates them to a list
    
    #initialize the aggregator
    numbers = []
    
    try:
        #open the file
        infile = open('numberlist.txt', 'r')
        
        #loop to add each number to the list
        for num in infile:
            numbers.append(int(num.rstrip('\n')))
            
        infile.close()
        
    except Exception as err:
        print(err)
    print('Here is the list created from numberlist.txt:')
    print(numbers)
         
#---------------------------------------------------------------------------------------------#

def random_numbers(): #Program 7-18 (import random at the top of your file)
    #random numbers accepts no arguments
    #it creates a 2D list with a maximum row index of 3
    #and a maximum column index of 2
    #it uses nested loops to fill the 2D list with a random number
    #from 1-100
    
    #constants for row/cols loops
    ROWS = 3
    COLS = 3
    
    values = [ [0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0] ]
    
    #loop to fille the list with random numbers
    for row in range(ROWS):
        for col in range(COLS): #for each row, fill all columns
            values[row][col] = random.randint(1,100)
            
    #output the list
            print(values)
                   
#---------------------------------------------------------------------------------------------#

