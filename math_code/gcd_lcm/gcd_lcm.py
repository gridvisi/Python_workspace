

r,R = 12,48 #大小齿轮的齿数
n = 1  #初始化
#大小齿轮数不为零的前提下，编码
if r < R:
    r, R = R, r  # 如果r小于R,交换赋值,保证r大于R
r,R = max(r,R),min(r,R)

while n*r%R != 0:
    n += 1
print(n*r)

# Python已有 gcd 函数，gcd可得到最大公约数
# 由最大公约数求最小公倍数

import math
lcm = r * R / math.gcd(r,R)
print(lcm)

#2 欧几里得法
r,R = 12,48
def gcd_while(r,R):
    if r > R:
        r, R = R, r
    while R != 0:
        r,R = R,r%R
    return r
print(gcd_while(r,R))

a,b = 18,12
def gcd(a,b):
    if a % b == 0:
        return b
    else:
        return gcd(b,a%b)
print(gcd(a,b))

r,R = 12,18

def gcd_recur(r,R):
    if r%R == 0:
        return R
    else:
        return gcd_recur(R,r % R)
print(gcd_recur(r,R))





