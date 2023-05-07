from turtle import Screen, Turtle
import time

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    '''Create a 3pc snake base and append to the segments list'''
    def __init__(self):
        self.segments = []
        self.pos_x = 0
        self.pos_y = 0
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for segment in range(0,3):
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.setposition(x=self.pos_x, y=self.pos_y)
        self.segments.append(new_segment)
        self.pos_x -= 20

    def extend(self):
        self.add_segment(self.segments[-1].position())
    
    '''Make a Snake move and linked every piece and make them replace the previouse piece position'''
    def move(self):
        for seg_num in range(len(self.segments) -1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)
        # segments[0].left(90)
        '''Moving snake head & block to move in opposite direction instantly'''
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)