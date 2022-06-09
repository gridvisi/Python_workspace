'''
当你把10的连续幂除以13，你得到整数除法的下列余数：
1，10，9，12，3，4。
然后整个模式重复。
因此，下面的方法是：将数字的最右边的数字乘以上面所示序列中最左边的数字，将第二个最右边的数字乘以序列中数字的第二个最左边的数字。
循环继续，你总结所有这些产品。重复这个过程直到和的序列是平稳的。

我认为有趣的是，以最高“聪明”分数标记的解决方案也会得出最高的“最佳实践”分数。在大多数情况下，这些应该是颠倒的。
递归很聪明，但很难推理，而且计算成本更高。它因数学上的纯洁而受人喜爱；它是最聪明的。
迭代既快又容易推理；几乎总是最佳实践。


When you divide the successive powers of 10 by 13 you get the following remainders of the integer divisions:
1, 10, 9, 12, 3, 4.
Example: What is the remainder when 1234567 is divided by 13?

7×1 + 6×10 + 5×9 + 4×12 + 3×3 + 2×4 + 1×1 = 178

We repeat the process with 178:
8x1 + 7x10 + 1x9 = 87
and again with 87:
7x1 + 8x10 = 87

Test.describe("thirt")
Test.it("Basic tests")
Test.assert_equals(thirt(8529), 79)
Test.assert_equals(thirt(85299258), 31)
Test.assert_equals(thirt(5634), 57)
Test.assert_equals(thirt(1111111111), 71)
Test.assert_equals(thirt(987654321), 30)
'''
def thirt(n):
    k,nls,st = [1, 10, 9, 12, 3, 4],list(str(n)),0
    mark,re = [],n

    s = map(lambda x,y:x*y,k,nls)
    return list(s)
n = 987654321
n = 1234567
n = 8529
n = 321
n = 1234567
n = 13
print(f"{n}",thirt(n))



def thirt(n,mark = [0,1]):
    k,s = [1, 10, 9, 12, 3, 4],0
    for i,e in enumerate(str(n)[::-1]):
        s += int(e)*k[i % len(k)]
    mark.append(s)
    n = s
    if mark[-1] == mark[-2]:return mark[-1]
    return thirt(n,mark)

array = [1, 10, 9, 12, 3, 4]

def thirt(n):
    total = sum([int(c) * array[i % 6] for i, c in enumerate(reversed(str(n)))])
    if n == total:
        return total
    return thirt(total)

n = 987654321
#n = 1234567
n = 1111111111
n = 5634
n = 85299258
n = 13
n = 198
print(thirt(n))
print(f"{n}",thirt(n))

import itertools as it
def thirt(n):
    if n < 100: return n
    pattern = it.cycle([1, 10, 9, 12, 3, 4])
    return thirt(sum(d * n for d, n in zip(map(int, str(n)[::-1]), pattern)))

from itertools import cycle

def thirt(n):
    c = cycle([1, 10, 9, 12, 3, 4])
    m = sum(int(l)*next(c) for l in str(n)[::-1] )
    return m if m == n else thirt(m)

#sum([int(i)*k[str(nls)[::-1].index(i)%len(k)] for i in str(nls)[::-1]])

def thirt(n):
    w = [1, 10, 9, 12, 3, 4]
    while True:
        r = n; q = -1; c = 0; j = 0
        while (q != 0):
            q = int(r / 10)
            c += (r % 10) * w[j % 6]
            r = q
            j += 1
        if (c == n): return c
        n = c

        
from itertools import cycle

def thirt(n):
    c = cycle([1, 10, 9, 12, 3, 4])
    m = sum( int(l)*next(c) for l in str(n)[::-1] )
    return m if m == n else thirt(m)
'''
def thirt(n):
    k,s = [1, 10, 9, 12, 3, 4],0
    mark,re,x = [],n,True
    while x == True:
        print('re',re)
        for i,e in enumerate(str(re)[::-1]):
            s += int(e)*k[i % len(k)]
        re = s
        if re not in mark:mark.append(s)
        elif re in mark: x = False
'''