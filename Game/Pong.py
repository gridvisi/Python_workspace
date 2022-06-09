
"""Pong, classic arcade game.

Exercises

1. Change the colors.
2. What is the frame rate? Make it faster or slower.
3. Change the speed of the ball.
4. Change the size of the paddles.
5. Change how the ball bounces off walls.
6. How would you add a computer player?
6. Add a second ball.

"""

from random import choice, random
from turtle import *
from freegames import vector
import turtle as Pen
def value():
    "Randomly generate value between (-5, -3) or (3, 5)."
    return (3 + random() * 2) * choice([1, -1])

ball = vector(0, 0)
aim = vector(value(), value())
state = {1: 0, 2: 0}

def move(player, change):
    "Move player position by change."
    state[player] += change

def rectangle(x, y, width, height):
    "Draw rectangle at (x, y) with given width and height."
    Pen.up()
    Pen.goto(x, y)
    Pen.down()
    Pen.begin_fill()
    for count in range(2):
        Pen.forward(width)
        Pen.left(90)
        Pen.forward(height)
        Pen.left(90)
    Pen.end_fill()

def draw():
    "Draw game and move pong ball."
    Pen.clear()
    rectangle(-200, state[1], 10, 50)
    rectangle(190, state[2], 10, 50)

    ball.move(aim)
    x = ball.x
    y = ball.y

    Pen.up()
    Pen.goto(x, y)
    Pen.dot(10)
    Pen.update()

    if y < -200 or y > 200:
        aim.y = -aim.y

    if x < -185:
        low = state[1]
        high = state[1] + 50

        if low <= y <= high:
            aim.x = -aim.x
        else:
            return

    if x > 185:
        low = state[2]
        high = state[2] + 50

        if low <= y <= high:
            aim.x = -aim.x
        else:
            return

    Pen.ontimer(draw, 50)

Pen.setup(420, 420, 370, 0)
Pen.hideturtle()
Pen.tracer(False)
Pen.listen()
Pen.onkey(lambda: move(1, 20), 'w')
Pen.onkey(lambda: move(1, -20), 's')
Pen.onkey(lambda: move(2, 20), 'i')
Pen.onkey(lambda: move(2, -20), 'k')
draw()
done()

