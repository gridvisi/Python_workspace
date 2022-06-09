
import turtle
t = turtle
# 画笔放在画布正中央：
t.goto(0,0) #


# 从位置 0,-100, 正中央的下方100的位置开始，走一条长度为100的直线
t.up()  #抬笔 ，不显示笔迹
t.goto(0,-100)
t.down() #落笔 ， 开始显示笔迹
t.forward(100)

#画一个半径为100的圆形
t.pencolor("blue")
turtle.circle(50)

#一个正方形
t.pencolor("red")
for i in range(5):
    t.forward(100)
    t.pencolor("red")
    t.left(90)

t.done()  # 保持画布不消失
