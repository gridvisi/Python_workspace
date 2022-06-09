#triangle  rectangles
#turtle.forward(200)
#turtle.backward(200)
#turtle.done()
#import tkinter


import turtle as t #乌龟
#t = turtle.Turtle()
#turtle.forward

t.color("red")
#t.color("颜色")


"""
关于颜色列举几个英中对照：
black 黑色
blue 蓝色
green 绿色
gray 灰色
red 红色
yellow 黄色
purple 紫色
pink 粉色
"""
for i in range(5):
    print(i)
    #turtle.left(90)
    t.left(90)
    #turtle.backward(250)
    t.backward(250)


import turtle
t = turtle.Turtle()
t.color("red")
t.fd(100)
t.end_fill()     #填充完成
turtle.done()


# 代码部分：
import turtle
#t = turtle.Pen()  #获得画笔
t = turtle.Turtle()
t.color("red")
#t.fillcolor("red")  # 设置填充颜色为红色
for i in range(5):
    print(i)
    #turtle.left(90)
    t.left(90)
    #turtle.backward(250)
    t.backward(250)
t.end_fill()     #填充完成
turtle.done()

#2

'''
import turtle
t = turtle.Pen()  #获得画笔
t.hideturtle()  #隐藏海龟
t.fillcolor("yellow")  #设置填充颜色为红色
t.begin_fill()    #开始填充
for x in range(1, 5):
    t.forward(150)
    t.left(90)  #在这里先向右直行，然后左转216°(左下，正五角星度数180/5=36°)
t.end_fill()     #填充完成
turtle.done()



'''
