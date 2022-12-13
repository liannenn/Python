class CashRegister:
    # The __init__ method initializes the attributes.
    def __init__(self):
        self.itemlist = []

    def purchase_item(self, item):
        self.itemlist.append(item)
        
    def get_total(self, price):
        total = 0
        for item in itemlist:
            total += item.cost
        return total

    def show_items(self):
        for item in self.itemlist:
            print(item, end="\n\n")

    def clear(self):
        self.itemlist = []