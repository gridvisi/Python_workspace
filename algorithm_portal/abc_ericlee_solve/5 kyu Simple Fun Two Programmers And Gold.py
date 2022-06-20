'''
https://www.codewars.com/kata/59549d482a68fe3bc2000146/train/python

分金子的奥秘
在野外，两个程序员A和B同时发现了一些黄金。他们都想得到这些金子，于是他们决定用以下规则来分配金子。

他们把金子分成n堆，并排在一起。每堆的数量和堆的顺序都是随机的。

他们轮流从最左边或最右边取走一堆黄金。

在每一轮中，程序员将用他的智慧来选择对他最有利的黄金。

输入
一个代表黄金的整数的列表*。

输出
计算出的A和B最终获得的黄金数量，以一个元组*（A的数量，B的数量）。

*列表/元组的表示方法因语言而异--见实例测试

注意，我们可以假设A总是先拿，而且每次都使用最佳策略。

例子
对于黄金=[10,1000,2,1]，输出应该是[1001,12]。

在第一轮，A可以拿10或1，10比1大。
我们应该选择10吗？不，聪明的程序员不这么认为;-)
因为如果A选择10，下一回合B可以选择1000。
所以，A选择1是最好的选择。

在第二轮，无论B选择10还是2，在第三轮，A总是可以选择1000。
所以，B选择10是最好的选择。

最终结果。
A: 1 + 1000 = 1001
B: 10 + 2 = 12
对于金币=[10,1000,2]，输出应该是[12,1000]。

在这个例子中，A面临的选择与前一个例子中的第2个回合相同。

test.assert_equals(distribution_of([4, 7, 2, 9, 5, 2]), (18, 11))
    test.assert_equals(distribution_of([10, 1000, 2, 1]),(1001, 12))
    test.assert_equals(distribution_of([10, 1000, 2]),(12, 1000))
    test.assert_equals(distribution_of([140, 649, 340, 982, 105, 86, 56, 610, 340, 879]),(3206, 981))

'''

def distribution_of(gold):
    pass


gold = [4, 7, 2, 9, 5, 2]

#top 1st
from functools import lru_cache

def distribution_of(gold):
    mini = lru_cache(maxsize=None)(lambda i,j: j-i and min(maxi(i+1, j), maxi(i, j-1)))
    maxi = lru_cache(maxsize=None)(lambda i,j: j-i and max(gold[i]+mini(i+1, j), gold[j-1]+mini(i, j-1)))
    return (res := maxi(0, len(gold))), sum(gold)-res


#2nd solution
def distribution_of(gold):
    n = [*gold]
    for s in range(2, len(gold) + 1):
        m = [min(n[i:i + 2]) for i in range(len(n) - 1)]
        n = [sum(gold[i:i + s]) - v for i, v in enumerate(m)]
    return (*n, *m)

from functools import*

@lru_cache
def dist(gold):
    if len(gold)==1:
        return gold[0],0
    if len(gold)==2:
        return max(gold),min(gold)
    a1,b1=dist(gold[1:])[::-1]
    a2,b2=dist(gold[:-1])[::-1]
    a1+=gold[0]
    a2+=gold[-1]
    if a1>a2:
        return a1,b1
    return a2,b2

def distribution_of(gold):
    return dist(tuple(gold))


from functools import cache


def distribution_of(gold):
    return _distribution_of(tuple(gold))


@cache
def _distribution_of(gold):
    if not gold:
        return (0, 0)

    a, *xa = gold
    *xb, b = gold
    p2a, p1a = _distribution_of(tuple(xa))
    p2b, p1b = _distribution_of(tuple(xb))
    return max((p1a + a, p2a), (p1b + b, p2b))


def distribution_of(gold):
    n = len(gold)
    dp = [[(0,0) for _ in range(n)] for _ in range(n)]
    # init
    for i in range(n):
        dp[i][i] = (gold[i], 0)
    for l in range(1, n):
        for i in range(0, n - l):
            (b1, a1) = dp[i+1][i+l]
            (b2, a2) = dp[i][i+l-1]
            if gold[i] + a1 >= gold[i+l] + a2:
                dp[i][i+l] = (gold[i] + a1, b1)
            else:
                dp[i][i+l] = (gold[i+l] + a2, b2)
            # print(i, i+l, dp[i][i+l])
    return dp[0][n-1]