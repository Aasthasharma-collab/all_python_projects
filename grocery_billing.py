import time 

print("----welcome to the store----")

current_time = time.localtime()

if current_time.tm_hour >= 0 and current_time.tm_hour < 12:
    print("jai shaiya ram")
elif current_time.tm_hour >= 12 and current_time.tm_hour < 18:
    print("jai shaiya ram")
else :
    print("jai shaiya ram")

items = {
    "milk": 60,
    "bread": 40,
    "eggs": 90,
    "butter": 250,
    "cheese": 180,
    "rice": 80,
    "flour": 45,
    "sugar": 42,
    "apples": 120,
    "bananas": 50,
}

print("available items:")
for product, price in items.items():
    print(f"- {product}: ₹{price}")

user_choice = input("haji bolo: ").strip().lower()
selected_items = [item.strip() for item in user_choice.replace(",", " ").split()]

valid_items = []
for item in selected_items:
    if item in items:
        valid_items.append(item)
    else:
        print(f"{item}kone")

if not valid_items:
    print("abanu his khtm huyo , sham tk ahjajiyo")
else:
    item_quantities = {}
    for item in valid_items:
        try:
            qty = int(input(f"khatri for {item}: "))
            if qty > 0:
                item_quantities[item] = qty
            else:
                print(f"invalid quantity for {item}, skipping!")
        except ValueError:
            print(f"invalid quantity for {item}, skipping!")
    if item_quantities:
        name = input("naam bolo: ")
        print("recipt lelo")

        print("========================================")
        print(f"           {name.upper()}         ")
    print("           OFFICIAL RECEIPT                 ")
    print("========================================")

    subtotal = 0
    for item, qty in item_quantities.items():
        item_price = items[item]
        item_total = item_price * qty
        subtotal += item_total
        print(f"{item:<12}: @{item_price} x {qty} = ₹{item_total:.2f}")

    print("----------------------------------------")

    tax_rate = 0.08
    tax_amount = tax_rate * subtotal
    grand_total = subtotal + tax_amount
    print(f"subtotal = ₹{subtotal:.2f}")
    print(f"tax_amount = ₹{tax_amount:.2f}")
    print(f"grand_total = ₹{grand_total:.2f}")
    print("----------------------------------------")
    print("thank you for shopping")
