#http://www.grantjenks.com/docs/freegames/tiles.html
'''
 puzzle game of sliding numbers into place. Click a tile adjacent to the empty
 square to swap positions. Can you make the tiles count one to fifteen from left
 to right and bottom to top?
 滑动数字到位的益智游戏。点击空方块相邻的瓷砖来交换位置。你能让瓷砖从左到右、
 从下到上数出一到十五吗？
'''
from random import *
from turtle import *
from freegames import floor, vector
import turtle
tiles = {}
neighbors = [
    vector(100, 0),
    vector(-100, 0),
    vector(0, 100),
    vector(0, -100),
]

def load():
    "Load tiles and scramble."100
    count = 1

    for y in range(-200, 200, 100):
        for x in range(-200, 200, ):
            mark = vector(x, y)
            tiles[mark] = count
            count += 1

    tiles[mark] = None

    for count in range(1000):
        neighbor = choice(neighbors)
        spot = mark + neighbor

        if spot in tiles:
            number = tiles[spot]
            tiles[spot] = None
            tiles[mark] = number
            mark = spot

def square(mark, number):
    "Draw white square with black outline and number."
    import turtle
    turtle.up()
    turtle.goto(mark.x, mark.y)
    turtle.down()

    turtle.color('black', 'white')
    turtle.begin_fill()
    for count in range(4):
        turtle.forward(99)
        turtle.left(90)
    turtle.end_fill()

    if number is None:
        return
    elif number < 10:
        turtle.forward(20)

    turtle.write(number, font=('Arial', 60, 'normal'))

def tap(x, y):
    "Swap tile and empty square."
    x = floor(x, 100)
    y = floor(y, 100)
    mark = vector(x, y)

    for neighbor in neighbors:
        spot = mark + neighbor

        if spot in tiles and tiles[spot] is None:
            number = tiles[mark]
            tiles[spot] = number
            square(spot, number)
            tiles[mark] = None
            square(mark, None)

def draw():
    "Draw all tiles."
    for mark in tiles:
        square(mark, tiles[mark])
    turtle.update()

turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)
load()
draw()
turtle.onscreenclick(tap)
done()