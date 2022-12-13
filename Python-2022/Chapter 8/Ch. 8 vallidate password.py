def validate_password(): #Programs 8-7
    #validate_password accepts no arguments
    #it prompts the user for a password
    #and passes the password to login.valid_password
    #to loop while the password is invalid
    
    password = input("Please enter your password: ")
    
    valid_password(password)
    
def valid_password(password): #Program 8-6
    #valid password accets a string for password
    #it tests the following conditions
    #is password at least 7 characters
    #does password have at least one uppercase letter
    #does password have at least one lowercase letter
    #does password have at least on digit (numeric)
    #if the passwrd meets all conditions is_valid is true
    #valid_password returns is_valid
    has_upper = False
    has_lower = False
    has_digit = False
    has_character = False
    
    for letter in password:
        if password.isalnum():
            has_digit = True
            if password.islower():
                has_lower = True
                if password.isupper():
                    has_upper = True
                    if password >= 6:
                        has_character = True
                        
    if has_upper is True and has_lower is True and has_digit is True and has_character is True:
        print("Password accepted.")
    
    else:
        print("The password you entered is not valid. Please try again.")
        validate_password()