__author__ = 'lizhenjie'
import turtle
turtle.pensize(5)
turtle.pencolor("blue")
turtle.forward(200)
turtle.right(90)

turtle.fillcolor("black")
turtle.forward(200)
turtle.right(90)

turtle.color('purple')
turtle.begin_fill() #开始填充

for _ in range(5):
    turtle.forward(200)
    turtle.right(90)
    #turtle.end_fill()
    #turtle.penup()
    #turtle.goto(-150,-120)
    turtle.color("gray")
    turtle.write("mccree", font=('Calibri', 15, 'normal'))
turtle.end_fill()  #结束填充
turtle.done()