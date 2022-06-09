'''
https://blog.csdn.net/apple_hzc/article/details/82767327
'''
#假设屋里有5个人，收入排序后显示
pay = [ 3000,4500,15000,20000,25000]
pay.append(120000)
mean = sum(pay) / len(pay) #平均值 ​
median = pay[2] = 15000 #中位数

print(mean,median)

arr = [ 6, 4, 2, 6, 10]
print(sorted(arr))
def fruit(arr):
    res,arrs = [],arr
    for x in range(1,100):
        arrs.append(x)
        fruit_mean = sum(arr)/len(arr)
        if len(arrs) % 2 == 1:
            fruit_median = sorted(arrs)[1 +len(arr)//2]
            if fruit_mean == fruit_median:
                res.append(x)
            arrs.remove(x)
        elif len(arrs) % 2 == 0:
            st, nd = len(arrs)//2-1, 1+len(arrs) // 2
            ls = sorted(arrs)[st:nd]
            fruit_median = (sum(ls)) / 2
            if fruit_mean == fruit_median:
                print(fruit_median)
                res.append(x)
            arrs.remove(x)
    return res

print(fruit(arr))

from numpy import median
weights = [6, 4, 2, 6, 10]
for i in range(100):
    mean_weights = (sum(weights) + i)/(len(weights) + 1)
    median_weights = median(weights + [i])
    if mean_weights == median_weights:
        print(f"{i}")
#如果不想换行可以用 print(xxx,end='')

import numpy as np
A = np.random.randn(1,2)
print("A is:",A)

np.random.seed(2)
B = np.random.randn(1,3)
print("B is:", B)

import numpy
arr = [1,2,3,4]
#shape = (2,4)
array = numpy.array([[1,2,3],[4,5,6],[7,8,9]])

print(array)

print(np.arange(1,11,3))  # 1D array
fruit = np.random.randint(1,11,size = (5,5))
print('fruit = ',fruit)

num = 0
while(num<5):
    np.random.seed(2)
    print(np.random.random())
    num+=1
