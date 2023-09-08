from turtle import Turtle
from time import sleep

#Turtle heading directions
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self, segments:int = 3, delay:float = 0.20, color:str = "white") -> None:
        self.segments = segments
        self.game_running = True
        self.delay = delay
        self.color = color
        self.segments_list = []
        self.__init_segments()

    def __init_segments(self) -> None:
        start = 0
        stop = ((self.segments - 1) * -20) - 1
        step = -20

        for x_position in range(start, stop, step):
            segment = Turtle(shape="square")
            segment.penup()
            segment.color(self.color)
            segment.goto(x_position, 0)
            self.segments_list.append(segment)

    def move(self):
        sleep(self.delay)

        for idx in range(len(self.segments_list) - 1, 0, -1):
            prev_segment = self.segments_list[idx - 1]
            self.segments_list[idx].goto(prev_segment.xcor(), prev_segment.ycor())
        
        self.segments_list[0].forward(20)

    def up(self):
        if self.segments_list[0].heading() != DOWN:
            self.segments_list[0].setheading(UP)
    
    def right(self):
        if self.segments_list[0].heading() != LEFT:
            self.segments_list[0].setheading(RIGHT)
    
    def down(self):
        if self.segments_list[0].heading() != UP:
            self.segments_list[0].setheading(DOWN)
    
    def left(self):
        if self.segments_list[0].heading() != RIGHT:
            self.segments_list[0].setheading(LEFT)
