import turtle as t
from random import randint
t.bgcolor("black") #purple, orange, red, yellow,blue,light blue, grey,
x = 1
t.speed(0)
while x < 400:
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    t.colormode(255)
    t.pencolor(r,g,b) #red,blue,green
    t.fd(50 + x)
    t.rt(90.99)
    x += 1
t.exitonclick()
