
import turtle
turtle.bgcolor("orange")
turtle.penup()
turtle.goto(-100,-100)
turtle.pendown()
turtle.turtlesize(2)
i = 0
t = ["blue","yellow","back","green","red"]
for i in range(5):
    turtle.color(t[i])
    for j in range(4):
        turtle.circle(100)
    i += 1
t.done()