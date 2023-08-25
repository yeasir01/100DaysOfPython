from turtle import Turtle, Screen
from random import randint

pen = Turtle()
screen = Screen()
screen.colormode(255)
pen.speed(0)

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r,g,b

direction = 0

while direction < 360:
    pen.color(random_color())
    pen.setheading(direction)
    pen.circle(100)

    direction += 4


screen.exitonclick()