print("Welcome to HANGMAN")
import random

words = [
    "python", "developer", "hangman", "challenge", "variable",
    "function", "keyboard", "monitor", "internet", "hardware",
    "software", "programming", "database", "algorithm", "debugging",
    "interface", "network", "protocol", "security", "firewall",
    "computer", "processor", "storage", "pythonista", "repository",
    "iteration", "recursion", "encryption", "framework", "automation"
]

random_word = random.choice(words)
print(random_word)  #For Debugging

lives = len(random_word)
spaces_to_fill = ["_"] * len(random_word)

print(" ".join(spaces_to_fill))

while "_" in spaces_to_fill and lives > 0:
    response = input("please guess a letter \n")
    if response in random_word:
        for index, letter in enumerate(random_word):
            if letter == response:
                spaces_to_fill[index] = response
    else:
        lives -= 1
        print(f"you have {lives} guesses left. ")

    print(" ".join(spaces_to_fill))


if "_" not in spaces_to_fill:
    print("\n🎉 Congratulations! You guessed the word!")
else:
    print(f"\nGame over! The word was: {random_word}")