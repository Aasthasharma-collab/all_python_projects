import random
import string

print("----secret language coding and decoding----")
user_message = input("enter your message: ")
user_choice = input("encode or decode?: ").strip().lower()

words = user_message.split()
new_words = []
if user_choice == "encode":
    for word in words:
        if len(word) >= 3:
            r1 = "".join(random.choices(string.ascii_lowercase, k=3))
            r2 = "".join(random.choices(string.ascii_lowercase, k=3))
            encoded_word = r1 + word[1:] + word[0] + r2
            new_words.append(encoded_word)
        else:
            new_words.append(word[::-1])
    result = " ".join(new_words)
    print(f"encoded word : {result} ")

elif user_choice == "decode":
    for word in words:
        if len(word) >= 3:
            stripped_word = word[3:-3]
            decoded_word = stripped_word[-1] + stripped_word[:-1]
            new_words.append(decoded_word)
        else:
            new_words.append(word[::-1])
    result = " ".join(new_words)
    print(f"decoded word: {result}")
else:
    print("inavlid option! please choose 'encode' or 'decode'".title())

