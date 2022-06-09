from turtle import *
import turtle
t = turtle.Pen()  #获得画笔
t.hideturtle()  #隐藏海龟
t.fillcolor("red")  #设置填充颜色为红色
t.begin_fill()    #开始填充
t.forward(200)
# Make a diameter 200 semicircle, curving down
for i in range(100):
    t.forward(3.1416)
    t.right(1.8)
t.forward(200)
t.fillcolor("blue")  #设置填充颜色为红色
t.begin_fill()    #开始填充
t.end_fill()     #填充完成
turtle.done()



#t = turtle()
t.forward(300)
t.fillcolor("green")  #设置填充颜色为红色
t.begin_fill()    #开始填充

t.left(90)
t.backward(325)
t.fillcolor("blue")  #设置填充颜色为红色
t.begin_fill()    #开始填充
t.end_fill()     #填充完成
turtle.done()


print("Python")
print("Time")

print(1+1)

print(sum([i for i in range(2022)]))

