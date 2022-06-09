
from turtle import *
from datetime import *
import time
'''主要的思想就是海龟作图，然后用一个循环去刷新一帧图像
但是因为应用了比较复杂的数码管图像，每一帧刷新延迟会比较严重
所以引入了多只乌龟来进行刷新，同时控制不同乌龟的刷新速度，来优化程序
'''
def skip(t :Turtle ,step=5):
    # 这里定义了一个新的turtle操作，跳跃,默认画出小间隔
    # 确保之后小乌龟都是以pendown，然后白的靠跳
    t.penup()
    t.forward(step)
    t.pendown()

def digital_tuber(ignitor ,t :Turtle):
    # 画出一个数码管（6边形），但是不注册它,颜色由外部控制
    # 小乌龟会在自己面朝的方向（正中）上画出一个数码管
    temp = t.pensize()
    t.pensize(2)
    skip(t)
    if ignitor:
        # ignitor用于控制是否进行画图，不然就是空白管
        t.pendown()
        t.begin_fill()
        t.begin_poly()
        for i in range(2):
            t.left(30)
            t.forward(5)
            t.right(30)
            t.forward(32)
            t.right(30)
            t.forward(5)
            t.right(150)
        t.end_poly()
        t.end_fill()
        skip(t ,40)
    else:
        skip(t ,40)
    skip(t)
    t.pensize(temp)
    # 还原

def digital_maker(digit :int ,t :Turtle):
    # 画出数码管构成数字,然后在每次显示的时候对一个图像刷新
    # 用一个函数来实现所有数字
    t.left(90)    # 因为我们采取的是默认的模式，而不是logo
    t.pendown()
    # 画出管的实现
    digital_tuber(True ,t) if digit in [0, 1, 4, 5, 6, 8, 9] else digital_tuber(False ,t)
    t.right(90)
    digital_tuber(True ,t) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else digital_tuber(False ,t)
    t.right(90)
    digital_tuber(True ,t) if digit in [0, 2, 3, 4, 7, 8, 9] else digital_tuber(False ,t)
    digital_tuber(True ,t) if digit in [0, 3, 4, 5, 6, 7, 8, 9] else digital_tuber(False ,t)
    t.right(90)
    digital_tuber(True ,t) if digit in [0, 2, 3, 5, 6, 8, 9] else digital_tuber(False ,t)
    t.right(90)
    digital_tuber(True ,t) if digit in [0, 1, 2, 6, 8 ,] else digital_tuber(False ,t)
    t.right(90)
    digital_tuber(True ,t) if digit in [2, 3, 4, 5, 6, 8, 9] else digital_tuber(False ,t)

def show_number(n :int ,t :Turtle):
    # 用于画出数字
    n = str(n)
    for i in n:
        digital_maker(int(i) ,t)
        skip(t ,20)

def setframe():
    # 画出程序的外框，和文字
    t = Turtle()
    t.hideturtle()
    # 框架的画出不参与刷新，所以我们不需要外部turtle
    t.begin_poly()
    t.pensize(10)
    t.penup()
    t.goto(-450 ,250)
    t.pendown()
    t.goto(450 ,250)
    t.goto(450 ,-250)
    t.goto(-450 ,-250)
    t.goto(-450 ,250)
    t.penup()
    t.end_poly()

def show_hours(t :Turtle):
    # 画出下方的精确时间的函数
    t.reset()
    t.penup()
    t.goto(-275, -100)
    t.pendown()
    temp = datetime.today()
    h = temp.hour
    m = temp.minute
    s = temp.second
    # 确保是两位数的格式
    if h <= 9:
        h = '0 ' +str(h)
    else:
        h = str(h)
    if m <= 9:
        m = '0' + str(m)
    else:
        m = str(m)
    if s <= 9:
        s = '0' + str(s)
    else:
        s = str(s)
    #drawDate( h +': ' + m +': ' +s ,t)

def defaultsetter():
    # 用于初始化我们的画图体系
    global dater, framer    # 在重置阶段就申明好乌龟，就不要多次申明了
    # 实际上我想做的优化就是让许多只小乌龟去画，就可以减少刷心负担
    #tracer(0)
    #screensize(1000, 600)
    framer = Turtle()
    framer.hideturtle()
    dater = Turtle()
    dater.hideturtle()

def resh_hour():
    # 两个大函数的递归调用，为了区别刷新频率
    dater.reset()
    show_hours(dater)
    #ontimer(resh_hour ,1000)
    # 刷新基础时间，间隔为一秒

def main():
    defaultsetter()
    setframe()
    show_hours()
    resh_hour()
    #mainloop()
if __name__ == '__main__':
    main()