import random
import os

os.system('cls') #clears terminal

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
combined = []

print("WELCOME TO THE PyPASSWORD GENERATOR!")

characters = int(input("Password length?\n"))
inc_letters = input("Would you like to include letters? Y or N?\n").lower()
inc_numbers = input("Would you like to include numbers? Y or N?\n").lower()
inc_symbols = input("Would you like to include symbols? Y or N?\n").lower()

if inc_letters == "y":
    combined.append(letters)

if inc_numbers == "y":
    combined.append(numbers)

if inc_symbols == "y":
    combined.append(symbols)

password = ""

for x in range(0, characters):
    rand_list_idx = random.randint(0, len(combined) - 1)
    cur_list_length = len(combined[rand_list_idx])
    rand_char_idx = random.randint(0, cur_list_length - 1)
    password += combined[rand_list_idx][rand_char_idx]

print(password)