
#动态规划入门任务：有多少条没有重复的路


import turtle
import random
import math


c = ['lightcoral','coral','darkorange','gold',
     'palegreen','paleturquoise','skyblue',
     'plum','hotpink','pink']

colors = ['red', 'cyan', 'pink', 'yellow', 'green', 'orange']
colors = c
t = turtle.Turtle()
t.pensize(5)
angle = 30
turtle.bgcolor("gray")
length= 300
size = 10
x = 300
y = x * math.tan((angle/180)* math.pi)
t.goto( x, -y)
t.goto(-x, -y)
t.goto(-x,  y)
t.goto(0,0)
t.goto(-x,  y)
g = 10
vs,v = 0,0

color=random.choice(colors)
time_length = 10 #second
t.right(angle)
for i in range(int(time_length//0.1)):
    t.pencolor(color)
    t.fillcolor(color)
    t.penup()

    v += vs + math.sin((angle/180)*math.pi)*g #*0.1
    t.speed(v)

    t.forward(v * 1)
    t.pendown()

    t.begin_fill()
    t.circle(size)
    t.end_fill()
turtle.exitonclick
turtle.bgcolor("gray")
