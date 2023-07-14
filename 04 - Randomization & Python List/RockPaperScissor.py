import random
import os

os.system('cls') #clears terminal

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images = [rock, paper, scissors]

print("***************** WELCOME TO RPS, LETS PLAY! *****************")
computers_choice = random.randint(0, 2)
users_choice = int(input('Please make a selection? Rock: "0", Paper: "1", Scissors: "2"? '))

if users_choice != 0 and users_choice != 1 and users_choice != 2:
    print("You've made an invalid selection. Game Over!")
else:
    print("Computer:", images[computers_choice])
    print("You:", images[users_choice])

    if computers_choice == users_choice:
        print("It's a Draw!")
    elif users_choice == 0 and computers_choice == 2:
        print("You Win!")
    elif users_choice == 1 and computers_choice == 0:
        print("You Win!")
    elif users_choice == 2 and computers_choice == 1:
        print("You Win!")
    else:
        print("You lose!")
