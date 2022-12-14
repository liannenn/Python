import verify as ver

class RetailItem:
        def __init__(self, description, stock, price):
        #retail item
        #has description, stock, price
        self.description = description
        self.stock = stock
        self.price = price

        
    def __list__(self):
        return [{self.description}, {self.stock}, {self.price}]
    
    def __str__(self):
        return f"{self.description}:{self.stock}:{self.price}"

class CashRegister:

       #cash register class
       #has empty, purchase item, total, and cart
       def __init__(self,retail_item):
        self.__items = []
    def empty(self):
        self.__items = []

    def purchase_item(self, retail_item):
        self.__items.append(retail_item)
        print("The item was added to the cash register.")

    def get_total(self):
        total = 0.0
        for item in self.__items:
            total = total + item.get_price()
            return total

    def show_cart(self):
        print("The items in the cash register are:")
        print()
        for item in self.__items:
            print(item)
            print()
    
def main():
       inventoryList = []
    
    try:
        infile = open("Inventory Data.txt", "r")
        line = infile.readline()
        while line != "" and line != "\n":
            formatted = line.rstrip('\n')
            split = formatted.split(":")
            inventoryList.append(formatted)
            line = infile.readline()
        infile.close()
    except IOError:
        print("No existing inventory found. Creating new list...")
    stop = False
    while stop == False:
        print("Welcome to the ACME Stock Menu. \n _____________________ \n 1) Manage Inventory \n 2) Manage Purchase \n 3) Exit") 
        menuChoice = ver.verifyIntRange("1-3: ", 1, 3)
        if menuChoice == 1:
            password = input("Input your password.")
            check = passwordCheck(password)
            if check == True:
                inventory(inventoryList)
            
        if menuChoice == 2:
            retailMenu(inventoryList)
            
        elif menuChoice == 3:
            stop = True
    
def inventory(inventoryList):
        stop = False
    
    while stop == False:
        print("\n Welcome to the Inventory Menu: \n\n _______________________________\n\n 1) Add to inventory \n 2) Display Inventory Data \n 3) Save inventory data \n 4) Leave menu\n")
        menuChoice = ver.verifyIntRange("1-4: ", 1, 4)
        
        if menuChoice == 1:
            inventoryList = addInventory(inventoryList)
        elif menuChoice == 2:
            print(inventoryList)
        elif menuChoice == 3:
            inventoryList = writeInventory(inventoryList)
        elif menuChoice == 4:
            print("Goodbye, thank you for using Inventory Menu!")
            stop = True

def addInventory(inventoryList):
    discription = input("Input item description: ")
    stock = ver.verifyIntMin("Input amount in stock: ", 1)
    price = ver.verifyFloatMin("Input item price: ", .01)
    

    item = RetailItem(discription, stock, price)
    itemString = item.__str__()

    inventoryList.append(itemString)

    return inventoryList

def writeInventory(inventoryList):
        infile = open("Inventory Data.txt", "w")
    while len(inventoryList) > 0:
        item = str(inventoryList.pop(0))+"\n"
        infile.write(item)

def retailMenu(inventoryList):
       cart = list([])
    stop = False
    while stop == False:
        print("\n Welcome to the the Retail Menu: \n _________________________ \n 1) Display Cart \n 2) Shop \n 3) Clear Cart \n 4) Check-Out")
        menuChoice = ver.verifyIntRange("1 - 4: ", 1, 4)
        if menuChoice == 1:
            print(cart)
        elif menuChoice == 2:
            cart = shop(inventoryList, cart)
        elif menuChoice == 3:
            cart.clear()
            print("Your cart is now empty!")
        elif menuChoice == 4:
            priceCalculator(cart)
            stop = True
    
def shop(inventoryList, cart):
    itemStock = dict({})
    itemPrices = dict({})
    items = list([])
    stop = False
    while stop == False:
        inventoryList = list([])
        infile = open("Inventory Data.txt", "r")
        line = infile.readline()
        while line != "" and line != "\n":
            formatted = line.rstrip('\n')
            split = formatted.split(":")
            inventoryList.append(formatted)
            line = infile.readline()
        infile.close()
        
        copyList = inventoryList.copy()
        while len(copyList) > 0:
            selection = copyList.pop(0)
            listed = selection.split(":")
            itemName = listed[0]
            itemStock[itemName]  = int(listed[1])
            itemPrices[itemName] = float(listed[2])
            items.append(itemName)
            print(itemName, " has ", itemStock[itemName], " units in stock, and each unit costs $", format(itemPrices[itemName], ".2f"), sep = "")
        
        
        userChoice = input("Which of these items would you like to purchase? ")
        if userChoice in items:
            
            quantity = ver.verifyIntRange("How many would you like? ", 1, itemStock[userChoice])
            price = quantity*itemPrices[userChoice]
            searchQue = userChoice + ":" + str(itemStock[userChoice]) + ":" + str(itemPrices[userChoice])
            originalItem = inventoryList.index(searchQue)
            text = userChoice+":"+str(quantity)+":" + str(price)
            cart.append(text)
            itemStock[userChoice] = itemStock[userChoice] - quantity
        if itemStock[userChoice] == 0:
            inventoryList.remove(searchQue)
        else:
            originalSplit = inventoryList[originalItem].split(":")
            originalSplit[1] = itemStock[userChoice]
            newData = originalSplit[0]+":"+str(originalSplit[1])+":"+originalSplit[2]
            inventoryList[originalItem] = newData
        my_reg = CashRegister(userChoice)
        my_reg.purchase_item(userChoice)
        writeInventory(inventoryList)
        stop = ver.quit()
    print(cart)
    return cart

def priceCalculator(cart):
    totalPrice = 0
    while len(cart) > 0:
        item = cart.pop(0)
        data = item.split(":")
        itemPrice = int(data[1])*float(data[2])
        totalPrice += itemPrice
    print("The total price is: $", totalPrice, sep = "")
    
def passwordCheck(password):
     if password == #put your own custom password here as a string:
        return True
    else:
        return False

