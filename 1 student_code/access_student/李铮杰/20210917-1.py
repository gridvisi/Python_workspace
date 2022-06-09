
import turtle
turtle.pensize(0.0)
turtle.pencolor("blue")
turtle.fillcolor("black")
turtle.color('purple')
turtle.begin_fill()
for _ in range(50):
    turtle.forward(200)
    turtle.left(500)
    turtle.color("gray")
    turtle.write("vector", font=('Arial', 5, 'normal'))
turtle.done()
