'''
 假设地球是一个密度均匀的完美球体。距离地球R的高度自由落体，地球的半径是R = 6370公里，这个无底洞将会有12740公里长，整个过程仅仅耗费大约40分钟，一天就是17个来回！
R是地球的半径，g是地球表面重力引起的加速度。k = 1.42745

https://brilliant.org/problems/looking-down-into-the-earth/
'''

#
import math
R = 6370000
#if high_to_earth = R or high_to_earth = 0:
g = 9.8
k = 1.42745
sec = k * math.sqrt(R/g)
minu = sec/60
cycle = 24*60/minu
print(sec,minu,cycle)

def hilarious(n):
    j = 1
    i = 0
    s = 0
    while i < n:
        i += j
        s += 1
        j += 1
        print(i,s,j)
    return s
n = 99
print(hilarious(n))
