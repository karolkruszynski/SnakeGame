from turtle import Screen, Turtle
import time

segments = []
pos_x = 0
pos_y = 0

class Snake():

    '''Create a 3pc snake base and append to the segments list'''
    for segment in range(0,3):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.setposition(x=pos_x,y=pos_y)
        segments.append(new_segment)
        pos_x -= 20
    
    '''Make a Snake move and linked every piece and make them replace the previouse piece position'''
    def move(self):
        for seg_num in range(len(segments) -1, 0, -1):
            new_x = segments[seg_num - 1].xcor()
            new_y = segments[seg_num - 1].ycor()
            segments[seg_num].goto(new_x, new_y)
        segments[0].forward(20)
        # segments[0].left(90)
