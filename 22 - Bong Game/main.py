from turtle import Screen
from paddle import Paddle
from game import Game
from ball import Ball
from time import sleep

# Config
WIN_WIDTH=800
WIN_HEIGHT=600
OFFSET = 13
SLEEP_TIME = 0.10

window = Screen()
window.setup(WIN_WIDTH, WIN_HEIGHT)
window.bgcolor("black")
window.title("Py-Pong")
window.tracer(0)

game = Game(WIN_WIDTH, WIN_HEIGHT)

top_border = game.top_border - OFFSET
bottom_border = game.bottom_border + OFFSET

ball = Ball()

right_paddle = Paddle((340, 0))
left_paddle = Paddle((-340, 0))

window.listen()
window.onkeypress(right_paddle.up, "Up")
window.onkeypress(right_paddle.down, "Down")
window.onkeypress(left_paddle.up, "w")
window.onkeypress(left_paddle.down, "s")

while game.is_running:
    window.update()
    ball.move()

    # Detect collision with top and bottom
    if ball.ycor() > top_border or ball.ycor() < bottom_border:
        ball.bounce_y()
    
    # Detect collision with paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 340:
        ball.bounce_x()
    
    if ball.distance(left_paddle) < 50 and ball.xcor() > -340:
        ball.bounce_x()

    sleep(SLEEP_TIME)
window.exitonclick()