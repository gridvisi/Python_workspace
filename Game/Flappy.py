
"""Flappy, game inspired by Flappy Bird.
# 愤怒的小鸟
Exercises

1. Keep score.
2. Vary the speed.
3. Vary the size of the balls.
4. Allow the bird to move forward and back.

"""

from random import *
from turtle import *
import turtle as t
from freegames import vector

bird = vector(0, 0)
balls = []

def tap(x, y):
    "Move bird up in response to screen tap."
    up = vector(0, 30)
    bird.move(up)

def inside(point):
    "Return True if point on screen."
    return -200 < point.x < 200 and -200 < point.y < 200

def draw(alive):
    "Draw screen objects."
    t.clear()

    t.goto(bird.x, bird.y)

    if alive:
        t.dot(10, 'green')
    else:
        t.dot(10, 'red')

    for ball in balls:
        t.goto(ball.x, ball.y)
        t.dot(20, 'black')

    t.update()

def move():
    "Update object positions."
    bird.y -= 5

    for ball in balls:
        ball.x -= 3

    if randrange(10) == 0:
        y = randrange(-199, 199)
        ball = vector(199, y)
        balls.append(ball)

    while len(balls) > 0 and not inside(balls[0]):
        balls.pop(0)

    if not inside(bird):
        draw(False)
        return

    for ball in balls:
        if abs(ball - bird) < 15:
            draw(False)
            return

    draw(True)
    t.ontimer(move, 50)

t.setup(420, 420, 370, 0)
t.hideturtle()
t.up()
t.tracer(False)
t.onscreenclick(tap)
move()
done()