__author__ = 'Administrator'
'''
主程序递归
解两道题：第一是寻找 fjan518(n)=1994 求n？
第二题如下：
If the number is odd, multiply by 3 and add 1.
If the number is even, divide by 2.
The Collatz conjecture suggests that when you keep doing this, you will always reach 1 eventually.
However, 7 is not the only number that requires 16 steps. What is the total number of positive
integers which require exactly 16 steps to reach 1 for the first time?
'''

def odd(n,counter):
    counter = 0
    temp = n
    cache = []
    if n%2 == 1:
        n = n*3 + 1
        counter += 1
        cache.append(n)

    if n%2 == 0:
        n = n/2
        counter += 1
        cache.append(n)

    if n == 1 and counter == 16:
        print(temp)

n = int(input("n:"))
if


'''
while True:
    if n != 1:
        stepsixteen(n)
    print('final:',stepsixteen(n))


x = stepsixteen(n)
if x%2 == 1:
    x = stepsixteen(n)
if x%2 == 0:
    x = stepsixteen(n)
if x == 1:
    x = stepsixteen(n)
print(x,stepsixteen(n))
'''
def fjan518(n):
    if n == 1:
        return 0
    elif n%2 == 0:
        return 2*fjan518(n/2)+1
    elif n%2 == 1:
        return 2*fjan518((n-1)/2)

n = int(input("n:"))
print('f(',n,')=',fjan518(n))

cache = []
for i in range(1,10000):
    cache.append(fjan518(i))

cachelist = list(cache)
print (cachelist)

key = int(input("The number you seek?"))
print('you seek',key,'be located:',cache.index(key))

i = len(cache)-1
while i >= 0:
    if cache[i] == key:
        print ('在cache[%d]的处找到key值' % i)
        break
    i -= 1
else:
    print ('没找到')

# 两分法寻找
'''
def find(li,key):
    if len(li) == 1:
        if li[0] == key:
            return True
        return False
    m = len(li)/2
    if find(li[:m],key) or find(li[m:],key):
        return True
    else:
        return False
print(find(cache,1994))
'''
#print(cache)
