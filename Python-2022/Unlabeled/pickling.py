import pickle

def read_main():
    
    end_of_file = False
    
    infile = open('info.dat', 'rb')
    
    while not end_of_file:
        try:
            person = pickle.load(infile)
            display_data(person)
            
        except EOFError:
            end_of_file = True
        
def display_data(person):
    print('Name: ', person['name'])
    print('Age: ', person['age'])
    print('Weight: ', person['weight'])
    print()
    
def save_data(file):
    
    person = {}
    
    person['name'] = input('Name: ')
    person['age'] = int(input('Age: '))
    person['weight'] = float(input('Weight: '))
    
    picke.dump(person, file)