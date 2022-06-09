
import turtle as t
from tkinter import *
import random
c = ['red2','SkyBlue3','yellow']

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
# Setup the window with a background color
screen = t.Screen()
screen.bgcolor("white")


for i,xy in enumerate([(-60,-60),(0,30),(60,-60)]):
    print(i,xy)
    # 抬起画笔
    t.penup()
    t.begin_fill()
    # 设置圆心点的颜色

    t.color(c[i])  # 同时给笔和内部区域设置颜色
    # 移动到0,1位置
    t.goto(xy[0], xy[1])

    # 放下画笔 开始画
    t.pendown()

    t.pensize(5)
    t.pencorlor = "blue"
    t.circle(100)
    t.end_fill()


'''

t.pensize(5)
t.pencorlor = "blue"
t.circle(100)
t.end_fill()
'''
t.done()

