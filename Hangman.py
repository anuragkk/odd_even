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
# print(random_word)  # Uncomment for debugging

lives = len(random_word)
spaces_to_fill = ["_"] * len(random_word)
guessed_letters = set()

print(" ".join(spaces_to_fill))

while "_" in spaces_to_fill and lives > 0:
    response = input("Please guess a letter: ").lower()

    # Validate input
    if len(response) != 1 or not response.isalpha():
        print("❌ Invalid input! Please enter a single letter.")
        continue

    if response in guessed_letters:
        print(f"⚠️ You've already guessed '{response}'. Try another letter.")
        continue

    guessed_letters.add(response)

    if response in random_word:
        for i in range(len(random_word)):  # Loop using range instead of enumerate
            if random_word[i] == response:
                spaces_to_fill[i] = response
    else:
        lives -= 1
        print(f"❌ Wrong guess! You have {lives} guesses left.")

    print(" ".join(spaces_to_fill))

if "_" not in spaces_to_fill:
    print("\n🎉 Congratulations! You guessed the word!")
else:
    print(f"\n💀 Game over! The word was: {random_word}")
