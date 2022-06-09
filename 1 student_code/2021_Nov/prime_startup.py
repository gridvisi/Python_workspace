
'''
There are 10 types of people: those who understand binary and those who don't.

有10种类型的人：理解二进制的人和不理解二进制的人。
'''

print(int(oct(31))) #10

print(bin(2))
# 0b10
# 0x10
print(int(0x10))

#生活遇到的进制：
#1： True or False
#2： 7进制
#3： 12进制
#4： 24进制

#Oct 31 = Dec 25
#十月31日 == 12月25日
# oct

print(oct(8),oct(16),oct(32))
#ouput:
#0o10 0o20 0o40


import math

def isPrime(x):
    if x == 1:return False #不是素数
    elif x == 2:return True #是素数

    for i in range(2,int(math.sqrt(x)+1)):
        if x%i == 0:
            return False
    return True

import math
x = 100

x = 100000000
print('math.sqrt()',x**0.5)
print(int(x**0.5)+1)
print(int(math.sqrt(x))+1)