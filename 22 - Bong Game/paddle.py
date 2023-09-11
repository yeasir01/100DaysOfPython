from turtle import Turtle

DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, position: tuple) -> None:
        super().__init__()
        self.shapesize(5, 1)
        self.color("white")
        self.shape("square")
        self.penup()
        self.setposition(position)

    def up(self):
        new_y = self.ycor() + DISTANCE
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - DISTANCE
        self.goto(self.xcor(), new_y)
        