
#10转2
jieguo=[]
def zhuanhua (n):
    while n:
        jieguo.append(n%2)
        n = n//2
    return jieguo[::-1]

print(zhuanhua(31))

h = 150
w = 73
import math
print(w*(170/150)**3)