__author__ = 'Administrator'
import time
import math

def foo(n):
    return str(n)[::-1]  #巧妙地运用切片十进制回文满足

def foo2(s):
    if s == "":
        return s
    else:
        return foo(str(s)[2:])

def short(m):
    return str(m)[2:]

def is_prime_v2(n):
    if n == 0 or n == 1:
        return False

    max_divisor = math.floor(math.sqrt(n))
    for d in range(2,1+max_divisor):
        if n % d == 0:
            return False
    return True
num = 357357573335577735575753575
#n = int(input("输入你要judge the number："))
print ('n is prime:',is_prime_v2(num))
n = 17
if is_prime_v2(n) == False:
     max_divisor = math.floor(math.sqrt(n))
     for d in range(2,1+max_divisor):
        if n % d == 0:
            print('factor is:',d)




i= int(input("输入你要找的素数范围："))
prime=[]
prime_revise=[]
for i in range(i+1):
    if is_prime_v2(i) == True:
        prime.append(i)
    if is_prime_v2(i) == True and is_prime_v2(int(foo(i))) == True:
        prime_revise.append(int((foo(i))))
        '''
        while True:
            i += 1
            if str(i) == foo(i) and short(bin(i)) == foo2(bin(i)) and is_prime_v2(i) == True:
                print("满足十进制和二进制都是回文数:",i)
                #print(foo(i),foo2(i),short(bin(i)))
                break
        '''
print(prime)
print('素数:',prime[-1],'是第',len(prime),'个素数')
print(prime_revise)
print('素数:',prime_revise[-1],'是第',len(prime_revise),'个素数')

for k in prime_revise:
    for j in prime_revise:
        if k + j == 24:
            print(k,j)



'''
#====== time function ======
t0= time.time()
for n in range(1,100000):
    is_prime_v2(n)

t1 = time.time()
print("time required:",t1-t0)

m = int(input("last number:"))
fab=[]
fab.append(1)
fab.append(1)
print (fab[0])
for i in range (2,m+1):
    fab[i]=fab.append(fab[i-2]+fab[i-1])
print (fab)

cishu = int(input(":"))
t0= time.time()
fb = []
num1 = 1
num2 = 1
num3 = 0
fb.append(1)
fb.append(1)
for i in range(0,cishu):
    num3 = num1+num2
    num1 = num2
    num2 = num3
    fb.append(num3)
print(fb)
if fb[-1]>10**8:
    print(fb[-1]/(10**8),"亿")
t1 = time.time()
print("time required:",t1-t0)
'''