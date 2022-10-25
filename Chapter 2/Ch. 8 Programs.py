def sum_of_digits():
    total = 0
    accumulator = 0
    
    try:
        
        numbers = input("Please enter a string of single digit numbers without spaces: ")
        
        for number in numbers:
            accumulator +=1
            numbers[accumulator]
            total+=accumulator
            
        print(total)