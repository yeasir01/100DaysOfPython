print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input('Your at a cross road. Where would you like to go? "left" or "right"?\n').lower()

if direction == "left":
    
    swim = input('You have arrived at a lake. There is an island in the distance. Type "swim" to swim across or "wait" to wait for a boat.\n').lower()
    
    if swim == "wait":
        door = input('You have arrived to the island unharmed. There is a house with three doors. One "red", One "yellow" and one "blue". Which door do you choose?\n').lower()
        
        if door == "red":
            print("You've been burnt by fire. Game Over!")
        elif door == "blue":
            print("You've been eaten by beasts. Game Over!")
        elif door == "yellow":
            print("You Win!")
        else:
            print("You choose a door that doesn't exists. Game Over!")
    else:
        print("You've been attacked by a trout. Game Over!")
else:
    print("You fell into a hole. Game Over!")