from turtle import Turtle
from time import sleep

#Turtle heading directions
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self, segments:int = 3, delay:float = 0.15, color:str = "greenYellow") -> None:
        self.segments = segments
        self.game_running = True
        self.delay = delay
        self.color = color
        self.segments_list = []
        self.__init_segments()
        self.head = self.segments_list[0]

    def __init_segments(self) -> None:
        start = 0
        stop = ((self.segments - 1) * -20) - 1
        step = -20

        for x_position in range(start, stop, step):
            self.__add_segment((x_position, 0))
    
    def __add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("black")
        new_segment.fillcolor(self.color)
        new_segment.goto(position)
        self.segments_list.append(new_segment)
    
    def extend(self):
        self.__add_segment(self.segments_list[-1].position())

    def move(self):
        sleep(self.delay)

        for idx in range(len(self.segments_list) - 1, 0, -1):
            prev_segment = self.segments_list[idx - 1]
            self.segments_list[idx].goto(prev_segment.xcor(), prev_segment.ycor())
        
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
