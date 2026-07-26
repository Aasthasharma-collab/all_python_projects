print("----amazon----".upper())
phone_tags = {"5g", "camera", "electronics", "latest", "phone"}
laptop_tags = {"electronics", "computer", "lenavo", "itel", "gaming", "work"}
accessory_tags = {"wireless", "charger", "cover", "phone holder"}
speaker_tags = {"speaker", "tv", "wireless"}
buds_tags = {"bluetooth", "wireless", "waterproof"}


user_search = input(" what are you looking for: ")

products = set(user_search.lower().split())

if products & phone_tags:
    print("Phones found")
if products & laptop_tags:
    print("Laptops found")
if products & accessory_tags:
    print("Accessories found")
if products & speaker_tags:
    print("Speakers found")
if products & buds_tags:
    print("Buds found")
    print("⚠️ Note: Buds are currently OUT OF STOCK!")
if not products & (phone_tags | laptop_tags | accessory_tags | speaker_tags | buds_tags):
    print("No matching products found")
