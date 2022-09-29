import os

def file_write():
    
    outfile = open('lotr.txt', 'w')
    
    outfile.write('Frodo Baggins\n')
    outfile.write('Gandalf\n')
    outfile.write('Aragorn\n')
    
    outfile.close()
    
def file_read():
    
    infile = open('lotr.txt', 'r')
    file_contents = infile.read()
    
    infile.close()
    print(file_contents)
    
def read_line():
     
    infile = open('lotr.txt', 'r')
    
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    
    infile.close()
    
    print(line1)
    print(line2)
    print(line3)
    
def write_names():
    
    print("Please enter the name of three friends.")
    
    name1 = input("Friend 1: ")
    name2 = input("Friend 2: ")
    name3 = input("Friend 3: ")
    
    myfile = open("friends.txt", "a")
    
    myfile.write(name1 +'\n')
    myfile.write(name2 +'\n')
    myfile.write(name3 +'\n')
    
    myfile.close()
    
def string_newline():
    
    myfile = open("friends.txt", "r")
    
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    
    line1 = line1.rstrip('\n')
    line2 = line2.rstrip('\n')
    line3 = line3.rstrip('\n')
    
    infile.close()
    
    print(line1)
    print(line2)
    print(line3)
    
def write_numbers():
    
    print("Please enter the name of three friends.")
    
    numb1 = input("Please enter a number: ")
    numb2 = input("Please enter a number: ")
    numb3 = input("Please enter a number: ")
    
    myfile = open("numbers.txt", "w")
    
    myfile.write(str(numb1) +'\n')
    myfile.write(str(numb2) +'\n')
    myfile.write(str(numb3) +'\n')
    
    outfile.close()
    
    print()
    print("Your numbers have been written to numbers.txt")
    
def read_numbers():
    
    infile = open("numbers.txt", "r")
    
    
    num1 = int(infile.readline())
    num2 = int(infile.readline())
    num3 = int(infile.readline())
    
    infile.close()
    
    total = num1 + num2 + num3
    
    print("Here is your problem: ", num1, "+", num2, "+", num3, "=", total)
    
def write_sales():
    
    sales_file = open("sales.txt", 'w')
    counter = 1
    days = int(input("How many days do you want to enter sales for? "))
    while counter <= days:
        counter+=1
        sales = int(input("Enter the sales for day #", counter, ": "))
    
        sales_file.write(str(sales) + '\n')
    
        sales_file.close()
    
    print("All data has been saved to sales.txt.")
        
def read_sales():
    
    file = open("sales.txt", 'r')
    
    line = sales_file.readline()
    
    while line != '':
        amount = float(line)
        
        print(format(amount, ',.2f'))
        
        line = sales_file.readline()
        
    sales_file.close()
    
def write_video_times():
    
    counter=1
    
    amt = int(input("How many videos are in the project? "))
    
    file = open("video_txt.txt", "w")
    
    while counter <= amt:
        counter+=1
        time = int(input("Enter the time for video #", str(counter), ":"))
        vid_file.write(str(time) + '\n')
        
    print("All times have been writen to video_txt.txt.")
    
def read_video_times():
    
    file = open("video_txt.txt", "w")
    
    counter = 1
    total = 0
    
    for time in file:
        counter+=1
        run_time = time.rstrip('\n')
        print("Video #", counter, "time:", run_time)
        total += run_time
        
    print("The total running time of all videos is:", total, "seconds.")
    
def save_emp_records():
    
    file = open("employees.txt", "w")
    
    counter = 1
    amt = int(input("How many records do you want to enter? "))
    
    while counter <= amt:
        
        print("Enter data for employee #", counter, "\n")
        name = input("Name: ")
        id_numb = input("ID Number: ")
        department = input("Department: ")
        
        file.write(str(name) + '\n')
        file.write(str(id_numb) + '\n')
        file.write(str(department) + '\n')
        
        counter+=1
        
    print("All records were saved to employees.txt.")
    
    file.close()
    
def read_emp_records():
    
    file = open("employees.txt", "r")
    
    counter = 1
    total = 0
    
    for amt in file:
        counter+=1
        name = name.rstrip('\n')
        id_numb = id_numb.rstrip('\n')
        department = department.rstrip('\n')
        
        print("\nRecord for employee #", counter)
        print("Name: ", name)
        print("ID Number: ", id_numb)
        print("Department: ", department)
        
    print("\n", amt, "records retrieved.")
    
def write_coffee():
    #write_coffee accepts no arguments
    #it opens the ifle coffee.txt to append
    #it loops while the user wants to continue entering records
    #it prompts the user for the coffee description and number of pounds
    #the user should be prompted if they want to continue
    
    #prime the loop, open the file to append, display the header
    
    another = 'y'
    coffee_file = open("coffee.txt", "a")
    
    #loop to get the records
    while another.lower() == 'y':
        print("Enter the following coffee data:\n")
        desc = input("Description")
        pounds = input("Quantity (in pounds): ")
        
        #append the data to the file
        coffee_file.write(desc + '\n')
        coffee_file.write(pounds + '\n')
        
        #prompt for another entry
        another = input("\nDo you wish to enter another coffee? (y to continue): ")
        
        #close the file and output saved message
        coffee_file.close()
        print("\nAll data appended to coffee.txt.")

def read_coffee():
    #read_coffee accepts no arguments
    #it loops to read the records in coffee.txt
    #and outputs the description and pounds of coffee
    
    #open coffee.txt and read the first description
    
    coffee_file = open('coffee.txt', 'r')
    desc = coffee_file.readline()
    
    #loop the read, strip, and output each record
    while desc != '':
        pounds = coffee_file.readline()
        
        #strip the newline
        
        desc = desc.rstrip('\n')
        pounds = pounds.rstrip('\n')
        
        print("\nDescription:", desc)
        print("Quantity (in pounds):", pounds)
        
        #get the new description
        
        desc = coffee_file.readline()
        
        
    #close the file and output to the user
    coffee_file.close()
    print("\mAll records retreived.")
    
def search_coffee():
    #search coffee accepts no arguments
    #it searches coffee.txt for a string the user enters
    #if no record matches, it outputs a message to the user
    
    #boolean flag to determine search status
    found = False
    
    #get input from the user
    search = input("Enter a coffee description to search for: ")
    
    #open the file coffee.txt
    coffee_file = open('coffee.txt', 'r')
    
    #get the first description from the file
    desc= coffee_file.readline()
    
    #loop to read each line of the file
    while desc != '':
        pounds = coffee_file.readline()
    
    #strip the newline from the description
    desc = desc.rstrip('\n')
    
    if desc.lower() == search.lower(): #determine if the record is found and display the record
        print('\nRecord found!\n')
        print("Description:", desc)
        print("Quality (in pounds):", pounds)
        found = True #toggle the flag variable to true
        
    #get the next description
        desc = coffee_file.readline()
        
    coffee_file.close()
    
    if not found: #found = False
        print("\nThe record was not found.")
        
def modify_coffee(): #Program 6-18
    #modify coffee accepts no arguments
    #it imports the os module - this is needed to perform OS related file commands
    #it searched through the records and allows the user to modify the quantity
    
    #boolean flag variable
    found = False
    
    #Get the search description and new quanityt
    search = input("Enter the coffee description to modify: ")
    new_qty = input("Enter the new quantitity: ")
    
    #open the coffee.txt file to read and a new temporary file to write
    coffee_file = open('coffee.txt', 'r')
    temp_file = open('temp.txt', 'w')
    
    #read the first description
    desc = coffee_file.readline()
    
    while desc != '':
        qty = coffee_file.readline()
        
        #strop new line
        desc = desc.rstrip('\n')
        qty = qty.rstrip('\n')
        
        if search.lower() == desc.lower(): #coffee found
            #write the description and new quantity to the temp file
            temp_file.write(desc + '\n')
            temp_file.write(new_qty + '\n')
            
        #read the next description
            desc = coffee_file.readline()
 
     #all records have been processed, remove and rename files
            coffe_file.close()
            temp_file.close()
            
    #delete the original
    os.remove('coffee.txt')
    
    #rename the temp file to coffee.txt
    os.rename('temp.txt', 'coffee.txt')
    
    #description not found
    if found == False:
        print("\nRecord not found.")
    else:
        print("The quantity for", search,"has been updated to", new_qty, "pounds.")
        
def delete_rec():
   if search.lower() != desc.lower(): #coffee found
       #write the description and quantity to the temp file
       temp_file.write(desc + '\n')
       tempfile.write(qty + '\n')
       
   else:
        #toggle flag to true
        found = True
        
def exit_coffee():
    print("Thank you for using Caffeine Overload Inventory Control System.")
        
def coffee_shop(): #Program 6-16 - 6-19 modification
    #coffee shop accepts no arguments
    #it calls coffee_shop_menu to display a menu to the user
    #and calls each function according to the user input
    
    print("Welcome to Caffeine Overload Inventory Control System. Please choose an inventory option.")
    print("1) Add a record")  
    print("2) Modify a record")
    print("3) Delete a record")
    print("4) Display all saved records")
    print("5) Exit")
    option = input("Inventory option: ")
    
    if option == '1':
        write_coffee()
    if option == '2':
        modify_coffee()
    if option == '3':
        delete_rec()
    if option == '4':
        read_coffee()
    if option == '5':
        exit_coffee()
    else:
        print("Enter a valid input.")
        coffee_shop()
        
def division(): #Program 6-20
    #division accepts no arguments
    #it prompts the user for two integers
    #it divides num1/num2 and outputs the result
    
    #get input from the user
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a second number: "))
    
    #perform calculations and output
    result = num1 / num2
    
    print(num1, "divided by", num2, "is", result)
    
def division2():
    
    if num2 != 0:
        result = num1/num2
        print(num1, "divided by", num2, "is", result)
    else:
        print("Cannot divide by 0.")
        
def gross_pay1(): #Program 6-22
    #gross pay 1 accepts no arguments
    #it prompts the user for hours worked and hourly pay
    #it calculates the gross pay = hours * rate and outputs the result
    
    #get input from the user
    hours = int(input("Enter the number of hours worked: "))
    rate = float(input("Enter the pay rate: "))
    
    pay = hours * rate
    
    print("Gross pay: $", format(pay, ',.2f'), sep ='')
    

def gross_pay2():
    #gross pay 2 accepts no arguments
    #it prompts the user for hours worked and hourly pay
    #it calculates the gross pay = hours * rate and outputs the result
    
    #get input from the user
    
    
    try:
        hours = int(input("Enter the number of hours worked: "))
        rate = float(input("Enter the pay rate: "))
        pay = hours * rate
    
        print("Gross pay: $", format(pay, ',.2f'), sep ='')
    
    except ValueError as err:
        
        print('\n',err)
        print("Please enter numbers only.\n")
        print("----------------------------")
        print("\n")
        gross_pay2()
        
def display_file1(): #Program 6-24
    #display file 1 accepts no arguments
    #takes input from the user for a filename to open
    #and reads the contents of the file
    
    #get input from the user
    filename = input("enter filename to open: ")
    
    #open the file and read the contents
    infile = open(filename, 'r')
    contents = infile.read()
    
    #output and close the file
    print(contents)
    infile.close()
    
def display_file2(): #Program 6-25
    #display file 1 accepts no arguments
    #takes input from the user for a filename to open
    #and reads the contents of the file
    try:
    
        #get input from the user
        filename = input("Enter filename to open: ")
        
        #open the file and read the contents
        infile = open(filename, 'r')
        contents = infile.read()
        
        #output and close the file
        print(contents)
        infile.close()
     
    except IOError as IO:
        
        print("File does not exist. ")
        
def sales_report1():
    
    try:
        file = open("sales.txt", 'r')
        
        line = sales_file.readline()
        
        while line != '':
            amount = float(line)
            
            print(format(amount, ',.2f'))
            
            line = sales_file.readline()
            
        sales_file.close()
        
    except IOError:
        
        print("ERROR: An errror occurred trying to read the file.")
        
    except ValueError:
        
        print("ERROR: Non-numeric data found, calculations haulted.")
        
    except:
        print("ERROR: A problem has occurred.")
        
def salesreport2():
    try:
        file = open("sales.txt", 'r')
        
        line = sales_file.readline()
        
        while line != '':
            amount = float(line)
            
            line = sales_file.readline()
            
        sales_file.close()
        
    except IOError:
        
        print("ERROR: An errror occurred trying to read the file.")
        
    except ValueError:
        
        print("ERROR: Non-numeric data found, calculations haulted.")
        
    except:
        print("ERROR: A problem has occurred.")
        
    else:
        #output the data
        print(format(total, ',.2f'))