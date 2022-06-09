'''
https://www.codewars.com/kata/5bb3e299484fcd5dbb002912/train/python
For more examples,

pyramid(1) == 1

pyramid(3) == 2

pyramid(6) == 3

pyramid(10) == 4

pyramid(15) == 5
Write a function that takes number of balls (≥ 1) and calculates how many levels you can build a triangle.

'''


import math
def pyramid(balls):
    #i = 3
    layer = int(math.sqrt(2*balls))
    print(layer)
    while (layer) * (layer+1) <= 2*balls:
        layer += 1
        if layer * (layer+1) == balls:
            return layer
    return layer-1


# cool!
def pyramid(balls):
    count = 0
    while balls > count:
        count += 1
        balls -= count
    return count

#
def pyramid(balls):
    return ((8*balls + 1)**.5 - 1) // 2



balls = 9999
balls = 4
print(pyramid(balls))