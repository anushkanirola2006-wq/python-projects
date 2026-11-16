import random

print("Welcome to Anushka's Guessing Game!")

secret_number = random.randint(1, 10)
attempts = 0

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    attempts += 1

    if guess == secret_number:
        print("Congratulations! You won! ❤️")
        print("Your attempts:", attempts)
        break

    elif guess > secret_number:
        print("Too high! Try a smaller number.")

    else:
        print("Too low! Try a bigger number.")