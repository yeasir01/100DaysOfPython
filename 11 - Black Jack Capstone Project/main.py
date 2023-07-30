import art
import os
import random

def play():
    os.system('cls')
    print(art.logo)

    user_cards = []
    dealer_cards = []
    game_over = False

    #function returns a random card from the list
    def random_card():
        cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
        return random.choice(cards)

    #function tallies up cards in a provided list and returns a total
    def card_total(cards_list):
        total = 0

        for card in cards_list:
            if card == "J" or card == "Q" or card == "K":
                total += 10
            elif card == "A":
                total += 11
            else:
                total += card
        
        if total > 21 and "A" in cards_list:
            total -= 10

        return total

    #function checks scores and returns a message
    def score_message(user, dealer):
        if user == dealer:
            return "😐 Draw!"
        elif user > 21:
            return "❌ Bust, you loose!"
        elif dealer == 21:
            return "😢 Dealer wins!"
        elif user == 21:
            return "🃏 Blackjack. You win!"
        elif dealer > 21:
            return "🏆 You win, dealer went over!"
        elif user > dealer:
            return "🏆 You win!"
        else:
            return "😭 You loose"

    #loop set the initial 2 cards for user & dealer
    for _ in range(2):
        user_cards.append(random_card())
        dealer_cards.append(random_card())

    #check the dealer cards if the sum of all the cards are below 17 assign additional cards
    while card_total(dealer_cards) < 17:
        dealer_cards.append(random_card())

    while not game_over:
        user_total = card_total(user_cards)
        dealers_total = card_total(dealer_cards)
        message = score_message(user_total, dealers_total)

        if user_total > 21:
            game_over = True
            print(f"Your Hand: {user_cards} = {user_total}")
            print(f"Dealers Hand: {dealer_cards} = {dealers_total}")
            print(message)
        else:
            print(f"Your Hand: {user_cards} = {user_total}")
            print(f"Dealers Hand: [{dealer_cards[0]}, ...] = ?")

            answer = input("\nWould you like to Hit or Stand? H or S? ").lower()

            if answer not in ["h", "s"]:
                game_over = True
                print("Invalid Entry. Game Over!")
            elif answer == "h":
                user_cards.append(random_card())
            else:
                game_over = True
                print(f"Your Hand: {user_cards} = {user_total}")
                print(f"Dealers Hand: {dealer_cards} = {dealers_total}")
                print(message)
        
    #After exiting the while loop ask user if they would like to play again
    play_again = input("\nReplay? Y or N? ").lower()
    if play_again == "y": play()
    
#call the play function initialize game play
play()