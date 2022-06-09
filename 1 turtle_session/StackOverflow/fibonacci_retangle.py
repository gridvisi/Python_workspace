
from turtle import Screen, Turtle

SCALE = 5
CURSOR_SIZE = 20

square = Turtle('square', visible=False)
square.fillcolor('green')  #'white'
square.speed('fastest')
square.right(90)
square.penup()

previous_scaled, previous, current = 0, 0, 1
colors = 2* ['red','orange','yellow','green','blue','purple','pink']
for i in range(14):
    square.fillcolor(colors[i])
    current_scaled = current * SCALE
    square.forward(current_scaled/2 + previous_scaled/2)
    square.shapesize(current_scaled / CURSOR_SIZE)
    square.left(90)
    square.forward(current_scaled/2 - previous_scaled/2)
    square.stamp()
    previous_scaled, previous, current = current_scaled, current, current + previous

screen = Screen()
screen.exitonclick()