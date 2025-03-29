import random

print("Welcome to HANGMAN")

# Word bank
words = [
    "python", "developer", "hangman", "challenge", "variable",
    "function", "keyboard", "monitor", "internet", "hardware",
    "software", "programming", "database", "algorithm", "debugging",
    "interface", "network", "protocol", "security", "firewall",
    "computer", "processor", "storage", "pythonista", "repository",
    "iteration", "recursion", "encryption", "framework", "automation"
]

# Choose a random word
random_word = random.choice(words)
lives = len(random_word)  # Default lives based on word length
spaces_to_fill = ["_"] * len(random_word)  # Hidden word representation
guessed_letters = set()

# Select difficulty level
level_selected = input("Please choose your level (easy/medium/hard): ").lower()

if level_selected == "easy":
    spaces_to_fill[0] = random_word[0]  # Reveal first letter
    spaces_to_fill[-1] = random_word[-1]  # Reveal last letter
    lives += 2  # Extra lives for easy mode

elif level_selected == "medium":
    random_index = random.randint(1, len(random_word) - 2)  # Pick a random position (not first or last)
    spaces_to_fill[random_index] = random_word[random_index]  # Auto-fill one random letter

elif level_selected == "hard":
    lives -= 2  # Reduce lives for hard mode

print("\n" + " ".join(spaces_to_fill))

# Game loop
while "_" in spaces_to_fill and lives > 0:
    response = input("\nPlease guess a letter: ").lower()

    # Validate input
    if len(response) != 1 or not response.isalpha():
        print("❌ Invalid input! Please enter a single letter.")
        continue

    if response in guessed_letters:
        print(f"⚠️ You've already guessed '{response}'. Try another letter.")
        continue

    guessed_letters.add(response)

    # Check if guessed letter is in the word
    if response in random_word:
        for i in range(len(random_word)):
            if random_word[i] == response:
                spaces_to_fill[i] = response
    else:
        lives -= 1
        print(f"❌ Wrong guess! You have {lives} guesses left.")

    print(" ".join(spaces_to_fill))

# Check game outcome
if "_" not in spaces_to_fill:
    print("\n🎉 Congratulations! You guessed the word!")
else:
    print(f"\n💀 Game over! The word was: {random_word}")
