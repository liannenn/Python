class RetailItem:
    def __init__(self, description, units, cost) :
        self.description = description
        self.units = units
        self.cost = cost
    
    def __str__(self):
        return "Description: " + str(self.description) + \
               "\nUnits: " + str(self.units) + \
               "\nCost: " + str(self.cost)
