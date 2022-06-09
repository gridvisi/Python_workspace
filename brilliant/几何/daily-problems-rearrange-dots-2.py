'''
https://brilliant.org/daily-problems/rearrange-dots-2/
'''

def triangle(x):
    return sum([i for i in range(1,x+1)])

def triangle_tower(n):
    unit = sum([i for i in range(1,n+1)])
    # 3个塔形垒起的小三角构成：(n)*(1 + n)/2
    #if n==1: return 3*unit
    #if n==2: return 3*
    #3 * (n)*(1 + n)/2
    return 3*unit

print([triangle_tower(i) for i in range(1,10)])