import time

current_time = time.localtime()

if current_time.tm_hour >= 0 and current_time.tm_hour < 12:
    print("Good morning")
elif current_time.tm_hour >= 12 and current_time.tm_hour < 18:
    print("Good afternoon")
else:
    print("Good evening")

print("put all your items here")
customer_name = input("your name: ")
tax_rate = 0.08
cart = [
    {"name": "pen", "price": 10, "qty": 2},
    {"name": "notebook", "price": 80, "qty": 3},
    {"name": "book", "price": 150.05, "qty": 7},
]


subtotal = 0
print("here is you receipt")
print("========================================")
print(f"           {customer_name.upper()}         ")
print("           OFFICIAL RECEIPT                 ")
print("========================================")
for item in cart:
    item_total = item["price"] * item["qty"]
    subtotal += item_total
    print(f"{item['name']:<12} @{item['price']:.2f} x{item['qty']} = ₹{item_total:.2f}")

print("----------------------------------------")
tax_amount = subtotal * tax_rate
grand_total = subtotal + tax_amount

print(f"{'subtotal:':<25} ₹{subtotal:.2f}")
print(f"{'tax_amount:':<25} ₹{tax_amount:.2f}")
print(f"{'grand_total:':<25} ₹{grand_total:.0f}")

print("----------------------------------------")
print("thank you for shopping from us")