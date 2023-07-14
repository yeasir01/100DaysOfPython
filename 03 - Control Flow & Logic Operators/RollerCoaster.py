#Nested if else statements

height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))

    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12.")
    
    wants_photo = input("Would you like to add a photo for $3? Y or N. ")

    if wants_photo == "Y":
        bill += 3
        print(f"Your total is ${bill}")
    else:
        print(f"Your total is ${bill}")
else:
    print("Sorry, you have to be a bit taller to ride.")