# https://docs.python.org/2/library/stdtypes.html#float.as_integer_ratio

'''
https://www.codewars.com/kata/589e2af835999cbe2f000229/train/python

你发现一个魔力骰子，它有无限多的面，显示所有的数字1,2,3,4,5,....。通过无限次的掷骰子，你发现得到数字n的概率是1/2^n。

你遇到了你的朋友，他告诉你，他找到了另一个有无限多面的魔力骰子0,1,2,3,4,5 ......但他不知道找到某个数字m的概率。

你的朋友想测试他的新骰子，并建议玩一个简单的游戏。每个人掷三次骰子。每个玩家取其三次结果中的最大值。数值较大的玩家获胜。
你的朋友掷了三次骰子。你很聪明，你知道原则上，你可以计算出赢得游戏的概率。但如何计算呢？

INPUT：一个整数n>=0。

输出：两个整数a和b，写成a/b的概率的分子和分母（取最小可能的b），即你在三次尝试中赢得游戏。

在Python中输出为list。

test.describe("Basic Tests")
test.it("Example from description:")
test.assert_equals(magicdice(1),[7,8],"Input n=1 does not work! See Example in the description")
test.it("A simple one:")
test.assert_equals(magicdice(5),[2977,32768], "Input n=5 does not work! Should be [2977,32768]")
'''
import itertools
a = ['1', '2', '3']
b = 2
print([''.join(x) for x in itertools.product(*[a] * b)])


#1st solution
from fractions import Fraction
print(Fraction(1,2))
def magicdice(n):
    f = 1 - (1 - Fraction(1, 2) ** n) ** 3
    return [f.numerator, f.denominator]

#3rd solution
def magicdice(n):
    return [(2**n)**3-((2**n)-1)**3,(2**n)**3]


def magicdice(n):
  return [3*pow(4,n)-3*pow(2,n)+1,pow(8,n)]


print(float.is_integer(5.0))

from itertools import combinations
from itertools import permutations
import itertools
def magicdice(n):
    if n == 0: return [1, 1]
    draw = (0.5**(n+1))
    lst = [str(i) for i in range(1,n+1)]
    comlst = [x for x in itertools.product(*[lst]*3)]
    #print(comlst)
    win = 1
    total = 0
    for arr in comlst:
        print(arr)
        for i in arr:
            win *= (0.5**int(i))
        total += win
    print(total)
    return [float.as_integer_ratio(1-total),float.as_integer_ratio(1-total)[1]],float.as_integer_ratio(draw)
#float.as_integer_ratio(draw)]
n = 2
print(magicdice(n))



from itertools import product
a = '123'
b = 3
print([''.join(x) for x in product(a, repeat=b)])