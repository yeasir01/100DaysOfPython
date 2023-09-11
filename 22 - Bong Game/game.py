from turtle import Turtle


class Game(Turtle):
    def __init__(self, width, height) -> None:
        super().__init__()
        self.top_border = 0
        self.bottom_border = 0
        self.is_running = True
        self.__render_border(width, height)

    def __render_border(self, width, height):
        self.pencolor("White")
        self.pensize(3)
        self.penup()
        self.hideturtle()

        # Move borders away from edge and get all coordinates
        left = -(width - 60) / 2.0
        right = (width - 60) / 2.0
        top = (height - 60) / 2.0
        bottom = -(height - 60) / 2.0

        # Set attributes in object
        self.top_border = top
        self.bottom_border = bottom

        # Draw a border clockwise
        self.goto(left, top)
        self.pendown()
        self.goto(right, top)
        self.goto(right, bottom)
        self.goto(left, bottom)
        self.goto(left, top)
        self.penup()


