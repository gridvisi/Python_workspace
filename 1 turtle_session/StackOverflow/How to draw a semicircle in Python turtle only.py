

#3rd   circle_lzj
from turtle import*
import turtle
t = turtle
t.speed(0)
i=0
while i < 360:
    t.forward(1)
    t.left(1)
    i+=1

import turtle
t = turtle.Pen()
t.left(90)
for x in range(180):
    t.forward(1)
    t.right(1)
t.right(90)
t.forward(115)


from turtle import Turtle, Screen

screen = Screen()

DIAMETER = 200
STAMP_SIZE = 20
BACKGROUND = screen.bgcolor()

yertle = Turtle('circle', visible=False)
yertle.penup()

yertle.shapesize(DIAMETER / STAMP_SIZE)
yertle.color('black', BACKGROUND)  # drop second argument for a filled semicircle
yertle.stamp()

yertle.shape('square')
yertle.shapesize(stretch_len=(DIAMETER / 2) / STAMP_SIZE)
yertle.color(BACKGROUND)
yertle.forward(DIAMETER / 4)
yertle.stamp()

screen.exitonclick()

