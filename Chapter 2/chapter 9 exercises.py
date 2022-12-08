def unique_words():
    word_amt = 0
    word_unique = False
    
    infile = open('text.txt', 'r')
    
    complete_file = []
    
    for line in infile:
        
        line=infile.readline()
        
        complete_file.append(line)
        
    for line in complete_file:
        for word in line:
            word+=1
            if word > 2:
                word_unique == True
            if word < 2:
                word_unique == False
            if word_unique == True():
                print(word)
                