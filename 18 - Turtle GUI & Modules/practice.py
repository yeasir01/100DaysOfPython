from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
timmy.shape("turtle")
timmy.color("red")

""" 

#Draw a square challenge
for _ in range(4):
    timmy.forward(100)
    timmy.right(90)

#Draw a triangle
for _ in range(3):
    timmy.forward(100)
    timmy.left(120) 

"""
#Draw a dashed line
for _ in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

screen.exitonclick()