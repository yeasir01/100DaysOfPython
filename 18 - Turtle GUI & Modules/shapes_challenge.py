#Using turtle draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon

from turtle import Turtle, Screen
from random import randint

pen = Turtle()
screen = Screen()
screen.colormode(255)

def new_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r,g,b

sides = 3

while sides < 10:
    pen.color(new_color())

    for _ in range(sides):
        pen.forward(100)
        pen.right(360 / sides)

    sides += 1

screen.exitonclick()