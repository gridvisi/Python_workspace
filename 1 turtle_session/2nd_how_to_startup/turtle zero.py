import turtle
#turtle.forward(100)
import turtle
t = turtle.Pen()  #获得画笔
t.hideturtle()  #隐藏海龟
t.speed(200)
t.fillcolor("green")  #设置填充颜色为红色
t.begin_fill()    #开始填充
for x in range(1, 360):
    t.forward(2)
    t.left(1)  #在这里先向右直行，然后左转216°(左下，正五角星度数180/5=36°)
import math
for y in range(5):

    t.forward(360//round(math.pi,1))
    t.left(90)
t.end_fill()     #填充完成
turtle.done()


import math

print(abs(-1-0)) #绝对值

#left : 2 - 1
#right : - 1


#1-100

# please computer help me add number from 1 to 100?
# 从1 加到 100？ 可否？
print([i for i in range(1,51)])

print(sum([i for i in range(1,51)]))

#pie

print(math.sqrt(9)) #square 9 m2 side = ？
print(math.floor(5.6))

import turtle
#turtle.forward(100)

#import turtle
t = turtle.Pen()  #获得画笔
t.hideturtle()  #隐藏海龟
t.fillcolor("red")  #设置填充颜色为红色
t.begin_fill()    #开始填充
for x in range(1, 6):
    t.forward(300)
    t.left(216)  #在这里先向右直行，然后左转216°(左下，正五角星度数180/5=36°)
t.end_fill()     #填充完成


"""
功能：角星的绘制
"""
import turtle

def main():
    """
       主函数
    """
    count = 1
    while count <= 5:
        turtle.forward(100)   #向前走50
        turtle.right(144)    #向右转144度
        count = count + 1
    turtle.exitonclick()
if __name__ == '__main__':
    main()


'''

turtle.pensize(5)
import turtle
turtle.pensize(5)
turtle.pencolor("red")
turtle.fillcolor("purple")
turtle.begin_fill()
for _ in range(5):
    turtle.forward(200)
    turtle.right(144)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(-150,-120)
    turtle.color("red")
    turtle.write("Done", font=('Arial', 20, 'normal'))
turtle.done()
'''
'''
reset()
fillcolor('red')
begin_fill()
circle(100,180)
end_fill()
'''
