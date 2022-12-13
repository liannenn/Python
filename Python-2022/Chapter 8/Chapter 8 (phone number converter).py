
def phone_number():
    
    message = input("Enter a telephone number in the form of XXX-XXX-XXXX: ").upper()
    
    message = message.split('-')
        
    
    
    
        
    converter_phone(message)
    


def converter_phone(message):
    

    phone_numb = []
    
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N','O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    phone_letters = ['2', '2', '2', '3', '3', '3', '4', '4', '4', '5', '5', '5', '6',
                     '6', '6', '7', '7', '7', '7', '8', '8', '8', '9', '9', '9', '9']
    
    for character in message:
        if character.isnumeric() == True:
            phone_numb.append(character)
    
    for character in message:
        for i in range(len(message)):
            for j in range(len(alphabet)):
                    phone_numb.append(phone_letters[j])
                    
    print(phone_numb)
                