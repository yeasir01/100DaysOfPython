from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("CadetBlue")

timmy.forward(100)

screen = Screen()

print(screen.canvheight) #Prints value of attribute

screen.exitonclick()