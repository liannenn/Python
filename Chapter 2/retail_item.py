class RetailItem:
    def _init__(self, description, units, cost)
        self.__itemname = itemname
        self.__description = description
        self.__units = units
        self.__cost = cost
    
    def set_itemname(self, itemname):
        self.__itemname = itemname
    
    def set_description(self, description):
        self.__description = description
                             
    def set_units(self, units):
        self.__units = units
        
    def set_cost(self, cost):
        self.__cost = cost
        
    def get_itemname(self itemname):
        return self.__itemname 
   
    def get_description(self, description):
        return self.__description
     
    def get_units(self, units):
        return self.__units
        
    def get_cost(self, cost):
        return self.__cost
    
    def __str__(self):
        return "Description: " + self.__name + \
               "\nUnits: " + self.__phone + \
               "\nCost: " + self.__email
