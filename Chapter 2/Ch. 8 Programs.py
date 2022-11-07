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
        

def morse_code_main():
    message = input("Enter a message to encode to morse code: ").strip().upper()
    
    if message.isalnum() == True:
        message = morse_code(message)

    for i in range(len(message)):
        print(message[i], end=" ")
    print("")


def morse_code(message):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'X', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    morse_letters = ['•-', '-•••', '-•-•', '-••', '•', '••-•', '--•', '••••', '••', '•---', '-•-', '•-••', '--','-•', '---', '•--•', '--•-', '•-•', '•••', '-', '••-', '•••-', '•--','-••-', '-•--', '--••', '•----', '••---', '•••---', '••••-', '•••••', '-••••', '--•••','---••', '----•', '-----']
    
    morse = []

    for i in range(len(message)):
        for j in range(len(alphabet)):
            if message[i] == alphabet[j]:
                morse.append(morse_letters[j])

    return morse

def phone_number():
    
    message = input("Enter a telephone number in the form of XX-XXX-XXXX: ").strip('-').upper()
    
    if message.isalnum() == True:
        message = phone_number(message)

    for i in range(len(message)):
        print(message[i], end=" ")
    print("")


def morse_code(message):
    alphabet = ['A' 'B' 'C' 'D' 'E' 'F' 'G' 'H' 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    phone_letters = ['2', '2', '2', '3', '3', '3', '4', '4', '4', '5', '5', '5', '6', '6', '6', '7', '7', '7', '7', '8', '8', '8', '9', '9', '9', '9']
    
    phone_number = []

    for i in range(len(message)):
        for j in range(len(alphabet)):
            if message[i] == alphabet[j]:
                phone_numbers.append(phone_letters[j])

    return morse

def avg_num_words():
    
    infile = open('text.txt', 'r')
    
    complete_file = []
    
    for line in infile:
        
        line=infile.readline()
        
        complete_file.append(line)
        
def igpay_atinlay():
    
    convert = input("Enter a message to convert to pig Latin: ")
    
    for word in convert:
        
    
        
        
        
    print(file)
     