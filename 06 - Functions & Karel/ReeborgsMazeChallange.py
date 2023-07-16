#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

#my solution to maze challenge
def turn_right():
    for x in range(0, 3):
        turn_left()
       
def foward():
    while front_is_clear():
        move()

while not at_goal():
    foward()
    if right_is_clear():
        turn_right()
        foward()
    else:
        turn_left()
        foward()