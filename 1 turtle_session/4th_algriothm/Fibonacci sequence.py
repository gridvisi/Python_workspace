import turtle as t

wn = t.Screen()
wn.bgcolor("white")
from turtle import *

prev = 0
start = 1
fibonacci = 1
sqs = input("How many Squares do you want?")
for i in range(int(sqs)):
    print(str(i) + ". " + str(fibonacci))

    t.color('black')
    for f in range(6):
        t.forward(5 * fibonacci)
        if f < 5: t.right(90)

    fibonacci = start + prev
    prev = start
    start = fibonacci

t.done()