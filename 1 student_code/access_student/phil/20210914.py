

import turtle as t
t.pencolor("blue")
t.penup()
t.goto(0,-50)
t.pendown()
t.circle(100)
t.penup()
t.goto(-100,-50)
t.pendown()
for i in range(4):
    t.forward(200)
    t.left(90)