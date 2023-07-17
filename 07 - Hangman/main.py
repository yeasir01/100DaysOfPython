import random
import word_list
import art
import os

os.system('cls') #clears terminal

random_word = random.choice(word_list.list)
word_length = len(random_word)
display = []

end_of_game = False
lives = 6

#Populate blanks
for x in random_word:
    display.append("_")

print(art.logo)
print(art.stages[lives])

def populate_display(guess):
    for position in range(word_length):
        letter = random_word[position]

        if letter == guess:
            display[position] = letter

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if (guess in display):
        print(f"You've already guessed {guess}, try again.")
    else:
        if (guess in random_word):
           populate_display(guess)

           if not "_" in display:
               end_of_game = True
               print("Congratulation you won!")
        else:
            lives -= 1
            print(f'"{guess}" is not in the word, you lose a turn.')
            if (lives == 0):
                end_of_game = True
                print("You Lost, Better Luck Next Time!")

    print(art.stages[lives])
    print(f"Word: {''.join(display)}                  Turns: {lives}\n")