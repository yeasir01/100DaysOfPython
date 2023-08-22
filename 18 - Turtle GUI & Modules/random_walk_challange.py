from turtle import Turtle, Screen
from random import choice, randint

pointer = Turtle()
screen = Screen()
directions = [0, 90, 180, 270]

pointer.pensize(15)
pointer.shape("triangle")
pointer.speed(0)
screen.colormode(255)

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)

for _ in range(400):
    pointer.pencolor(random_color())
    pointer.forward(30)
    pointer.setheading(choice(directions))

screen.exitonclick()