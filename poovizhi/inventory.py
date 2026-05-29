#import uuid
from data_manager import load_data, save_data

MEDICINES_FILE = "medicines.json"

def get_inventory():
    return load_data(MEDICINES_FILE, {})

def save_inventory(inventory):
    save_data(MEDICINES_FILE, inventory)

def add_medicine(name, price, stock, expiry_date):
    inventory = get_inventory()
    med_id = str(len(inventory) + 1)
    print("Generated ID:", med_id)   
    inventory[med_id] = {
        "name": name, 
        "price": float(price), 
        "stock": int(stock), 
        "expiry_date": expiry_date
    }
    save_inventory(inventory)
    return med_id

def view_medicines():
    return get_inventory()

def update_medicine(med_id, name=None, price=None, stock=None, expiry_date=None):
    inventory = get_inventory()
    if med_id not in inventory:
        return False
    if name:
        inventory[med_id]["name"] = name
    if price is not None:
        inventory[med_id]["price"] = float(price)
    if stock is not None:
        inventory[med_id]["stock"] = int(stock)
    if expiry_date:
        inventory[med_id]["expiry_date"] = expiry_date
    save_inventory(inventory)
    return True

def remove_medicine(med_id):
    inventory = get_inventory()
    if med_id in inventory:
        del inventory[med_id]
        save_inventory(inventory)
        return True
    return False
