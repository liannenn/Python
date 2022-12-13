def line_numbers():
    
    try:
        infile = input("Insert file name: ")
    
        while line != '':
            
            line = infile.readline()
            file_contents = open(infile, "r")
            file_contents = infile.read()
            print(infile_contents)
            infile.close()
        
    except:
        
        print("[Errno 2] No such file or directory: '",infile,"'")    
      