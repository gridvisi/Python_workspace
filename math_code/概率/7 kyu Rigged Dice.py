'''
https://www.codewars.com/kata/573acc8cffc3d13f61000533/train/python

创建一个操纵的骰子函数，22%的时间返回数字6，其余时间统一返回整数1，2，3，4，5。其余时间则统一返回整数1,2,3,4,5。
uniformly 均匀 adv ()  一律 ()

只有一个测试用例，调用 throw_rigged 函数 100k 次，并检查在 21700-22300（含）次的范围内返回 6。该测试不会检查1-5
是否被统一或随机返回，但它会检查你的函数是否在1-6（含）范围内返回整数。

这个测试大概有98%的时间有效，所以如果你确信你的解决方案是正确的，你可能需要运行两次。

random.random
random.random()用于生成一个0到1的随机符点数: 0 <= n < 1.0
'''
import random
from fractions import Fraction

def throw_rigged():
    n,m = Fraction(0.22).numerator,Fraction(0.22).denominator
    return random.choice([i for i in range(1,7)]),n,m

test = 22 * [6] + [1,2,3,4,5]*26
print(test)
random.shuffle(test)
print(test)

def throw_rigged():
    test = 22 * [6] + [1, 2, 3, 4, 5] * 26
    random.shuffle(test)
    return random.choice(test)
print(throw_rigged())

#1st solution
import random
def throw_rigged():
    return 6 if random.random() <= .22 else random.randrange(1, 6)