
# Python program to print complete Koch Curve.
# Koch Snowflake using Python turtle
from turtle import *
import turtle as t
# function to create koch snowflake or koch curve
def snowflake(lengthSide, levels):
    if levels == 0:
        t.forward(lengthSide)
        return
    lengthSide /= 3.0
    snowflake(lengthSide, levels -1)
    t.left(60)
    snowflake(lengthSide, levels -1)
    t.right(120)
    snowflake(lengthSide, levels -1)
    t.left(60)
    snowflake(lengthSide, levels -1)

# main function
if __name__ == "__main__":
    # defining the speed of the turtle
    t.speed(9999)
    length = 300.0

    # Pull the pen up – no drawing when moving.
    # Move the turtle backward by distance, opposite
    # to the direction the turtle is headed.
    # Do not change the turtle’s heading.
    t.penup()

    t.backward(length /2.0)

    # Pull the pen down – drawing when moving.
    t.pendown()
    for i in range(3):
        snowflake(length, 4)
        t.right(120)

        # To control the closing windows of the turtle
    #mainloop()

