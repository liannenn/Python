def get_average():
    #Assign a variable to the three test scores
    first_score = float(input('Enter the first test score:'))
    second_score = float(input('Enter the first test score:'))
    third_score = float(input('Enter the first test score:'))
    avg_score = (first_score + second_score + third_score)/3
    #Add up the scores and divide by 3
    
    #Output the avg
    print('The average score is : avg_score')
                        
def program2_17():
    number_of_seconds = float(input('Enter the number of seconds:'))
    hours = (number_of_seconds //3600)
    minutes = (number_of_seconds //60) % 60
    seconds = (number_of_seconds % 60)
    print('Here is the time in hours, minutes, and seconds:')
    print('Hours:', hours)
    print('Minutes:', minutes)
    print('Seconds:',seconds)
    
def program2_18():
    
     f = float(input('Enter the desired future value:')) #Get desired value
     r = float(input('Enter the annual interest rate:')) #Get annual interest rate
     n = float(input('Enter the number of years they money will grow:')) #Get amt of years
     p = float(input('You will need to deposit: ')) #Give amt needed to deposit
     answer = f / (1 + r)**n #Get answer
     print('You will need to deposit ', end='$')
     print (format(answer, ".2f")) #Print answer
     
def program2_22():
    numb1 = 127.90
    numb2 = 3465.15
    numb3 = 3.78
    numb4 = 264.82
    numb5 = 88.08
    numb6 = 800.00
    
    print(format(numb1, '7.2f'))
    print(format(numb2, '7.2f'))
    print(format(numb3, '7.2f'))
    print(format(numb4,'7.2f'))
    print(format(numb5, '7.2f'))
    print(format(numb6, '7.2f'))
    
     
     
    
    

    
     
     
    
    