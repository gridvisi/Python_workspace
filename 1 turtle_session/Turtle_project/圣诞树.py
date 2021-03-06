
import turtle as t
from turtle import *
import random
import time

n = 80.0
t.speed(1000)
t.screensize(bg = "seashell")
t.left(90)
t.forward(3*n)
t.color("orange","yellow")
t.begin_fill()

t.left(126)
for i in range(5):
    t.forward(n/5)
    t.left(72)
t.end_fill()

t.right(126)
t.color("dark green")

t.backward(n * 4.8)

def tree(d,s):
    if d<= 0:return
    t.forward(s)
    tree(d-1,s*.8)
    t.right(120)
    tree(d-3,s*.5)
    t.right(120)
    tree(d - 3, s * .5)
    t.right(120)
    t.backward(s)

tree(15,n)
t.backward(n/2)

for i in range(200):
    a = 200 - 400*random.random()
    b = 10 - 20*random.random()
    t.up()
    t.forward(b)
    t.left(90)
    t.forward(a)
    t.left(90)
    t.forward(a)
    t.down()
    if random.randint(0,1) == 0:
        t.color("tomato")
    else:
        t.color("wheat")

    t.circe(2)
    t.up()
    t.backward(a)
    t.right(90)
    t.backward(b)
