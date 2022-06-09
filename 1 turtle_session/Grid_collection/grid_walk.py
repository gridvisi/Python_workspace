

"""
R:red, G:green, B:blue
RGB颜色表示法:
    red: (255,0,0)
    green: (0,255,0)
    blue: (0,0,255)
"""
# 1. 生成渐变色的列表
# 从红色到黄色
colors1 = [(255, g, 0) for g in range(0, 256)]
# 从黄色到绿色
colors2 = [(r, 255, 0) for r in range(255, -1, -1)]
# 从绿色到青色
colors3 = [(0, 255, b) for b in range(0, 256)]
# 从青到蓝
colors4 = [(0, g, 255) for g in range(255, -1, -1)]
# 从蓝到紫
colors5 = [(r, 0, 255) for r in range(0, 256)]
# 从紫到红
colors6 = [(255, 0, g) for g in range(255, -1, -1)]
# colors = colors1 + colors2 + colors3 + colors4 + colors5 + colors6
colors = colors1 + colors2 + colors3 + colors4 + colors5 + colors6


c = [
'lightcoral',
'coral',
'darkorange',
'gold',
'palegreen',
'paleturquoise',
'skyblue',
'plum',
'hotpink',
'pink']

import turtle
import random
import math
'''
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
    t.left()
    v += vs + math.sin((angle/180)*math.pi)*g #*0.1
    t.speed(v)

    t.forward(v * 1)
    t.pendown()

    t.begin_fill()
    t.circle(size)
    t.end_fill()
turtle.exitonclick
turtle.bgcolor("gray")

'''


# curve_曲线
colors = c
t = turtle.Turtle()
t.pensize(5)
angle = 30
turtle.bgcolor("gray")
length = 300
size = 10
x = 300
y = x * math.tan((angle / 180) * math.pi)
t.goto(x, -y)
t.goto(-x, -y)
t.goto(-x, y)
t.goto(0, 0)
t.goto(-x, y)
g = 10
vs, v = 0, 0

color = random.choice(colors)
time_length = 10  # second
t.right(90)
for i in range(int(time_length // 0.1)):
    t.pencolor(color)
    t.fillcolor(color)
    t.penup()

    v += vs + math.sin((angle / 180) * math.pi) * g  # *0.1
    t.speed(v)
    t.forward(v * 1)
    t.left(v*(math.pi - 2.99))
    t.pendown()

    t.begin_fill()
    t.circle(size)
    t.end_fill()
turtle.exitonclick
turtle.bgcolor("gray")


'''

import turtle
import random
colors = ['red', 'cyan', 'pink', 'yellow', 'green', 'orange']
colors = c
t= turtle.Turtle()
t.speed(10)
turtle.bgcolor("gray")
length= 100
angle = 50
size = 5

for i in range(length):
    color=random.choice(colors)
    t.pencolor(color)
    t.fillcolor(color)
    t.penup()
    t.forward(i+50)
    t.pendown()
    t.left(angle)
    t.begin_fill()
    t.circle(size)
    t.end_fill()
    turtle.exitonclick
turtle.bgcolor("black")

'''