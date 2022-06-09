'''
https://brilliant.org/daily-problems/sum-of-ages/

The product of Ivy's, Joshua's, Kylie's, and Logan's ages is 1296.
1296.Which of these numbers cannot be the sum of their ages?

23  24 25  26


'''
# Hint: 周长一定的前提下，矩形中正方形面积最大，任意形状是圆形面积最大
# 逻辑推理可得，面积相同的前提下，正方形的周长最小，圆形的周长最小
import math
root = math.sqrt(math.sqrt(1296))
print(root)

'''
his means the sum of all four ages cannot be smaller than 24.24.

For completeness, their ages are

6, 6, 6,6,6,6, and 66 for the sum to be 24;24;
4, 6, 6,4,6,6, and 99 for the sum to be 25;25;
3, 6, 8,3,6,8, and 99 for the sum to be 26.26.
'''