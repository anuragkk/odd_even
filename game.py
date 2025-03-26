

import random

choices = ["Rock", "Paper", "Scissors"]

user_choice = input("What do you choose? Type Rock, Paper, or Scissors: ").capitalize()
if user_choice not in choices:
    print("Invalid choice. Please choose Rock, Paper, or Scissors.")
else:
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if (user_choice == "Rock" and computer_choice == "Scissors") or \
       (user_choice == "Paper" and computer_choice == "Rock") or \
       (user_choice == "Scissors" and computer_choice == "Paper"):
        print("You won!")
    elif user_choice == computer_choice:
        print("It's a draw!")
    else:
        print("You lost!")
