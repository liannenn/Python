def count_t():
    #count_t accepts no arguments
    #it prompts the user for a word
    #and iterates through each letter
    #counting the number of upper and lower case t's
    #it outputs the total number of times it appeared in the word
    
    #gets word
    word = input("Please enter a word: ")
    #labels counter
    counter = 0 
    
    #sets a loop for the amount of letters in a word 
    for letter in word:
        #loops the amount of letters and checks whether or not they are the letter t or T
        if letter == 'T' or letter == 't':
        
            #adds to the counter if 2nd loop is true
            counter +=1
    
    #prints the amount of t or T at the end
    print("The letter T or t appears", counter, "times in the word: ", word)
    
def concatenate(): #Program 8-2
    #concatenate accepts no arguments
    #it concatenates and prints the trwo strings
    #Carmen and Sandiego
    name = "Carmen"
    print("Where in the world is ", name)
    name += 'Sandiego'
    print("Where in the world is ", name)
    

def string_test(): #Program 8-5
    #strings test accepts no arguments
 jmn   #it takes input from the user in the form of a string
    #and performs a variety of tests on the string
    
    #get input from the user
    user_string = input("Enter a string to evaluate: ")
    
    #perform string tests
    if user_string.isalnum():
        print("The string only contains alphanumeric characters.")
    if user_string.isdigit():
        print("The string only contains digits.")
    if user_string.isalpha():
        print("The string only contains alpha characters.")
    if user_string.isspace():
        print("The string only contains whitespaces.")
    if user_string.islower():
        print("The string is all lowercase.")
    if user_string.isupper():
        print("The string is all uppercase.")
        
    print()
    print("Your string converted to all uppercase is: ", user_string.upper())
    print("Your string converted to all lowercase is: ", user_string.lower())
    
