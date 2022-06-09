'''
https://medium.com/search?q=python%20turtle
'''

import turtle
import random

# Setup the window with a background color
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle
speedy = turtle.Turtle()
speedy.speed(0)

# Create a list of colors
sfcolor = ["white"]


# Define a function to create different sized snowflakes
def snowflake(size):
    # move the pen into starting position
    speedy.penup()
    speedy.forward(10 * size)
    speedy.left(45)
    speedy.pendown()
    speedy.color(random.choice(sfcolor))
    # draw branch 8 times to make a snowflake
    for i in range(8):
        branch(size)
        speedy.left(45)


# This function creates one branch of the snowflake
def branch(size):
    for i in range(3):
        for i in range(3):
            speedy.forward(10.0 * size / 3)
            speedy.back(10.0 * size / 3)
            speedy.right(45)
        speedy.left(90)
        speedy.back(10.0 * size / 3)
        speedy.left(45)
    speedy.right(90)
    speedy.forward(10.0 * size)


# Loop to create 20 snowflakes of different sizes and at
# different starting locations
for i in range(20):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    sfsize = random.randint(1, 4)
    speedy.penup()
    speedy.goto(x, y)
    speedy.pendown()
    snowflake(sfsize)