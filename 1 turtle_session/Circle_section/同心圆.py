
# 同心圆

import turtle
def describing_circle(radius,color):
    # 页面的大小
    turtle.setup(width=1400, height=800)

    # 颜色
    turtle.color(color,'red'  )  # 同时给笔和内部区域设置颜色

    # 笔粗细
    turtle.pensize(3)

    # 速度
    turtle.Turtle().screen.delay(1)  # 设置速度 并且取消延迟

    # 隐藏画笔
    turtle.hideturtle()

    # 抬起画笔
    turtle.penup()

    # 将画笔移动到0，-200的坐标点去
    turtle.goto(0 ,-radius)

    # 放下画笔 开始画
    turtle.pendown()

    # 需要进行填充
    #turtle.begin_fill()

    # 半径是200的圆（正数表示从下面往上画）
    turtle.circle(radius)

    # 结束填充
    #turtle.end_fill()

    # 抬起画笔
    turtle.penup()

    # 设置圆心点的颜色
    turtle.color('yellow')  # 同时给笔和内部区域设置颜色

    # 移动到0,1位置
    turtle.goto(0 ,-1)

    # 放下画笔 开始画
    turtle.pendown()

    # 需要进行填充
    turtle.begin_fill()

    # 画圆  半径为1
    turtle.circle(1)

    # 结束填充
    turtle.end_fill()

import time
for i in range(14):
    color_ls = ['red', 'blue', 'yellow', 'pink', 'black', 'orange', 'grey', 'green', 'purple', 'lavender']
    color_ls = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple']
    color_ls = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple']
    # 颜色
    #turtle.color(color_ls[r])  # 同时给笔和内部区域设置颜色
    describing_circle(i*20,color_ls[i%len(color_ls)])
time.sleep(20)