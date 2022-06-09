
import turtle
import random

# 使用turtle绘制Fibonacci螺旋
def draw_fibonacci(x):
    # F0=1
    # F1=1
    # Fn=F（n-1）+F（n-2）

    # 产生斐波那契数列，用于查表
    # 像这种计算复杂性指数增长的计算，不要写个函数去每次求一个数
    # 最好的办法是，按照规律写出查找表，用查找的方法来得到数据
    f_list = []
    for i in range(x):
        if i == 0:
            f_list.append(1)
        elif i == 1:
            f_list.append(1)
        else:
            f_list.append(f_list[i - 1] + f_list[i - 2])

    # 像素比例
    f0 = 50

    # 设置画笔属性
    turtle.pensize(5)
    turtle.pencolor("black")
    turtle.penup()
    turtle.home()
    turtle.pendown()

    for i in range(0, len(f_list)):
        # 绘制速度，1~10个不同速度等级，小于1或者大于10立即绘制
        turtle.speed(1)
        turtle.pendown()

        # 绘制矩形
        if i == 0:
            fill_color = "black"
        else:
            fill_color = (random.random(), random.random(), random.random())
        turtle.fillcolor(fill_color)
        turtle.begin_fill()
        turtle.forward(f_list[i] * f0)
        turtle.left(90)
        turtle.forward(f_list[i] * f0)
        turtle.left(90)
        turtle.forward(f_list[i] * f0)
        turtle.left(90)
        turtle.forward(f_list[i] * f0)
        turtle.left(90)
        turtle.end_fill()

        # 绘制圆弧
        fill_color = (random.random(), random.random(), random.random())
        turtle.fillcolor(fill_color)
        if i == 0:
            turtle.forward(f_list[i] * f0 / 2)
            turtle.begin_fill()
            turtle.circle(f_list[i] * f0 / 2, 360)
            turtle.end_fill()
            # 移动到一下起点
            turtle.forward(f_list[i] * f0 / 2)
            continue
        else:
            turtle.begin_fill()
            turtle.circle(f_list[i] * f0, 90)
            turtle.left(90)
            turtle.forward(f_list[i] * f0)
            turtle.left(90)
            turtle.forward(f_list[i] * f0)
            turtle.end_fill()

        # 移动到一下起点
        turtle.speed(0)
        turtle.penup()
        turtle.left(90)
        turtle.forward(f_list[i] * f0)
        turtle.left(90)
        turtle.forward(f_list[i] * f0)

    turtle.done()


if __name__ == "__main__":
    draw_fibonacci(6)

import turtle
t = turtle.Pen()
t.left(90)
for x in range(180):
    t.forward(1+x*0.01)
    t.right(1)
t.right(90)
t.forward(115)