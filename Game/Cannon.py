
"""Cannon, hitting targets with projectiles.
#  有小同学想学习python写小游戏，老师邮件发给到邮箱。加农炮射击类游戏，
#  熟悉重力影响，炮弹运动呈现抛物线的特点，命中右边的红色点；
 同学想学习python写小游戏，源码先邮件发给到邮箱。同学感受到简单的游戏需要掌握编程知识点和技
巧一点不简单！一个加农炮射击类游戏，熟悉重力影响，炮弹运动呈现抛物线的特点，命中右边的红色点；任务式学习打破孤立的知识点，活学活用起来！
Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.

"""

from random import randrange
from turtle import *
import turtle as t
from freegames import vector
t.setup(width=1400, height=800)

ball = vector(-500, -500)
speed = vector(0, 0)
targets = []
#炮弹的初速度是恒定的，命中目标靠角度

def tap(x, y):
    "Respond to screen tap."
    #每次发射一颗炮弹，先判断活动区域有无炮弹！
    if not inside(ball):
        ball.x = -399
        ball.y = -399
        #炮弹出发的固定位置坐标
        speed.x = (x + 20) / 5
        speed.y = (y + 20) / 5
        #炮弹的位置横竖轴坐标运动时的变化

def inside(xy):
    "Return True if xy within screen."
    return -400 < xy.x < 400 and -400 < xy.y < 400

def draw():
    "Draw ball and targets."
    t.clear()

    for target in targets:
        t.goto(target.x, target.y)
        t.dot(20, 'green')
        #目标的颜色和直径

    if inside(ball):
        #先判断是否在规定的活动区域
        t.goto(ball.x, ball.y)
        t.dot(17, 'red')
        # 炮弹的颜色和直径

    t.update()

def move():
    "Move ball and targets."
    #随机生成蓝色目标的高度，并保持高度不变且匀速向左移动
    #实现红色炮弹运动受重力影响表现

    if randrange(40) == 0:
        y = randrange(-170, 170)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 0.5
        #蓝色目标向左匀速移动

    if inside(ball):
        speed.y -= 0.5
        ball.move(speed)
        #y方向速度匀速减少是重力加速度

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 50:
            #命中的精度要求
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target):
            return

    t.ontimer(move, 30)
    #目标和炮弹的初速度

t.setup(720, 720, 370, 0)
#活动的窗口尺寸
t.hideturtle()
t.penup()
t.tracer(False)
t.onscreenclick(tap)
move()
done()