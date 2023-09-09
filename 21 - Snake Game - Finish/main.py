from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Turtle config setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while snake.game_running:
    screen.update()
    snake.move()

    # detect collision w/food object
    if snake.head.distance(food) < 15:
        food.new_location()
        scoreboard.update(score=1)
        snake.extend()

    # detect collision w/wall
    if (
        snake.head.xcor() > 290
        or snake.head.xcor() < -290
        or snake.head.ycor() > 290
        or snake.head.ycor() < -290
    ):
        snake.game_running = False
        scoreboard.game_over()

    # detect collision w/body using the slice method starting from the second segment
    for segment in snake.segments_list[1:]:
        if snake.head.distance(segment) < 10:
            snake.game_running = False
            scoreboard.game_over()

screen.exitonclick()
