from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Nokia Snake Game')
screen.tracer(0)

# a list of tuples
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

# segments list is used to represent the snake body
segments = []

for position in starting_positions:
    new_segment = Turtle('square')
    new_segment.color('white')
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

screen.update()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    # the range parameters: start, stop, step
    for seg_num in range(len(segments) - 1, 0, -1):
        # the way to move the snake is for the last segment to go to the position of the second last segment, and so on
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)















screen.exitonclick()