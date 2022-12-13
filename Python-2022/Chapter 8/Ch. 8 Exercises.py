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
    #it takes input from the user in the form of a string
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
    
def rep_operator():
    text = 'z' * 5

    print(text)

    print('sleepy... ' + text * 3)
    
def repetition():
    #repetition accepts no arguments
    #it multiplies 'X' by range (1,10)
    #then multiples 'Z' by rang (8,0,-1)
    
    #print X range(1,10)-times in length
    for count in range(1,10):
        print('Z' * count)
        
    for count in range(8,0,-1):
        print('Z' * count)
        
def split_op():
    
    text = 'The quick brown fox jumps over the lazy dog'

    word_list = text.split()

    print(word_list)

    text2 = 'five>four>three>two>one'

    word_list = text2.split('>')

    print(word_list)

def string_split(): #Program 8-9
    #string split accepts no arguments
    #it splits the string one two three four
    #adding it to a list
    
    text2 = 'one>two>three>four'

    word_list = text2.split('>')

    print(word_list)
    
def split_date(): #Program 8-10
    #split date accepts no arguments
    #it createsa date string of 11/26/2018
    #and splits the date into mm dd yyyy
    
    date = '11/26/2018'
    word_list = date.split('/')
    
    print("Month: ", word_list[0])
    print("Day: ", word_list[1])
    print("Year: ", word_list[2])
    