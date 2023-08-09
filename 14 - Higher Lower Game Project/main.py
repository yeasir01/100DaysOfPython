#import art and game data
from game_data import data
import random
import art
import os

def play():
    os.system('cls')
    print(art.logo)
    
    score = 0

    guess_a = random.choice(data)
    guess_b = random.choice(data)

    keep_playing = True

    def formatted(data):
        return f"{data['name']}, a {data['description']}, from {data['country']}"

    while keep_playing:
        print("A:",formatted(guess_a))
        print("B:", formatted(guess_b))
        
        user_input = input('Who has more followers? "A" or "B": ').lower()
        
        is_correct = None

        if user_input == "a":
            is_correct = guess_a["follower_count"] > guess_b["follower_count"]
        elif user_input == "b":
            is_correct = guess_a["follower_count"] < guess_b["follower_count"]
        
        os.system('cls')
        print(art.logo)

        if is_correct:
            score += 1
            print(f"You're right! Current Score: {score}")
            guess_a = guess_b
            guess_b = random.choice(data)

            while guess_a == guess_b:
                guess_b = random.choice(data)
        else:
            keep_playing = False
            print(f"Sorry! thats wrong. Final Score: {score}")
        
play()