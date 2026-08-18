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
