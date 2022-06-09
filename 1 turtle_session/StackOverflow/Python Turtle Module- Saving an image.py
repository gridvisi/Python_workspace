
#1st
from turtle import *
from random import *
import time

def randomcolour():
    colormode(255)
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    color(red, green, blue)

def randomplace():
    penup()
    x = randint(-100, 100)
    y = randint(-100, 100)
    goto(x, y)
    pendown()

def randomheading():
    heading = randint(0, 360)
    setheading(heading)

def drawrectangle():
    randomcolour()
    randomplace()
    hideturtle()
    length = randint(10, 100)
    height = randint(10, 100)
    begin_fill()
    forward(length)
    right(90)
    forward(height)
    right(90)
    forward(length)
    right(90)
    forward(height)
    right(90)
    end_fill()

    shape("turtle")
    speed(0)

for i in range(1, 30):
  randomcolour()
  randomplace()
  randomheading()
  stamp()



def drawcircle():
  radius = randint(5, 100)
  randomcolour()
  randomplace()
  dot(radius)

def drawstar():
    randomcolour()
    randomplace()
    randomheading()
    begin_fill()
    size = randint(20, 100)

    for side in range(5):
        left(144)
        forward(size)

        end_fill()

clear()
setheading(0)

for i in range(20):
  drawrectangle()

clear()

for i in range(50):
  drawcircle()

clear()

for i in range(20):
    sleep(5000)
    drawstar()

#2nd


from turtle import *  # @UnusedWildImport

import svgwrite

from svg_turtle import SvgTurtle


def draw_spiral():
    fillcolor('blue')
    begin_fill()
    for i in range(20):
        d = 50 + i*i*1.5
        pencolor(0, 0.05*i, 0)
        width(i)
        forward(d)
        right(144)
    end_fill()


def write_file(draw_func, filename, size):
    drawing = svgwrite.Drawing(filename, size=size)
    drawing.add(drawing.rect(fill='white', size=("100%", "100%")))
    t = SvgTurtle(drawing)
    Turtle._screen = t.screen
    Turtle._pen = t
    draw_func()
    drawing.save()


def main():
    write_file(draw_spiral, 'example.svg', size=("500px", "500px"))
    print('Done.')


if __name__ == '__main__':
    main()