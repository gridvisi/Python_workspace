'''
https://www.codewars.com/kata/5a03b3f6a1c9040084001765/train/python
'''
import math
print(math.ceil(3/2))
def angle(n):
    return (180 - math.ceil(360//n)*n)
n = 4
print(angle(n))