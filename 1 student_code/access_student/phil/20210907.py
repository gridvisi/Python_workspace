
import turtle as t
t.speed(0)
t.penup()
t.goto(0,-300)
t.pendown()
color = ['red','orange','yellow','green','blue']
i = 0
r = 5
t.fillcolor(color[i])
t.begin_fill()
for i in range(5):
    r -= 1  #r = r-1, r-1
    i += 1
    t.fillcolor(color[i%5]) #技巧点取余运算避免超出列表长度
    t.begin_fill()

    t.penup()
    t.goto(0, -300 + i*300//5) #0,0
    t.pendown()

    for j in range(360):
        t.forward(r)
        t.left(1)
    t.end_fill()