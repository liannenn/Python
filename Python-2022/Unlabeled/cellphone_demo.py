import cellphone

def cellphone_demo1():
    
    valid = False
    try:
        manufact = input("Enter the phone manufacturer: ")
        modelnumb =  input("Enter the model number: ")
        retailprice =  input("Enter the retail price: ")
    except:
        cellphone_demo1()
    
        
    