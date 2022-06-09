
import turtle
pen = turtle.Turtle()
pen.color('red')
pen.speed(100)
pen.hideturtle()

pen.penup()
pen.goto(-100,-100)
pen.pendown()

def draw_triangle(length):
    pen.setheading(180)
    for i in range(3):
        pen.rt(120)
        pen.fd(length)
def sierpinski_order_n_recursive(n ,length):
    if n == 1:
        draw_triangle(length)
    else:
        sierpinski_order_n_recursive(n-1,length)
        pen.rt(120)
        pen.fd(length*2**(n-2))
        sierpinski_order_n_recursive(n-1,length)
        pen.lt(120)
        pen.fd(length*2**(n-2))
        sierpinski_order_n_recursive(n- 1, length)
        pen.fd(length*2**(n-2))

sierpinski_order_n_recursive(6,8)

turtle.done()