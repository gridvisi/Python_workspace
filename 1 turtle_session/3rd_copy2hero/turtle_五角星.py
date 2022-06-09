import turtle
#import time
# right  left
turtle.circle(17)
for _ in range(5):
    turtle.circle(7)
    turtle.forward(100)
    turtle.pencolor("red")
    turtle.left(90)



turtle.goto(-90, 30)
#st = time.time()
turtle.pensize(0.7)
turtle.pencolor("yellow")
turtle.fillcolor("red")
turtle.fillcolor("green")
turtle.begin_fill()
for _ in range(5):
    turtle.forward(200)
    turtle.right(144)
turtle.end_fill()
#time.sleep(2)

turtle.penup()
turtle.goto(-150, -180)
turtle.color("violet")
turtle.write("Done", font=('Arial', 40, 'normal'))
turtle.mainloop()

import time
st = time.time()
print('s')
end = time.time()
print('共耗费时长：',st - end) # 为何为负数？
turtle.done()
