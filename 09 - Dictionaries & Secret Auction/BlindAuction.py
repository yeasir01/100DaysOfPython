import os
import art

os.system('cls') #clears terminal

bidders = {}

print(art.logo)
print("Welcome to the secret auction program.")

end_of_bid = False

def find_highest(bidders_dictionary):
    highest = 0
    winner = ""

    for bidder in bidders_dictionary:
        amount = bidders_dictionary[bidder]

        if amount > highest:
            highest = amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest}")

while not end_of_bid:
    name = input("What is your name? ")
    bid = float(input("What is your bid amount? $"))

    bidders[name] = bid

    more_bids = input('Are there any other bidders? "Y" or "N"? ').lower()
    
    if more_bids == "n":
        end_of_bid = True
        find_highest(bidders)
    else:
        os.system('cls')
