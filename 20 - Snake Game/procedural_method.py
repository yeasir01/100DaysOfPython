from turtle import Turtle, Screen
import time

#Turtle config setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# initial coordinates
segment_coordinates = [(0, 0), (-20, 0), (-40, 0)]
snake_body = []

# Set the starting position of the three segments
for position in segment_coordinates:
    segment = Turtle(shape="square")
    segment.penup()
    segment.color("white")
    segment.goto(position)
    snake_body.append(segment)

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)

    # Reverse for loop
    # forces the current segment to follow the coordinates of the previous segment.
    for idx in range(len(snake_body) - 1, 0, -1):
        prev_segment = snake_body[idx - 1]
        snake_body[idx].goto(prev_segment.xcor(), prev_segment.ycor())

    snake_body[0].forward(20)
    snake_body[0].left(90)

screen.exitonclick()
