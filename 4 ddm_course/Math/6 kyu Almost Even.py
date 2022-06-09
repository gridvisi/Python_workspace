'''
https://www.codewars.com/kata/529e2e1f16cb0fcccb000a6b/train/python
我们需要有能力将一个未知的整数分成给定数量的偶数部分--或者至少是尽可能的偶数部分。
各部分的总和应该是原始值，但每个部分都应该是一个整数，而且它们应该尽可能的接近。

示例代码。
split_integer(20, 6) # 返回 [3, 3, 3, 3, 4, 4] 。
完成函数，使其返回一个代表各部分的整数组。忽略各部分的顺序，你的函数的每个输入只有一个有效的解！
（同时，没有理由测试边缘情况：你的函数的输入对这个卡塔永远有效。

另外，没有理由测试边缘情况：你的函数的输入对这个卡塔总是有效的。

字符串串联法

We need the ability to divide an unknown integer into a given number of even
parts — or at least as even as they can be. The sum of the parts should be the
 original value, but each part should be an integer, and they should be as close
  as possible.

Example code:

split_integer(20, 6)  # returns [3, 3, 3, 3, 4, 4]
Complete the function so that it returns an array of integer representing the parts.
Ignoring the order of the parts, there is only one valid solution for each input to
your function!

(Also, there is no reason to test for edge cases: the input to your function will
always be valid for this kata.)

test.assert_equals(split_integer(10, 1), [10])
test.assert_equals(split_integer(2, 2), [1, 1])
test.assert_equals(split_integer(20, 5), [4, 4, 4, 4, 4])
'''

#18th solution by ericlee
def split_integer(num, parts):
    averg = num//parts
    ans = [averg] * parts
    if num % parts:
        for i in range(1,num % parts+1):
            ans[i] += 1
    return sorted(ans)
num, parts = 20,6
print(split_integer(num, parts))

#1st solution
def splitInteger(n, pp):
    p, bb = divmod(n, pp)
    return (pp - bb) * [p] + bb * [p + 1]

def split_integer(num, parts):
    n = num // parts
    result = [n] * parts
    for i in range(num - sum(result)):
        result[-1 - i] += 1
    return result

def split_integer(num, parts):
    div, mod = divmod(num, parts)
    return [div] * (parts - mod) + [div + 1] * mod

def split_integer(num, parts):
    result = []
    for i in range(parts, 0, -1):
        part = int(num/i)
        result.append(part)
        num -= part
    return result

from heapq import *

def split_integer(num, parts):
    k = [0] * parts
    for i in range(1, num+1):
        heapreplace(k, k[0] + 1)
    return sorted(k)

