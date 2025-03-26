import random

user_response = input("Please choose 'H' for head and 'T' for tail\n")
print("Welcome to TOSS")
random_result = random.randint(0, 1)
if random_result == 0 and user_response == "H":
    print("its a head, you won the toss")
elif random_result == 1 and user_response == "T":
    print("its a tail, you won the toss")
else:
    print("you lost")
