#No block scope in Python for (if, for, while)

enemies = ["Skeleton", "Zombie", "Alien"]
game_level = 3

if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy) #output: Skeleton

#You can access variables in if statement