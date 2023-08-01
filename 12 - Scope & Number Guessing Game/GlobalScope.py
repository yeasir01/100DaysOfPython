
#Modify Global Scope
enemies = 1
kills = 2

#Best practice is to avoid modifying the global scope from a function.
def increase_enemies():
    global enemies #required to modify a variable in the global scope
    enemies += 1
    print(f"enemies inside function: {enemies}")

increase_enemies() #output: enemies outside function: 2

#Heres a better way to modify variables in the global scope
def increase_kills():
    return kills + 1

kills = increase_kills()

print(kills) #output: 3