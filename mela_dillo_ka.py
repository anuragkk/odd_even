print("Welcome to roller coaster ride")
height = int(input("What is your height\n"))
bill = 0
if height >= 120:
    print("you can ride the roller coaster ")
    age = int(input("What is your age?\n"))

    if 45 <= age <= 55:
        print("your ride is free of cost")
    elif age <= 12:
        print("Child ticket is $5 ")
        bill += 5
    elif 12 < age < 18:
        print("Teenage ticket is $7")
        bill += 7
    else:
        print("Adult ticket is $12")
        bill += 12

    wants_photo = input("Do you like to have a photo taken")
    if wants_photo == "y":
        bill += 3

    print(f"your final bill is {bill}$")

else:
    print("Sorry you are not eligible to ride")
