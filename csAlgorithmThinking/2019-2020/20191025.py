import math
def sqrt_odd(x):

       st = sum([2*i+1 for i in range(x)])
       seq = [2*i+1 for i in range(x)]
       return x,seq,st,math.sqrt(st)
x = 2019
print(sqrt_odd(x))

seq = [i for i in range(1,11)]
print(seq)
print(seq[6:-1])
print(seq[6:10])

'''
for i in range(10):
       print (i)
'''
def pow3_odd(x):
    lenth = sum([i for i in range(1,x+1)])
    seq = [1 + 2*i for i in range(lenth)]
    st = sum(seq[-x:])
    return seq[-x:],st,pow(st,1/3)

'''
说明：作业
1-100之间所有的能被3整除的数列出来，并求和
'''