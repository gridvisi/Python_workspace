__author__ = 'Administrator'
'''
一个活塞门做到流畅如多米诺骨牌，如何设定定时器是关键，决定每个活塞触发的时间。
第n个活塞触发时间为前n-1，n-2，直到1的时间之和：f(n)=f(n-1)+f(n-2)+f(n-3)...f(1)
'''
'''
f=[]
f[1]=1
f[2]=2
for i in range(6):
    f.append()
'''
def f(n):
    if n == 1:
        return 0.1
    if n == 2:
        return 0.2
    if n == 3:
        return f(1)+f(2)
    else:
        return 2*f(n-1)

print(f(10))






