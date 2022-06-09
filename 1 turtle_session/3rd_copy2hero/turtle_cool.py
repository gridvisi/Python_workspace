#SquareSpiral1.py
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
sides = 4
colors=["red","yellow","green","blue","orange","purple","pink"]
for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(x*3/sides+x)
    t.left(360/sides+1)
    t.width(x*sides/200)

import turtle
t = turtle.Pen()
turtle.bgcolor("black")
sides=eval(input("输入要绘制的边的数目，请输入2-6的数字！"))
colors=["red","yellow","green","blue","orange","purple"]
for x in range(100):
    t.pencolor(colors[x%sides])
    t.forward(x*3/sides+x)
    t.left(360/sides+1)
    t.width(x*sides/200)

#https://blog.csdn.net/qq_14961401/article/details/58595783