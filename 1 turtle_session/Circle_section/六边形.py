#from turtle import *
import turtle
#import time
t = turtle
# 画一个六边形
def onesix(l, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(l, steps=6)
    t.color('black', 'orange')
    t.end_fill()
#time.sleep(10)
print(onesix(10,10,10))

#画r圈六边形
def rsix(l,r):
	xyset=set()
	findxy(r,xyset)
	for x,y in xyset:
		onesix(l,x,y)

def findxy(r, xyset=set()):
    x, y = 0, 0
    xyset.add((x, y))
    for i in range(r):
        xyempty = set()
        for x, y in xyset:
            xyempty.add((x + (3 ** 0.5) * l, y))
            xyempty.add((-x - (3 ** 0.5) * l, y))
            xyempty.add((x + (3 ** 0.5) * l / 2, y + 3 * l / 2))
            xyempty.add((-x - (3 ** 0.5) * l / 2, y + 3 * l / 2))
            xyempty.add((x + (3 ** 0.5) * l / 2, -y - 3 * l / 2))
            xyempty.add((-x - (3 ** 0.5) * l / 2, -y - 3 * l / 2))
        xyset |= xyempty


# tracer(False) #不要动画，不知道为什么用了这句语句后，最后一笔总是写不了，有个六边形会少一个边
t.speed(10)  # 速度会很慢
t.hideturtle()
l = 20  # 一个六边形的边的长度
r = 6  # 蜂窝的圈数
rsix(l, r)
t.done()