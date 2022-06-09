'''
Your task is to find the nearest square number, nearest_sq(n), of a positive integer n.
round() 方法返回浮点数x的四舍五入值。
'''
import math
def nearest_sq(n):
    lower = abs(n - int(math.sqrt(n))**2)
    high = abs(n - (math.ceil(math.sqrt(n))**2))
    if lower < high:
        return int(math.sqrt(n))**2
    return math.ceil(math.sqrt(n))**2
print(nearest_sq(111))