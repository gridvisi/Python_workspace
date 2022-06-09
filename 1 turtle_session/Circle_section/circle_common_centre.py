
import turtle  # 绘图库

def describing_circle(radii):
    # 页面的大小
    turtle.setup(width=900, height=500)
    # 颜色
    turtle.color('blue' ,'red'  )  # 同时给笔和内部区域设置颜色
    # 笔粗细
    turtle.pensize(3)
    # 速度
    turtle.Turtle().screen.delay(2  )  # 设置速度 并且取消延迟
    # 隐藏画笔
    turtle.hideturtle()
    # 抬起画笔
    turtle.penup()
    # 将画笔移动到0，-200的坐标点去
    turtle.goto(0 ,-radii)
    # 放下画笔 开始画
    turtle.pendown()
    # 需要进行填充
    turtle.begin_fill()
    # 半径是200的圆（正数表示从下面往上画）
    turtle.circle(radii)
    # 结束填充
    turtle.end_fill()

    # 抬起画笔
    turtle.penup()
    # 设置圆心点的颜色
    turtle.color('black' ,'black'  )  # 同时给笔和内部区域设置颜色
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


describing_circle(200  )  # 画圆的函数 传入圆的半径

# 点击窗口关闭
window =turtle.Screen()
window.exitonclick()
