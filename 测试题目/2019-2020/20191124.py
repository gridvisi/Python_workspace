import turtle
turtle.screensize(800,600, "light green")


'''

'''
# coding=utf-8
import turtle
import time
turtle.speed(1)

turtle.pensize(5)
turtle.pencolor("blue")
turtle.fillcolor("blue")

for _ in range(4):
    turtle.forward(210)
    turtle.left(90)
    #turtle.forward(210)

turtle.done()

turtle.begin_fill()
for _ in range(3):
    turtle.forward(210)
    turtle.right(120)
turtle.penup()
turtle.forward(70)
turtle.left(60)
turtle.forward(70)
turtle.backward(0)

turtle.penup()
turtle.pensize(5)
turtle.pencolor("yellow")
#turtle.fillcolor("white")
for _ in range(3):
    turtle.right(120)
    turtle.forward(210)
turtle.penup()

turtle.backward(70)
turtle.right(60)
turtle.forward(70)
turtle.end_fill()
time.sleep(2)

turtle.penup()
turtle.goto(-150, -120)
turtle.color("violet")
turtle.write("Done", font=('Arial', 40, 'normal'))

turtle.mainloop()

# coding=utf-8
import turtle
import time

# 同时设置pencolor=color1, fillcolor=color2
turtle.color("red", "yellow")

turtle.begin_fill()
for _ in range(50):
    turtle.forward(200)
turtle.left(170)
turtle.end_fill()

turtle.mainloop()
turtle.done()


'''
def draw1():
    reset()
    speed(10)
    for i in range(36):
        forward(200)
        left(170)
reset()
speed(10)
draw1()

#彩色螺旋线
import turtle
turtle.pensize(2)
turtle.bgcolor("black")
colors = ["red","yellow","purple","blue"]
turtle.tracer(False)
for x in range(400):
    turtle.forward(2*x)
    turtle.color(colors[x % 4])
    turtle.left(91)
turtle.tracer(True)
turtle.done()

'''
