import cash_register
import retail_item
import pickle

def ACME_main() :
    pass
Register = cash_register.CashRegister()
item = [retail_item.RetailItem("BOOGER", 43, 34.433), retail_item.RetailItem("BOOGjER", 439, 34.4393)]
Register.purchase_item(item[0])
Register.show_items()