import random

secret_number = random.randint(1, 100)
print("----random number guessing game----")
print("I have selected a number between 1 and 100. Try to guess it!")
print("You have 5 attempts to guess the correct number.")
user_input = int(input("Enter your guess: "))
if user_input != secret_number:
    for attempt in range(1, 5):
        user_input = int(input(f"Attempt {attempt + 1}: Enter your guess: \n"))
        if user_input == secret_number:
            print("Congratulations! You guessed the correct number.")
            break
        elif user_input < secret_number:
            print("Too low! Try guessing a higher number.")
        else:
            print("Too high! Try guessing a lower number.")
    else:
        print(f"Sorry, you've used all attempts. The correct number was {secret_number}.")

import random
print()
print("----random number guessing game----\n")
print("I have selected 5 random numbers between 1 and 20. Try to guess one of them!")
number = [random.randint(1, 20) for _ in range(5)]
for attempt in range(1, 11):
    user_input = int(input(f"Attempt {attempt}: Enter your guess (1-20): "))

    if user_input in number:
        number.remove(user_input)
        print(
            f"Congratulations! You guessed {user_input}. Remaining numbers to"
            f" guess: {len(number)}\n"
        )
        if len(number) == 0:
            print("You won! You found all 5 numbers!")
            break
    elif user_input < min(number):
        print("Too low! Try guessing a higher number.")
    elif user_input > max(number):
        print("Too high! Try guessing a lower number.")
    else:
        print("Incorrect guess! Try again.")    
else:
    print("you have run out of attempts. The correct numbers were: ", number)
    print("Game Over!")