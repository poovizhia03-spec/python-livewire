import sys
import time
import qrcode
from inventory import view_medicines, add_medicine, update_medicine, remove_medicine
from billing import generate_bill, view_sales

def print_menu():
    print("\n" + "="*50)
    print("        💉✚ MEDICINE STORE MINI PROJECT ✚💉   ")
    print("="*50)
    print("1. 🩹 View Inventory")
    print("2. 💊 Add Medicine")
    print("3. 🔬 Update Medicine")
    print("4. ✖ Delete Medicine")
    print("5. 🗒 Generate Bill")
    print("6. 📆 View Sales History")
    print("7. 🏃 Exit")
    print("="*50)

def display_inventory():
    print("\n--- 💊Current Inventory 💊 ---")
    inventory = view_medicines()
    if not inventory:
        print(" No medicines found in the store.")
        return

    print(f"{'ID':<8} | {'Name':<15} | {'Price':<8} | {'Stock':<6} | {'Expiry'}")
    print("-" * 60)
    for med_id, details in inventory.items():
        print(f"{med_id:<8} | {details['name']:<15} | ${details['price']:<7.2f} | {details['stock']:<6} | {details['expiry_date']}")

def handle_add_medicine():
    print("\n---🛒 Add New Medicine 🛒 ---")
    name = input("Enter medicine name: ")
    try:
        price = float(input("Enter price: "))
        stock = int(input("Enter initial stock quantity: "))
    except ValueError:
        print("Error🥀: Price must be a number, and stock an integer.")
        return
        
    expiry = input("Enter expiry date (YYYY-MM-DD): ")
    
    med_id = add_medicine(name, price, stock, expiry)
    print(f"Success 💐! Medicine added with ID: {med_id}")

def handle_update_medicine():
    print("\n--- 📶Update Medicine📶 ---")
    display_inventory()
    med_id = input("Enter the ID of the medicine to update: ")
    
    print("Leave field empty to keep current value.")
    name = input("New name: ")
    price_str = input("New price: ")
    stock_str = input("New stock: ")
    expiry = input("New expiry date: ")
    
    price = None if not price_str else float(price_str)
    stock = None if not stock_str else int(stock_str)
    
    success = update_medicine(med_id, name=name if name else None, 
                              price=price, stock=stock, 
                              expiry_date=expiry if expiry else None)
    if success:
        print("Medicine updated successfully 💐💐💐.")
    else:
        print("Error🥀: Medicine ID not found.")

def handle_delete_medicine():
    print("\n--- ❌Delete Medicine❌ ---")
    display_inventory()
    med_id = input("Enter the ID of the medicine to delete: ")
    
    confirm = input(f"Are you sure you want to delete ID {med_id}? (y/n): ")
    if confirm.lower() == 'y':
        success = remove_medicine(med_id)
        if success:
            print("Medicine deleted successfully 💐💐💐.")
        else:
            print("Error🥀: Medicine ID not found.")
def handle_generate_bill():
    print("\n--- 📝Generate Bill📝 ---")
    inventory = view_medicines()
    display_inventory()
    
    items_to_buy = []
    while True:
        med_id = input("Enter Medicine ID to buy (or 'done' to finish): ").strip()
        if med_id.lower() == 'done':
            break
            
        try:
            qty = int(input(f"Enter quantity for {med_id}: "))
            items_to_buy.append({"med_id": med_id, "quantity": qty})
        except ValueError:
            print("Quantity must be an integer.")
            
    if not items_to_buy:
        print("No items added to bill. Cancelling.")
        return
    temp_total = sum(inventory[i["med_id"]]["price"] * i["quantity"] for i in items_to_buy)
    print(f"\nSub-Total: ${temp_total:.2f}")
    print("Select Payment: 1. Cash | 2. Card | 3. UPI")
    choice = input("Choice: ")
    methods = {"1": "Cash", "2": "Card", "3": "UPI"}
    payment_mode = methods.get(choice, "Cash")

    if payment_mode == "Cash":
        try:
            paid = float(input(f"Cash Received 💸(Min ₹{temp_total:.2f}): "))
            if paid < temp_total:
                print("Insufficient cash💸.");
                return
            print(f"Change to return: ₹{paid - temp_total:.2f}")
        except:
            return
    elif payment_mode == "Card":
        print("\nProcessing Card🗳...")
        time.sleep(2)
        print("[✔] Success!🎊")


        
    result = generate_bill(items_to_buy,payment_mode)
    
    if result["success"]:
        bill = result["bill"]
        print("\n" + "*"*30)
        print("          🗳BILL INVOICE")
        print("*"*30)
        print(f"Sale ID: {bill['sale_id']}")
        print(f"Date: {bill['timestamp']}")
        print("-" * 30)
        for item in bill['items']:
            print(f"{item['name']} x{item['quantity']} - ${item['subtotal']:.2f}")
        print("-" * 30)
        print(f"TOTAL: ${bill['total_cost']:.2f}")
        print("*"*30)
        

        if payment_mode == "UPI":
            my_upi_id = "poovikutty0@oksbi" 
            upi_url = f"upi://pay?pa={my_upi_id}&pn=PoovizhiStore&am={bill['total_cost']}&cu=INR"
            qr = qrcode.QRCode(version=1, box_size=1, border=2)
            qr.add_data(upi_url)
            qr.make(fit=True)
            qr.print_ascii(invert=True)
            print(f"UPI ID: {my_upi_id}")
        print("*"*40)


    else:
        print(f"\nFailed to generate bill: {result['error']}")

def handle_view_sales():
    print("\n--- 🩺Sales History🩺 ---")
    sales = view_sales()
    if not sales:
        print("No sales recorded yet.")
        return
        
    for sale in sales:
        print(f"[{sale['timestamp']}] Sale ID: {sale['sale_id']} - Total: ${sale['total_cost']:.2f}")

def main():
    while True:
        print_menu()
        choice = input("🫵 Enter your choice 🫵 (1-7): ")
        
        if choice == '1':
            display_inventory()
        elif choice == '2':
            handle_add_medicine()
        elif choice == '3':
            handle_update_medicine()
        elif choice == '4':
            handle_delete_medicine()
        elif choice == '5':
            handle_generate_bill()
        elif choice == '6':
            handle_view_sales()
        elif choice == '7':
            print("Exiting Medicine Store App. Goodbye🌿!")
            sys.exit(0)
        else:
            print("Invalid choice. Please select a number between 1 and 7.")

if __name__ == "__main__":
    main()






































