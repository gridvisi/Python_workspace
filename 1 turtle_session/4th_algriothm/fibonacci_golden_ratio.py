from turtle import *
import turtle as t
# import cmath
t.speed(10)
t.pensize(5)


# 判断较小整数的函数
def little(a, b):
    if a < b:
        return a
    else:
        return b


# 初始点
# 矩形
x0 = 250
y0 = 150
r = little(2 * x0, 2 * y0)


# 定义绘制、填充1/2正方形及扇形的函数
def square_sector(r, color_couple):
    t.color("black", color_couple[0])
    t.begin_fill()
    # 顺时针画1/2正方形
    # for i in range(2):
    t.fd(r)
    t.rt(90)
    t.fd(r)
    t.end_fill()
    # 顺时针画剩余1/2正方形及1/4圆弧
    t.color("black", color_couple[1])
    t.begin_fill()
    for i in range(2):
        t.rt(90)
        t.fd(r) #r
    t.rt(90)
    t.circle(-r, 90)
    t.end_fill()


# 黄金比例
# golden_ratio = (cmath.sqrt(5)-1)/2#can't convert complex to int
golden_ratio = 0.618

# 5组填充色——[color_rect,color_arc]#1/2矩形，扇形
color_ls = [["#8F653B", "#EDCB67"], ["#B58539", "#7D6A98"], \
            ["#FAC374", "#56ACA9"], ["#D87D84", "#DA8F3C"],
            ["#769A43", "#CF4749"]]

#color_ls =  ['red','orange','yellow','green','blue'] #,'purple','pink']
t.pu()
t.goto(x0, y0)  # 矩形的右上顶点,默认初始角度0
t.pd()
t.seth(-90)
# 循环绘制、填充矩形及扇形
for i in range(5):
    r = 300 * (golden_ratio ** i)  # 边长
    print(r)
    # rt(90)#"正方形圆弧图块整体"右转90度绘制
    #square_sector(r,color_ls[i])
    square_sector(r, color_ls[i])

t.hideturtle()
done()
