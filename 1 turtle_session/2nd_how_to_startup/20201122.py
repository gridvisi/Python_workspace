import turtle
import time
turtle.forward(100)
turtle.pencolor("white")
#turtle.done()

turtle.goto(-90, 30)
st = time.time()
turtle.pensize(5)
turtle.pencolor("yellow")
turtle.fillcolor("yellow")

turtle.begin_fill()
for _ in range(5):
    turtle.forward(200)
    turtle.right(144)
turtle.end_fill()
time.sleep(2)

turtle.penup()
turtle.goto(-150, -180)
turtle.color("violet")
turtle.write("Done", font=('Arial', 40, 'normal'))
turtle.mainloop()

end = time.time()
print('共耗费时长：',st - end) # 为何为负数