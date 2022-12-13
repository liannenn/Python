class CashRegister:
<<<<<<< HEAD
    def purchase_item():
         
    
    def get_total():
    
    
    def show_cart():
    
    
    def empty():
        
=======

    # The __init__ method initializes the attributes.
    def __init__(self, purchase_item):
        self.__purchase_item = []

    def purchase_item(item, units):
        purchase_item.append(item)
        decrementInventory(units)

    def get_total(price):
        total += price
        return total

    def show_items(item_list):
        for item in item_list:
            print(item.get_item())
            print(item.get_units())
            print(item.get_price())
            print()

    def clear():
        purchase_list [:] = []
>>>>>>> fc8f360ad15486406a88677955be4c1949f125a9
