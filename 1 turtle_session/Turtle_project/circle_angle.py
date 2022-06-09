# 需要导入模块: import turtle [as 别名]
# 或者: from turtle import begin_fill [as 别名]
def square(x, y, size, name):
    """Draw square at `(x, y)` with side length `size` and fill color `name`.

    The square is oriented so the bottom left corner is at (x, y).

    """
    import turtle
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color(name)
    turtle.begin_fill()

    for count in range(4):
        turtle.forward(size)
        turtle.left(90)

    turtle.end_fill()
# 需要导入模块: import turtle [as 别名]
# 或者: from turtle import begin_fill [as 别名]
import turtle as t
def head():
    '''
    头
    '''
    t.color((255, 155, 192), "pink")
    t.pu()
    t.seth(90)
    t.fd(41)
    t.seth(0)
    t.fd(0)
    t.pd()
    t.begin_fill()
    t.seth(180)
    t.circle(300, -30)  # 顺时针画一个半径为300,圆心角为30°的园
    t.circle(100, -60)
    t.circle(80, -100)
    t.circle(150, -20)
    t.circle(60, -95)
    t.seth(161)
    t.circle(-300, 15)
    t.pu()
    t.goto(-100, 100)
    t.pd()
    t.seth(-30)
    a = 0.4
    for i in range(60):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            t.lt(3)  # 向左转3度
            t.fd(a)  # 向前走a的步长
        else:
            a = a - 0.08
            t.lt(3)
            t.fd(a)
    t.end_fill()


# 需要导入模块: import turtle [as 别名]
# 或者: from turtle import begin_fill [as 别名]
def draw_leaf(turtle):
    turtle.fillcolor("greenyellow")
    turtle.begin_fill()

    base = turtle.pos()
    turtle.circle(100, 75)
    turtle.goto(base)
    turtle.circle(-100, 75)
    turtle.goto(base)
    turtle.end_fill()


# 需要导入模块: import turtle [as 别名]
# 或者: from turtle import begin_fill [as 别名]
def ear():
    '''
    耳朵
    '''
    t.color((255, 155, 192), "pink")
    t.pu()
    t.seth(90)
    t.fd(-7)
    t.seth(0)
    t.fd(70)
    t.pd()
    t.begin_fill()
    t.seth(100)
    t.circle(-50, 50)
    t.circle(-10, 120)
    t.circle(-50, 54)
    t.end_fill()
    t.pu()
    t.seth(90)
    t.fd(-12)
    t.seth(0)
    t.fd(30)
    t.pd()
    t.begin_fill()
    t.seth(100)
    t.circle(-50, 50)
    t.circle(-10, 120)
    t.circle(-50, 56)
    t.end_fill()