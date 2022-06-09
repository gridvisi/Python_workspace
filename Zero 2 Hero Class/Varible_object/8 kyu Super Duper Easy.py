'''
https://www.codewars.com/kata/55a5bfaa756cfede78000026/train/python

Test.assert_equals(problem("hello"), "Error")
Test.assert_equals(problem(1), 56)
#There are more test cases

isinstance() 与 type() 区别：

type() 不会认为子类是一种父类类型，不考虑继承关系。

isinstance() 会认为子类是一种父类类型，考虑继承关系。

如果要判断两个类型是否相同推荐使用 isinstance()。


def isPrime(n):
    return n%2==0 n%i for i in range(int(math.sqrt(n))+1)

'''
import math
print('sqtr:',math.sqrt(1000))

#prime 1,
n = 8
print([i for i in range(n)])

def isPrime(n):
    if n == 0 or n == 1:return False
    if n == 2 or n == 3:return True
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
print('isPrime:',[isPrime(n) for n in range(100)])


# all the even within 0,100
print([i for i in range(100) if i % 2 == 1])

a = 'zzm'
print(isinstance(a,int))
print(isinstance(a,str))  #string

a = ["zzm","ada","alex","eric"]
print(isinstance(a,str))
print(isinstance(a,list))  #列表

age = ['11','10','10','18']

#dictary = dict() 字典  数据结构

print(list(zip(a,age)))
print(dict(zip(a,age)))
print('dict:',isinstance(dict(zip(a,age)),dict))



print(float(math.pi))
print(math.floor(3.6))
print(round(3.6456346,5))

a = 1
def problem(a):
    return a * 50 + 6 if isinstance(a,int) else "Error"  #intege
a = 1
a = "1"
print('problem:',problem(a))

def problem(a):
    return  "Error" if not isinstance(a,str) else a * 50 + 6

#1st
def problem(a):
    try:
        return a * 50 + 6
    except TypeError:
        return "Error"
