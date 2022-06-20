__author__ = 'Administrator'
'''
import numpy
a = numpy.array([[1,2,4],[4,5,6]])
b = numpy.array([[1,2,4,6],[4,5,6,9],[4,5,6,9]])

for a in arrays:
    if max(b.shape[:-2])!=min(b.shape[:-2]):

x = max(b.shape[:-1])
print(x)
print (a.shape[:-1])
print (b.shape[:-2])
print(b.shape)

def trans(m):
    a = [[] for i in m[0]]
    for i in m:
        for j in range(len(i)):
            a[j].append(i[j])
    return a

m = [[1, 2], [3, 4], [5, 6]]    # 想象第一个列表是原始的，后面的是往里添加的
print (trans(m))   # result:[[1, 3, 5], [ 2, 4, 6]]


import numpy as np

print(np.dot(3, 4.0))       # 12.0

a = np.array([[1, 2, 3],
              [2, 3, 4]])
b = np.array([2, 2, 2])
c = np.array([2, 2, 2])

print(np.dot(a, b))         # [12 18] 实现矩阵乘法
print(np.dot(b, c))
'''

import numpy as np
from scipy.linalg import solve
a = np.array([[3, 1, -2, 1], [1, -1, 4, 1], [2, 0, 3, 1]])
b = np.array([5, -2, 2.5])
x = solve(a, b)
print(x)
