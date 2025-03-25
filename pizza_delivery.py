print("Welcome to pizza Delivery")
size = input("What is the size you want S/M/L\n").upper()
pepperoni = input("Do you want peperoni on your pizza?\n").upper()
extra_cheese = input("Do you want extra cheese\n").upper()
price = 0
if size == "S":
    print("Small size is $15")
    price += 15
    if pepperoni == "Y":
        price += 2

elif size == "M":
    print("Medium size is of 20$")
    price += 20
    if pepperoni == "Y":
        price += 3
elif size == "L":
    print("Large is of 25$")
    price += 25
    if pepperoni == "Y":
        price += 3
else:
    print("Invalid size selection. Please choose S, M, or L.")
    exit()  # Exit the program if input is invalid
if extra_cheese == "Y":
    price += 1

print(f"your final price is now {price}$")
