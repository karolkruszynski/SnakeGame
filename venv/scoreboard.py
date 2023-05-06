from turtle import Turtle

class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,280)
        self.write(f"Score: {test}",True,align="center",font=('Arial', 10, 'bold'))

