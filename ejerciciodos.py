import os
import pandas as pd

_PRODUCT_DF = pd.DataFrame({
    "product_name": ["Chocolate", "Granizado", "Limon", "Dulce de Leche"],
    "quantity": [3, 10, 0, 5]
})

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def press_key():
    input("Press a key to continue...\n")
    clear_screen()

def get_current_stock(product_name):
    product = _PRODUCT_DF[_PRODUCT_DF['product_name'] == product_name]
    if product.empty:
        print("\nThe entered ice cream flavor is not available")
        press_key()
        return None
    else:
        return product['quantity'].iloc[0]

def is_product_available(product_name, quantity):
    current_stock = get_current_stock(product_name)
    if current_stock is not None:
        print("\nCurrent stock of ", product_name, "= ", current_stock)
        print("----------------------------------")
        if current_stock >= quantity:
            print("There is sufficient stock of ice cream available ", product_name, "\n")
            press_key()
            return True
        else: 
            print("\nThere is not enough stock of the ice cream entered :(\n")
            press_key()
            return False
    else:
        return False

def check_if_it_is_number(valor):
    if not valor.isdigit():
        print("\nYou must enter a number!!\n")
    else:
        return int(valor)

def input_product():
    i = True
    while i:
        print("\n_ Enter (1) to check stock availability of an ice cream flavor ")
        print("_ Enter (0) to exit the program")
        valor = input("\nEnter the numerical value: ")
        valor = check_if_it_is_number(valor)
        if valor == 1:
            product_name = input("\nEnter the name of the ice cream flavor to consult: ")
            quantity = input("Enter the requested quantity: ")
            quantity = check_if_it_is_number(quantity)
            if quantity != None:
                is_product_available(product_name, quantity)
        elif valor == 0:
            return i == False
        else:
            print("Please enter a value that is 0(zero) or 1(one)\n")
            press_key()
        

if input_product() == False:
    print("\n\nThank you for being part of Heladerías Frozen SRL, have a good day :D !!")
            
        
