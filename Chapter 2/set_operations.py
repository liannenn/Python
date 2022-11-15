def set_operations():
    
    softball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])

    basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])
    
    print("The following students are on the softball team:" )
    
    for player in softball:
        print('\n', player, '\n')
    
    print("The folllowing students are on the basketball team: ")
    
    for player in basketball:
        print('\n', player, '\n')
    
    print("The following students play both baseball AND basketball: ")
    
    both = softball.intersection(basketball)
    for player in both:
        print(player)
        
    print("The following students play either baseball  or basketball: ")
    
    either = softball.union(basketball)
    
    for player in either:
        print(player)
    
    print("The following students play softball, BUT NOT basketball: ")
    
    difference_softball = softball.difference(basketball)

    
    for player in difference_softball:
        print(player)
    
    print("The following students play basketball, BUT NOT softball: ")
    
    
    difference_basketball = basketball.difference(softball)

    for player in basketball:
        print(player)
    
    
    print("The following students play one sport, but not both: ")
    