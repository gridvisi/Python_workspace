
import turtle
turtle.bgcolor("orange") #bg:background
turtle.penup()           #
turtle.goto(-100,-100)
turtle.pendown()
turtle.pensize(5)
y = -100
i = 0
t = ["blue","yellow","black","green","red"]
turtle.penup()
turtle.goto(y,-100)
turtle.pendown()
turtle.color(t[i])
turtle.circle(100)
i += 1
y = -200
turtle.penup()
turtle.goto(0,y)
turtle.pendown()
turtle.color(t[i])
turtle.circle(100)
i += 1
y = -100
turtle.penup()
turtle.goto(105,y)
turtle.pendown()
turtle.color(t[i])
turtle.circle(100)
i += 1
y = -200
turtle.penup()
turtle.goto(210,y)
turtle.pendown()
turtle.color(t[i])
turtle.circle(100)
i += 1
y = -100
turtle.penup()
turtle.goto(315,y)
turtle.pendown()
turtle.color(t[i])
turtle.circle(100)
turtle.done()