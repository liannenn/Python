manufact = input("Enter a phone manufacturer: ")
model = input("Enter a phone model: ")
price = input("Enter a price: ")

while not valid:
    try:
        price = float(price)
        valid = True
    except:
        valid = False
        print("Be a try hard. Try again")
print("You have a", manufact, "model", model, "that retails for", price, ".")