import random

print("Welcome to Rock, Paper, Scissors! ❤️")

while True:

    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)

    user = input("\nChoose rock, paper, or scissors: ").lower()

    print("Computer chose:", computer)

    if user not in choices:
        print("Invalid choice! Try again.")

    elif user == computer:
        print("It's a draw!")

    elif user == "rock" and computer == "scissors":
        print("You win! 🎉")

    elif user == "paper" and computer == "rock":
        print("You win! 🎉")

    elif user == "scissors" and computer == "paper":
        print("You win! 🎉")

    else:
        print("Computer wins! 😢")

    play_again = input("Do you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing! ❤️")
        break