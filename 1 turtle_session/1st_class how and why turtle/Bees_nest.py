

import turtle as t
from tkinter import *
import random
c = ['red2','SkyBlue3','yellow']

def Hexagonal(side,n): #六边形,n=边的数量
    for _ in range(n):
        t.forward(side)
        t.left(360//n)
    return
side,n = 30,17

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


#for i,xy in enumerate([(-60,-60),(0,30),(60,-60)]):
t.goto(0, 0)
side = 60
for i in range(12):
    # 抬起画笔
    t.penup()
    t.begin_fill()
    # 设置圆心点的颜色

    t.color(c[i])  # 同时给笔和内部区域设置颜色
    # 移动到0,1位置


    # 放下画笔 开始画
    t.pendown()

    t.pensize(5)
    t.pencorlor = "blue"

    Hexagonal(side,n)
    t.end_fill()
    t.right(side)


    #t.forward(side//2)
    #t.right(120 - (i%3==2)*180)
    #t.forward(200)


'''

t.pensize(5)
t.pencorlor = "blue"
t.circle(100)
t.end_fill()
'''
t.done()
