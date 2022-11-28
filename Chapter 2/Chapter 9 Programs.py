def file_encryption():
    
    counter = 0
    super_l33t_codes = {'A' : 'Q', 'S' : 'W', 'D' : 'E', 'F' : 'E', 'G' : 'T', 'H' : 'Y', 'J' : 'U', 'K' : 'I',
                        'L' : 'O','Q' : '1', 'W' : '2', 'E' : '3', 'R' : '4', 'T' : '5', 'Y' : '6', 'U': '7',
                        'I' : '8', 'O' : '9', 'P' : '0', 'Z' : 'A' , 'X' : 'S', 'C' : 'D', 'V' : 'F', 'B' : 'G',
                        'N' : 'H', 'M' : 'J', ',' : ':', '.' : ' " ', " " : " ", "\n" : ""}
    file = input("Input a file to open: ")
    
    infile = open(file, 'r')
    
    line = ''
    
    newmessage = ''

    
    for line in infile:
        #split line into a list
        #process through the list similar to below
        for letter in line:
            letterupper = letter.upper()
            newmessage += super_l33t_codes[letterupper]
           
            #counter +=1
            
    print("Your encrypted file is:", newmessage)
    
def file_decryption():
    
     super_l33t_codes = {'Q' : 'A', 'W' : 'S', 'E' : 'D', 'E' : 'F', 'T' : 'G', 'Y' : 'H', 'U' : 'J', 'I' : 'K',
                        'O' : 'L', '1' : 'Q', '2' : 'W', '3' : 'E', '4' : 'R', '5' : 'T', '6' : 'Y', 'U': '7',
                        'I' : '8', 'O' : '9', 'P' : '0', 'Z' : 'A' , 'X' : 'S', 'C' : 'D', 'V' : 'F', 'B' : 'G',
                        'N' : 'H', 'M' : 'J', ',' : ':', '.' : ' " ', " " : " ", "\n" : ""}
    
    
    