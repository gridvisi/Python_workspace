
s = "slicing is easy"
#print(s[0],s[-1],s[::-1])

# 1到100之间的所有整除3的数列出来

n = 100
#1st for loop solution
def for_loop(n):
    ans = []
    for i in range(n+1): # why n+1?
        if not i%3:
            ans.append(i)
    return ans

#2nd 列表推导式
res = [i for i in range(n+1) if not i%3]

#3rd 切片
result = list(range(n+1))[::3]

print(for_loop(n))
print(res)
print(result)

import time
n = 10000000 # 一千万以内的3整数倍
start = time.time()
for_loop(n)
end = time.time()
print('for_loop time:',end - start)
#for_loop time: 1.2099478244781494

start = time.time()
res = [i for i in range(n+1) if not i%3]
end = time.time()
print('列表推导式 time:',end - start)
#for_loop time: 0.7299973964691162

#3rd 切片
start = time.time()
result = list(range(n+1))[::7]
#print(result)
end = time.time()
print('slice time:',end - start)
#for_loop time: 0.0


# 10000以内非质数
import time
def notPrime(x):
    if x==1 or x==0:return True
    return any([not x%i for i in range(2,int(x**0.5)+1)])

def notPrime(x):
    if x==1 or x==0:return True
    for i in range(2,int(x**0.5)+1):
        if x%i == 0:
            return True

#print('notPrime:',[i for i in range(100) if notPrime(i)])

def isPrime(x):
    if x==1 or x==0:return False
    return all([x%i for i in range(2,int(x**0.5)+1)])
#print('notPrime:',[i for i in range(100) if not isPrime(i)])
#time


def compare(n):
    start1 = time.time()
    res1 = [i for i in range(n) if notPrime(i)]
    end1 = time.time()
    t1 = end1-start1

    start2 = time.time()
    res2 = [i for i in range(n) if not isPrime(i)]
    end2 = time.time()
    t2 = end2-start2
    return 'notPrime',t1,'isPrime:',t2
n = 10000
func1,func2 = notPrime(n),isPrime(n)
print(compare(n))


def factor(n):
    nls,ans = [0]*(n+1),1
    res = [0,1]
    if n == 1 or n == 0: return True
    #prim = ['2','3','5','7']
    for i in range(2,n+1):
        if nls[i]:
            res.append(i)

        else:
            for j in range(i**2,n,i):
                #print(nls)
                nls[j] = 1
    return res
n = 100
print(factor(n))
print([i for i in range(n+1) if notPrime(i)])
#print([i for i in range(1000) if factor(i)])


n = 100000
start1 = time.time()
res1 = [i for i in range(n) if notPrime(i)]
end1 = time.time()
print('notPrime:',end1-start1)


start2 = time.time()
res2 = [i for i in range(n) if not isPrime(i)]
end2 = time.time()
t2 = end2-start2
print('Not isPrime:',end2-start2)

start3 = time.time()
res3 = factor(n)
end3 = time.time()
t3 = end3-start3
print('factor:',end3-start3)