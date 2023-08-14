import turtle

timmy = turtle.Turtle()
timmy.shape("turtle")
timmy.color("CadetBlue")

timmy.forward(100)

screen = turtle.Screen()

print(screen.canvheight) #Prints value of attribute

screen.exitonclick()