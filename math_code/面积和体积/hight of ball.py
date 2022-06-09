__author__ = 'Administrator'
'''
A hemispherical bubble is placed on top of a spherical bubble of radius .
A smaller, second hemispherical bubble is then placed on the first one. This process is continued until
 n hemispheres are placed.
Find the maximum possible height of such a tower with 80 hemispheres on top of the sphere.
半球形气泡位于半径为球形的气泡的顶部。然后，在第一个小气泡上放置一个较小的第二半球形气泡。这个过程一直持续到半球放置。
找到这样一个塔的最大可能高度，在球体的顶部有半球
import math
def hight(r,R,i,layer):
    R = 1
    R + r + math.sqrt(R**2 - r**2)
h = 1 + math.sqrt(2)
h = x + 1 + math.sqrt(1 ** 2 - x ** 2)
print()

import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import fmin,fminbound


def f(x):
    return x**2+10*np.sin(x)+1
x=np.linspace(-10,10,num=500)
min1=fmin(f,3)#求3附近的极小值
min2=fmin(f,0)#求0附近的极小值
min_global=fminbound(f,-10,10)#这个区域的最小值
print(min1)
print(min2)
print(min_global)
plt.plot(x,f(x))
plt.show()
输出：
'''

import math
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import fmin, fminbound
def f(x):
    return x + 1 + math.sqrt(1 ** 2 - x ** 2)
min = fminbound(f, 0, 1)
#print(min)
cache = []
for x in range(9):
    dx = 0.0001 * x
    cache.append(f(dx))
#print(cache)


# (1 + math.sqrt(2))**2 - 2*(1 + math.sqrt(2))*(x+1) +2*x*(x+1) = 1
# 2r²  - 2*√2*r +1 = 0

a = 2
b = - 2 * math.sqrt(2)
c = 1
def quadratic(a, b, c):
    p = b * b - 4 * a * c
    if p >= 0 and a != 0:  #一元二次方程有解的条件
        x1 = (-b + math.sqrt(p)) / (2 * a)
        x2 = (-b - math.sqrt(p)) / (2 * a)
        return x1, x2
    elif a == 0:  #a=0的情况下为一元一次方程
        x1 = x2 = -c / b
        return x1
    else:
        return ('Wrong Number！')

#print(quadratic(a,b,c))
start = 1 + math.sqrt(2)
ratio = 0.5*math.sqrt(2)
sum1 = []
for i in range(40):
    j = ratio**i
    sum1.append(j)
    print(j)
print(len(sum1),sum1)
Hight = start*(sum(sum1)) + 1
print(Hight)
t = math.sqrt(2)
print('susuan:',1+(t + 1)*(1 - t/160)/(1 - t/2))
'''
a = float(input('Please input a='))
b = float(input('Please input b='))
c = float(input('Please input c='))

#f(x):--　９９９　　> 2.4142118327167372, 2.4142135462503527, 2.4142124326291627
#print(math.sqrt(2))：　　　　　　　　　　　1.4142135623730951
#f(x):-＿９９９９　-> 2.4142135462503527, 2.414213562308064,　2.4142135500823163
'''