'''
1  =  1 square 平方
1+3 = 2 square平方
1+3+5 = 3 square平方
1+3+5+7 = 4 square平方
'''

from itertools import accumulate
from operator import mul
def sqrt_num(x):
    num = range(1,2*x,2)
    return x*x == list(accumulate(num))[-1],list(accumulate(num))
print(sqrt_num(10))

# 立方数和奇数和
def pow3_odd(x):
    lenth = sum([i for i in range(1,x+1)])
    seq = [1 + 2*i for i in range(lenth)]
    st = sum(seq[-x:])
    return seq[-x:],st,pow(st,1/3)

def pow_odd(N):  #N是金字塔第N层
    num = range(N, N*(N+1)//2, 2)
    left = N*N*N
    #图示金字塔第N层就有N个奇数，
    #从顶层数共有N*(N+1)/2个奇数
    #第N层的initial= N*(N+1)//2 - N
    right = list(accumulate(num))
    return left == right[-(N*(N+1)//2 - N)],right,left
N = 10
print(pow_odd(N))