import datetime
import uuid
import qrcode
import os
from data_manager import load_data, save_data
from inventory import get_inventory, save_inventory

SALES_FILE = "sales.json"

#  Load sales
def get_sales_history():
    return load_data(SALES_FILE, [])

#  Save sales
def save_sales_history(history):
    save_data(SALES_FILE, history)

#  Dynamic QR (with amount)
def generate_upi_qr(amount):
    upi_id = "poovikutty0@oksbi"
    name = "Poovizhi Store"

    upi_link = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu=INR"

    qr = qrcode.make(upi_link)
    filename = f"upi_qr_{uuid.uuid4().hex[:6]}.png"
    qr.save(filename)

    print(f"\n📱 QR Code generated: {filename}")
    print("👉 Scan using GPay / PhonePe / Paytm")

    

    return filename




#  Generate Bill
def generate_bill(items_to_buy, payment_method):
    inventory = get_inventory()
    bill_items = []
    total_cost = 0.0

    # ✅ Calculate bill
    for item in items_to_buy:
        med_id = item["med_id"]
        qty = item["quantity"]

        if med_id not in inventory:
            return {"success": False, "error": "Invalid Medicine ID"}

        medicine = inventory[med_id]

        if medicine["stock"] < qty:
            return {"success": False, "error": "Not enough stock"}

        cost = medicine["price"] * qty
        total_cost += cost

        bill_items.append({
            "name": medicine["name"],
            "quantity": qty,
            "subtotal": cost
        })

    # 💳 PAYMENT
    if payment_method == "UPI":
        generate_upi_qr(total_cost)
        
    elif payment_method == "Cash":
        try:
            paid = float(input(f"Total ₹{total_cost:.2f}. Enter cash: ₹"))
            if paid < total_cost:
                return {"success": False, "error": "Insufficient cash"}
            print(f"Balance: ₹{paid - total_cost:.2f}")
        except ValueError:
            return {"success": False, "error": "Invalid input"}

    else:
        return {"success": False, "error": "Invalid payment method"}

    # ✅ Update stock
    for item in items_to_buy:
        inventory[item["med_id"]]["stock"] -= item["quantity"]

    save_inventory(inventory)

    # 🧾 Save sale
    sale = {
        "sale_id": str(uuid.uuid4())[:8],
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "items": bill_items,
        "total_cost": total_cost,
        "payment_method": payment_method
    }

    history = get_sales_history()
    history.append(sale)
    save_sales_history(history)

    return {"success": True, "bill": sale}


# 🔹 View sales
def view_sales():
    return get_sales_history()
