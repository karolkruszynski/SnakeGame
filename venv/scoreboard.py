from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,280)
        self.write(f"Score: {self.score}",False,align="center",font=('Arial', 10, 'bold'))
        
    def score_track(self):
        self.clear()
        self.write(f"Score: {self.score}",False,align="center",font=('Arial', 10, 'bold'))


