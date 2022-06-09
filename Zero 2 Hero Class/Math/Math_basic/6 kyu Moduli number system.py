'''
https://www.codewars.com/kata/54db15b003e88a6a480000b9/train/python

For example, if we use the system [2, 3, 5] the number n = 11 is represented by
 "-1--2--1-", the number n = 23 by "-1--2--3-".

If we use the system [8, 7, 5, 3] the number n = 187 becomes "-3--5--2--1-".

You will be given a number n (n >= 0) and a system S = [m1,m2, ···,mk] and you
will return a string "-x1--x2-- ...--xk-" representing the number n in the system S.

If the moduli are not pairwise co-prime or if the product m1 * ... * mk is not
greater than n, return "Not applicable".

Examples:
(you can add them in the "Sample tests")

fromNb2Str(11, [2,3,5]) -> "-1--2--1-"
fromNb2Str(6, [2, 3, 4]) -> "Not applicable", since 2 and 4 are not coprime
fromNb2Str(7, [2, 3]) -> "Not applicable" since 2 * 3 < 7

一个有模数的数系由k个模数的向量[m1,m2,--,mk]来定义。

这些模数必须是成对共质的，也就是说，对于任何一对模数，唯一的公因子是1。

在这样的系统中，每一个数字n用一串"-x1--x2--...。--xk-"的残差表示，每个模数一个。乘积
m1*... * mk必须大于要在模数系统中转换的给定数字n。

例如，如果我们使用[2，3，5]系统，数字n=11用"-1--2--1-"表示，数字n=23用"-1--2--3-"表示。

如果我们使用系统[8，7，5，3]，数字n=187就会变成"-3--5--2--1-"。

你将得到一个数字n（n>=0）和一个系统S=[m1,m2,--,mk]，你将返回一个字符串"-x1--x2--...--xk-"代表系统S中的数字n。

如果模数不是成对共质，或者乘积m1*......*mk不大于n。* mk不大于n，则返回 "不适用"。

举例说明。
(你可以在 "样本测试 "中添加它们)

fromNb2Str(11, [2,3,5]) -> "-1--2--1-"
fromNb2Str(6,[2,3,4]) -> "不适用"，因为2和4不是同prime。
fromNb2Str(7, [2, 3]) -> "不适用"，因为2*3<7。

通过www.DeepL.com/Translator（免费版）翻译
'''
print(True + 1)
for i in range(2,3):print('test:',i)
#great common div = GCD

def gcd(input):
    judge = True
    for n in range(2,min(input)+1):
        if ([i % n == 0 for i in input]).count(1) >= 2:
            return not judge
    return judge

input = 3,7,12
input = [13,11,7,5,3,2]
print('gcd:',gcd(input))

def mult(arr):
    ans = 1
    for i in arr:
        ans *= i
    return ans

def fromNb2Str(n, modsys):
    if not gcd(modsys):return "Not applicable"
    elif mult(modsys) < n:return "Not applicable"
    else:
        return '-'+'--'.join([str(n % i) for i in modsys])+'-'

n,modsys = 3450, [13,11,7,5,3,2]
print(fromNb2Str(n, modsys))

#1st
from itertools import combinations
from fractions import gcd
from functools import reduce
def fromNb2Str(n, modsys):
    if any(gcd(x, y) > 1 for x, y in combinations(modsys, 2)) or n > reduce(lambda x, y: x*y, modsys):
        return "Not applicable"
    return "-" + "--".join(str(n % m) for m in modsys) + "-"

#2nd
def fromNb2Str(n, modsys):
    k = [n%x for x in modsys]
    prod = eval('*'.join(str(x) for x in modsys))
    if prod > n and sum(x%2 for x in modsys) == len(k)-1:
        return '-'+'--'.join(str(x) for x in k)+'-'
    return 'Not applicable'

#3rd
from math import gcd
import numpy
def fromNb2Str(n, mod):
    if numpy.prod(mod)<n or gcd(mod[0],mod[1])>1:
        return 'Not applicable'
    return "-"+"--".join(list(map(str,[n%elmod for elmod in mod])))+"-"

from math import gcd
from numpy import prod
def fromNb2Str(n, modsys):
    if not all([gcd(a,b)==1 or a==b for a in modsys for b in modsys]):
        return "Not applicable"
    if prod(modsys)<=n:
        return "Not applicable"
    return "-"+"--".join([str(n%i) for i in modsys])+"-"