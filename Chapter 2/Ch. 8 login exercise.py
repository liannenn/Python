def generate_login(): #Program 8-4
    #get login accepts no arguments
    #it prompts the uer for a first name, last name, and id number
    #it passes the values to login.get_login_name()
    #and receives the new user login
    
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    idnumber = input("Enter your id number: ")
    
    get_login_name(first, last, idnumber)

def get_login_name(first, last, idnumber): #Program 8-3
    #login accepts arguments for first, last, and idnumber
    #it creates separate substrings of the FIRST 3 letters of both
    #the first name and the last name and the LAST 3 characters of idnumber
    #it concatenates the strings in the order of first, last, id
    #and returns the newly generated login
    
    first_name = first[:3]
    last_name = last[:3]
    idnumber_name = idnumber[:3]
    
    print("Your system login name is: ",first_name,last_name,idnumber_name)
    
