#Class Dog
#Class Car

class Dog:
    #the Dog class accepts values for name, age, and the coat color
    #the str method prints the dog's vitals aka: the state of the object
    #the speak method prints what the dog "says"
    
    species = 'Canis familaris' #common nale for all dogs aka: all instances
    
    def __init__(self, name, age, coat):
        self.name = name #create an attribute for name for the object
        self.age = age #create an attribute for age for the object
        self.coat = coat #create an attribute for coat for the object
        
    #----------------------------Instance Methods-----------------------#
    
    def __str__(self):
        #str returns a string with the state of the object
        #displaying the name, age, and coat of the dog
        return f"{self.name} is {self.age} year old and has a {self.coat} coat color."
    
    def speak(self, sound):
        #speak accepts an argument for the string sound
        #and reutns a string with the dogs name and what it "says"
        return  f"{self.name} says {sound}!"
    
class Car:
    #the object of the car class has the attrivutes
    #year, make, model, color, mileage
    #str prints the vehicle's vitals
    #method add_miles to add miles to the car's total mileage
    
    #------------------------attributes------------------------#
    def __init__(self, year, make, model, color, mileage):
        self.year = year #assign the year attribute
        self.make = make #assign the make attribute
        self.model = model #assign the model attribute
        self.color = color #assign the color attribute
        self.mileage = mileage #assign the mileage attribute
        
    #------------------------instance methods------------------------#
        
    def __str__(self): #return a string with the vitals of the vehicle
        return f"The {self.year} {self.color} {self.make} {self.model} has {self.mileage} miles."
    
    def add_miles(self, miles):
        #add miles accepts a numeric value for miles
        #it adds the miles to the total mileage
        #and returns a message
        
        self.mileage = self.mileage + miles
        return f"The mileage for {self.year} {self.model} is now {self.mileage}."
    