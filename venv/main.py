from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

segments = []
pos_x = 0
pos_y = 0

for segment in range(0,3):
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.setposition(x=pos_x,y=pos_y)
    segments.append(new_segment)
    pos_x -= 20

screen.update()
game_is_on = True

while game_is_on:
    for seg in segments:
        seg.forward(20)



screen.exitonclick()