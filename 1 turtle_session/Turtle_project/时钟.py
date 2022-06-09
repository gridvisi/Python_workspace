
# 需要导入模块: import turtle [as 别名]
# 或者: from turtle import mainloop [as 别名]

import turtle
from turtle import mainloop
def start():
    # 不显示绘制时钟的过程
    turtle.tracer(False)
    turtle.mode('logo')
    turtle.createHand('second_hand', 150)
    turtle.createHand('minute_hand', 125)
    turtle.createHand('hour_hand', 85)
    # 秒, 分, 时
    second_hand = turtle.Turtle()
    second_hand.shape('second_hand')
    minute_hand = turtle.Turtle()
    minute_hand.shape('minute_hand')
    hour_hand = turtle.Turtle()
    hour_hand.shape('hour_hand')
    for hand in [second_hand, minute_hand, hour_hand]:
        hand.shapesize(1, 1, 3)
        hand.speed(0)
    # 用于打印日期等文字
    printer = turtle.Turtle()
    printer.hideturtle()
    printer.penup()
    turtle.createClock(160)
    # 开始显示轨迹
    turtle.tracer(True)
    turtle.startTick(second_hand, minute_hand, hour_hand, printer)
    turtle.mainloop()

start()