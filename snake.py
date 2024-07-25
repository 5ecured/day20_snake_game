from turtle import Turtle

# a list of tuples
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        # segments is a list that is used to represent the snake body
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle('square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
         # the range parameters: start, stop, step
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # the way to move the snake is for the last segment to go to the position of the second last segment, and so on
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        
        # of course the first segment itself has to move, becase the rest of the segments follow the one in front of it
        self.segments[0].forward(MOVE_DISTANCE)