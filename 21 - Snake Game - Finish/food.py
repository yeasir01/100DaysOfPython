from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed(0)
        self.new_location()
    
    def new_location(self) -> None:
        rand_xcor = randint(-280, 280)
        rand_ycor = randint(-280, 280)
        self.goto(rand_xcor, rand_ycor)
