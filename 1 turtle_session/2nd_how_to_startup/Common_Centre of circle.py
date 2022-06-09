'''
2、画十个半径越来越小的同心填充圆形，每个圆形的颜色都不一样。

green 绿色
moss green 苔绿色
emerald green 鲜绿色
olive green 橄榄绿

blue 蓝色bai
turquoise blue 土耳其玉色
cobalt blue 钴蓝色, 艳蓝色
navy blue 藏青色, 深蓝色, 天蓝色
aquamarine blue 蓝绿色

red 红色
scarlet 绯红, 猩红
mauve 紫红
wine red 葡萄酒红
purple, violet 紫色

lavender 淡紫色
lilac 浅紫色
'''

import turtle as t
t.setup(650,650)
t.pencolor("green")
t.pensize(1.5)
t.penup()
for i in range(11):
    t.fd(30 + i*30)
    t.pendown()
    t.seth(90)
    t.circle(30+i*30,360)
t.done()


import turtle as t
t.setup(650,650)
t.pencolor("green")
t.pensize(1.5)
t.penup()
t.fd(300)
t.pendown()
t.seth(90)
t.circle(300,360)
t.done()




import turtle
t = turtle
from tkinter import *
canvas = Canvas(width=500, height=500, bg='blue')
canvas.pack(expand=YES, fill=BOTH)
k, j = 10, 10
for i in range(10):
    color = ['red','blue','yellow','pink','black','orange','grey','green','purple','lavender']
    t.pencolor(color[i])
    canvas.create_oval(250 - k, 250 - k, 250 + k, 250 + k, width=1)
    k += j
    j += 4

mainloop()


import turtle as t
t.circle(100, 90, 5)
t.exitonclick()



for r in range(1,11):
    t.goto(r,r)
    t.circle(10*r)

for _ in range(361):
    t.forward(3)
    t.left(1)


#from turtle import*
    t.speed(1)#画的速度，0-10之间

    t.seth(0)          #画笔方向指向0度，即东方
    t.circle(100,180)  #画笔方向逆时针画圆,半径100，旋转180度，即半圆
    t.circle(100,-180) #画笔方向倒退画圆，画同一个圆
    t.pencolor("yellow") #画笔颜色设为黄色，即画出线条的颜色
    t.circle(100,-180)
    t.pu()            #提起画笔，画笔移动，不留痕迹
    t.goto(0,0)      #画笔移动回原点
    t.pd()           #画笔落下，画笔移动时画线条
    t.seth(180)      #画笔方向设为180度，即西方
    t.pencolor("blue") #画笔颜色设为蓝色，即画出的线条颜色
    t.circle(100,180)
    t.circle(100,-180)
    t.pencolor("red")
    t.circle(100,-180)
    t.seth(0)
    t.circle(-100,180) #顺时针画圆
    t.circle(-100,-180)