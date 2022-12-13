class CellPhone:
    
    def __init__(self):
        
        self.manufacturer = manufacturer
        self.modelnumb = modelnumb
        self.retailprice = float(retailprice)
        
    def set_manufactur(self):
        
        self.manufacturer = input("Enter the phone manufacturer: ")
        
        return f"Manufacturer updated to self{self.manufact}."
        
    def set_model(self):
        
        self.modelnumb = input("Enter the model number: ")
        
        return f"Model updated to {self.model}."
        
    def set_retail_price(self):
        
        self.retailprice = input("Enter the retail price: ")
        
        return f"Retail price updates to {self.price}."
        
    def get_manufact(self, manufacturer):
        
        return f"Phone Manufacturer: {self.manufact}"
        
    def get_model(self, modelnumb):
    
        
        return f"Model Number: {self.modelnumb}"
    
    def get_retail_price(self, retailprice):
        
        
        return f"Retail Price: {self.retailprice}"