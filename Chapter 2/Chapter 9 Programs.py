def file_encryption():
    
    counter = 0
    super_l33t_codes = {'A' : 'Q', 'S' : 'W', 'D' : 'E', 'F' : 'E', 'G' : 'T', 'H' : 'Y', 'J' : 'U', 'K' : 'I',
                        'L' : 'O','Q' : '1', 'W' : '2', 'E' : '3', 'R' : '4', 'T' : '5', 'Y' : '6', 'U': '7',
                        'I' : '8', 'O' : '9', 'P' : '0', 'Z' : 'A' , 'X' : 'S', 'C' : 'D', 'V' : 'F', 'B' : 'G',
                        'N' : 'H', 'M' : 'J', ',' : ':', '.' : ' " '}
    file = input("Input a file to open: ")
    
    infile = open(file, 'r')
    
    line = ''
    
    newmessage = ''
    
    for line in infile:
        print(line)
        #split line into a list
        #process through the list similar to below
        for letter in line:
            letterupper = letter.upper()
            newmessage += super_l33t_codes[letterupper]
            print(super_l33t_codes[letterupper])
            #counter +=1
            
        if 
    print("Your encrypted file is", newmessage)
            
    