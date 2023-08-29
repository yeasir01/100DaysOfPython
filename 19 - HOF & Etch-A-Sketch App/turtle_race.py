from turtle import Turtle, Screen
import random

SCREEN_HEIGHT = 400
SCREEN_WIDTH = 500
TURTLE_WIDTH = 20

screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.title("Py-Turtle Racer")

config = [
    {"color": "red", "y_coordinate": -167},
    {"color": "blue", "y_coordinate": -100},
    {"color": "green", "y_coordinate": -33},
    {"color": "purple", "y_coordinate": 33},
    {"color": "gray", "y_coordinate": 100},
    {"color": "pink", "y_coordinate": 167},
]

turtles = []
# list Comprehension W/Join method to convert to comma separated string.
colors = ", ".join([item["color"] for item in config])

for item in config:
    t = Turtle(shape="turtle")
    t.penup()
    t.color(item["color"])
    t.goto(-250 + TURTLE_WIDTH, item["y_coordinate"])
    turtles.append(t)

choice = screen.textinput(
    "Question", f"Which color will win?\n{colors}\nEnter a color:"
)

is_playing = True
wining_color = None

while is_playing:
    random_turtle = random.choice(turtles)
    position = random_turtle.xcor()

    if position < (SCREEN_WIDTH / 2) - TURTLE_WIDTH:
        rand_distance = random.randint(0, 10)
        random_turtle.forward(rand_distance)
    else:
        is_playing = False
        wining_color = random_turtle.color()[1]

if wining_color == choice:
    print(f"You won! The {wining_color} turtle is the winner!")
else:
    print(f"You lost! The {wining_color} turtle is the winner!")

screen.exitonclick()
