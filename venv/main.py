from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

segments = []
pos_x = 0
pos_y = 0

for segment in range(0,3):
    segment_1 = Turtle(shape="square")
    segment_1.color("white")
    segment_1.setposition(x=pos_x,y=pos_y)
    segments.append(segment_1)
    pos_x -= 20




screen.exitonclick()