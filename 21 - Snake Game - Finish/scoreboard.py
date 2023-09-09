from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, color="white") -> None:
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.speed(0)
        self.color(color)
        self.setposition(0, 260)
        self.update(0)
    
    def update(self, score):
        self.score += score
        self.clear()
        self.write(f"SCORE: {self.score}", align="center", font=("Courier", 18, "normal"))
    
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align="center", font=("Courier", 18, "bold"))