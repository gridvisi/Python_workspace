__author__ = 'Administrator'
'''
python 数组的del ,remove,pop区别
2017年05月01日 17:51:22 AnneQiQi 阅读数：8823更多
个人分类： Python
以a=[1,2,3] 为例，似乎使用del, remove, pop一个元素2 之后 a都是为 [1,3], 如下：

>>> a=[1,2,3]
>>> a.remove(2)
>>> a
[1, 3]
>>> a=[1,2,3]
>>> del a[1]
>>> a
[1, 3]
>>> a= [1,2,3]
>>> a.pop(1)
2
>>> a
[1, 3]
>>>
那么Python对于列表的del, remove, pop操作，它们之间有何区别呢？

首先，remove 是删除首个符合条件的元素。并不是删除特定的索引。如下例： 本文来自Novell迷网站 http://novell.me

>>> a = [0, 2, 2, 3]
>>> a.remove(2)
>>> a
[0, 2, 3]
而对于 del 来说，它是根据索引（元素所在位置）来删除的，如下例：

>>> a = [3, 2, 2, 1]
>>> del a[1]
[3, 2, 1]
第1个元素为a[0] －－是以0开始计数的。则a[1]是指第2个元素，即里面的值2.

最后我们再看看pop

>>> a = [4, 3, 5]
>>> a.pop(1)
3
>>> a
[4, 5]
pop返回的是你弹出的那个数值。

所以使用时要根据你的具体需求选用合适的方法。 内容来自http://novell.me

另外它们如果出错，出错模式也是不一样的。注意看下面区别：

>>> a = [4, 5, 6]
>>> a.remove(7)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
>>> del a[7]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list assignment index out of range
>>> a.pop(7)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: pop index out of range

除了1和9以外，还有没有其他的完全平方的数字都是奇数的呢？.isdigit()
j = 33313333393
if isoddigit(j) == True:
    print(j)
'''

import math
def isint(x):
    y = math.sqrt(x)
    if y % 1 == 0:
        return True
    else:
        return False
# print(isint(9))

def isoddigit(x):
    str1 = str(x)
    #print(str1)
    distance = len(str1)
    #print(distance )
    perfect = []

    for i in range(distance):
        #print(i)
        perfect.append(str(int(str1[i]) % 2 == 1))
    #print(perfect)
    if perfect.count('False') == 0:
        return True
    return False


print(isoddigit(33313333393))

temp = []
for i in range(1,10000000): #完全平方数生产
    if isint(i) == True:
        temp.append(i)
print(i, temp)
#side = []
side = temp
for j in temp:
    if isoddigit(j) == True:
        print(j)

def Fibonacci(a, b, n):  #fib数列生成
    for i in range(n):
        a, b = b, a + b
        n -= 1
    return b

print('fib:', Fibonacci(1, 1, 10))
fib = []
for i in range(2, 400):
    fib.append(Fibonacci(1, 1, i))
print(fib, Fibonacci(1, 1, 10))

for x in side:  #fib数列中的完全平方数x
    #for y in side:
    if x in fib:
        print('fib数列中的完全平方数x:', x)

for x in side:  #fib数列中的两个完全平方数之和x
    for y in side:
        if math.sqrt(x + y) in fib:
            if y > x:
                print('fib数列中的两个完全平方数x:', int(math.sqrt(x)),int(math.sqrt(y)),int(math.sqrt(x + y)))

import math

side.pop(0)
pace = 0
for j in range(len(side)):
    #k = j + pace
    for k in range(len(side)):
        if side[j] + side[k] in side:
            if 0.5 * math.sqrt(side[j]) * math.sqrt(side[k]) == math.sqrt(side[j]) + math.sqrt(side[k]) + math.sqrt(
                            side[j] + side[k]):
                print(side[j], side[k], side[j] + side[k])

'''
    if pace < len(side):
        if side[j + pace] + side[j] in side:
            print(side[j],side[j + pace],side[j + pace] + side[j])
            pace += 1
for side[j] in side:
            for side[k] in side:
                for side[p] in side:
                    if side[j] + side[k] + side[j] in side[p]:
while True:
    if side[j] in side:
        if side[k] in side:
            if side[j + pace] + side[j] in side:
                print(side[j],side[k],side[j] + side[k])
            k += 1
        j += 1

'''
'''
 if isint(i) == True:
        side.append(i)
         if  +
            print(side[j] + side[k],side[j],side[k])
'''