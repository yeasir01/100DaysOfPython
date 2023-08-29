from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

def forward():
    turtle.forward(10)

def back():
    turtle.backward(10)

def left():
    turtle.left(10)

def right():
    turtle.right(10)

def reset():
    turtle.reset()

screen.listen()
screen.onkey(forward, "Up")
screen.onkey(back, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(reset, "c")

screen.exitonclick()