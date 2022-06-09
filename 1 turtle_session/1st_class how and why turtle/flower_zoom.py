#from turtle import *
import turtle as t
t.color('black', 'magenta')
#length,size = 100,50

def left_turn(length):
    for i in range(10):
        t.forward(length / 10)
        t.left(9)


def petal(size):
    t.begin_fill()
    left_turn(size)
    t.left(90)
    left_turn(size)
    t.left(90)
    t.end_fill()


for i in range(0, 200, 10):
    petal(i)
    t.right(360 / 10)

t.done()