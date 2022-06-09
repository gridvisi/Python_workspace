'''
数学和编程解倒水问题总结   B座17楼 5月23日

'''
p = 15
q = 9

def gcd(p,q):
    while p!= q:
        if p > q:
            p = p - q
        else:q = q - p
    return q

p,q = 15,9
print(gcd(p,q))

if p > q:
    ls = [i*gcd(p,q) for i in range(1,p) if i*gcd(p,q) <= p]
else:
    ls = [i*gcd(p,q) for i in range(1,q) if i*gcd(p,q) <= q]
print(ls)
#output：[3, 6, 9, 12, 15, 18, 21, 24]

p = 15
q = 9
v = 11
m = v - q

res = [i+m for i in ls if i+m <= q+p]
print(res)
#output:[5, 8, 11, 14, 17, 20, 23]

set(res + ls)
volume_in = set(ls + res)

volume_not_in = [i for i in range(0,p+q) if i not in volume_in ]
print(volume_in,volume_not_in)

