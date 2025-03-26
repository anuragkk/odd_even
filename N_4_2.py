
import random
print("Welcome to who will pay the bill\n")
names = ["Anurag", "Golu", "Mummy", "X", "Y", "Z"]
# print(len(names))
random_number = random.randint(0,5)
who_is_paying= names[random_number]
print(f"The person who will pay the bill today will be {who_is_paying}")
