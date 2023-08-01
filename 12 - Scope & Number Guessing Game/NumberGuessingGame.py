import random
import os
import art

os.system('cls')
print(art.logo)

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")

attempts = 0
rand_number = random.randint(1, 100)
win = False

difficulty = input('Choose a difficulty. "easy" or "hard"? ').lower()

if difficulty == "easy":
    attempts += 10
elif difficulty == "hard":
    attempts += 5

while attempts:
    print(f"\nYou have {attempts} remaining.")
    guess = int(input("Make a guess: "))

    if guess == rand_number:
        attempts = 0
        win = True
    if guess < rand_number:
        attempts -= 1
        if attempts > 1: print("To Low, Try again")
    if guess > rand_number:
        attempts -= 1
        if attempts > 1: print("To High, Try Again")

if win:
    print("\n👏 Congratulations, you got it!")
else:
    print(f"\n😭 Better luck next time! Number was {rand_number}.")