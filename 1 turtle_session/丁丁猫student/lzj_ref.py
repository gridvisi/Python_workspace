import turtle as t
import random
from random import randint

width,height = 100,100
t.goto(width / 2, randint(-height / 2, height / 2))
stars = []
for i in range(170):
    star = t.clone()
    s = random.randint(1,2) / 3
    star.shapesize(s, s)
    star.speed(int(s * 10))
    star.setx(width / 2 + randint(1, width))
    star.sety(randint(-height / 2, height / 2))
    star.showturtle()
    stars.append(star)
while True:
    for star in stars:
        star.setx(star.xcor() - 3 * star.speed())
        if star.xcor() < -width / 2:
            star.hideturtle()
            star.setx(width / 2 + randint(1, width))
            star.sety(randint(-height / 2, height / 2))
            star.showturtle()