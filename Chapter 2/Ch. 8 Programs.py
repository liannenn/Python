def sum_of_digits():
    #sum of digits accepts no arguments
    #it prompts the user for a string of numbers
    #it outputs the sum of numbers in the string
    
    #prime the total
    true_total = 0
    #prime the accumulator
    accumulator = 0
    
    
    try:
        
        #asks user for a string of single digit numbers
        numbers = input("Please enter a string of single digit numbers without spaces: ")
        
        for number in numbers:
            
            add = numbers[accumulator]
            add_numb = int(add)
            true_total += add_numb
            
            accumulator+=1
            
        print(true_total)
            
    except ValueError:
        sum_of_digits()
    except:
        sum_of_digits()
        
def date_converter():
    #date convert accepts no arguments
    #it prompts the user for  a date in the format mm/dd/yyyy
    #it outputs the date
    
    months_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']
    
    try:
        
        date = input("Enter a date in the format mm/dd/yyyy: ")
        
        date_split = date.split('/')
        
        month = date_split[0]
        
        month_int = int(month)
        
        final_month_int = (month_int - 1)
        
        final_month = months_order[final_month_int]
        
        day = date_split[1]
        year = date_split[2]
        
        print("The date is: ", final_month, day, year)
        
    except ValueError:
        
        date_converter
        
    except:
        
        date_converter
        
def morse_code():
    #morse code accepts no arguments
    #it converts the input given to morse code
    
    try:
        message = input("Enter a message to encode to morse code: ")
        
        alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I,' 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'X']
        
        letters = ['•-', '-•••', '-•-•', '-••', '•', '••-•', '--•', '••••', '••',
                   '•---', '-•-', '•-••', '--','-•', '---', '•--•', '--•-', '•-•',
                   '•••', '-', '••-', '•••-', '•--','-••-', '-•--', '--••']

        numbers = ['•----', '••---', '•••---', '••••-', '•••••', '-••••', '--•••',
                   '---••', '----•', '-----']
        
        
        