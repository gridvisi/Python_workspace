__author__ = 'Administrator'
'''
https://blog.csdn.net/u012560212/article/details/72500152

list=[1,2,5,9,4,6,3]
>>> max(list,key=lambda x:-x)#以-x的大小对原列表排序

Given n non-negative integers representing the histogram's ' \
'bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

while i < (len(given_height)-1):
    while j < len(given_height):

    #given_height = sorted([3,6,1,3,5])
    #print(given_height)
        if given_height[i] <= given_height [j]:
            x = given_height[i]
            temp.append(x)

        x = given_height[j]
        j += 1
        temp.append(x)
    i += 1

    h = max(temp)
print(temp,h)
'''
import math
heights = [2,1,5,6,2,3,3,7,6,9,9,8,99,23,1,33]

def largestRectangleArea(heights):
    area =[]
    j = 1
    i = 0
    while i < (len(heights)-1) and j < len(heights):
        if heights[i] <= heights[j]:
            x = heights[i]
            area.append(x)

        if  heights[i] > heights [j]:
            x = heights[j]
            area.append(x)
        j += 1
        i += 1
    return max(area)
print(largestRectangleArea(heights))





