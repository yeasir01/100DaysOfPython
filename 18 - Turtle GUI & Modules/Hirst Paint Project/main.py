import colorgram
import turtle as t
import random
import os

turtle = t.Turtle()
screen = t.Screen()
screen.setup(550, 550)
screen.colormode(255)

turtle.speed(0)
turtle.penup()

path = os.path.join(os.getcwd(), "18 - Turtle GUI & Modules", "Hirst Paint Project" , "image.jpg")
colors = colorgram.extract(path, 30)

rgb_colors = []
coordinates = -230

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))


def draw_circles():
    for _ in range(10):
        turtle.dot(20, random.choice(rgb_colors))
        turtle.forward(50)

for _ in range(10):
    turtle.setposition(-230, coordinates)
    draw_circles()
    coordinates += 50

screen.exitonclick()