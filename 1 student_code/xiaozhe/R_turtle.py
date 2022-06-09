
from turtle import *
import turtle as t
t.speed(5)
t.width(15)

# draw the left stem
t.left(90)
t.forward(205)

# draw the loop
t.right(90)
t.forward(50)
for i in range(20):
    t.right(18)       # fix this line
    t.forward(10)
t.forward(40)

# draw the right leg
t.back(50)
t.left(-40)
t.forward(120)

t.hideturtle()
t.bye()