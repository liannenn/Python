def birthday_main():
    birthdays = dict()
    
    choice = 0
    
    birthdays = {}
    
    get_menu_choice()

def get_menu_choice():
    
    print("Friends and their birthdays\n--------------------------------")
    print("1. Lookup a birthday.\n2. Add a new birthday. \n3. Change a birthday. \n4. Delete a birthday. \n5. Quit")
    
    try:
    
        choice = int(input("Enter your menu choice: "))
        
        if choice == '1':
            
            look_up(birthdays)
            
        if choice == '2':
            
            add_bday(birthdays)
            
        if choice == '3':
            
            change_bday(birthdays)
            
        if choice == '4':
                
            delete_bday(birthdays)    
                
        if choice == '5':
        
            print(" ")
        
    except:
        
    get_menu_choice():
        
def look_up(birthdays):
    
    name = input("Enter a name to enter: ")
    
    if len(birthdays) < 1:
        print("There are no birthdays to search!")
        
    else:
        
        print("Birthday for",  name, ":" birthdays.get[name, 'Entry not found.'])
        
def add_bday(birthdays):
    
    name = input("Enter a name")
    
def change_bday(birthdays):
    
def delete_bday(birthdays):

