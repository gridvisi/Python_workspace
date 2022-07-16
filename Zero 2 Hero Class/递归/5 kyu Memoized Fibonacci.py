'''
https://www.codewars.com/kata/529adbf7533b761c560004e5/train/python

问题背景

传统上，斐波那契数列被用来解释树状递归。



def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
这个算法达到了很好的学习目的，但是它的效率非常低，不仅是因为递归，还因为我们调用了两次fibonacci函数，

递归的右边分支（即fibonacci(n-2)）重新计算了左边分支（即fibonacci(n-1)）已经计算的所有斐波纳契数。

这种算法的效率很低，计算任何超过50的斐波那契数字的时间都太长了。在等待答案的时候，你可以去喝杯咖啡或者去打个盹。但如果你在《代码大战》这里尝试，你很可能在任何答案之前得到一个代码超时。

对于这个特殊的 "卡塔"，我们想实现记忆化备忘的解决方案。这将是很酷的，因为它将让我们继续使用树状递归算法，同时仍然保持足够的优化，以获得一个非常快速的答案。

记忆化版本的诀窍在于，我们将保留一个缓存数据结构（很可能是一个关联数组），当我们计算斐波那契数字时，我们将在其中存储这些数字。当计算一个斐波那契数时，我们首先在缓存中查找它，如果它不在那里，我们就计算它并把它放在缓存中，否则就返回缓存中的数字。

把这个函数重构为一个递归的斐波那契函数，使用备忘的数据结构避免了树状递归的不足之处。你能不能让记忆化缓存对这个函数是私有的？
'''

#https://www.codewars.com/kata/529adbf7533b761c560004e5/solutions#:~:text=from%20functools%20import%20lru_cache%0A%0A%40lru_cache(None)%0Adef%20fibonacci(n)%3A%0A%20%20%20%20if%20n%20in%20%5B0%2C%201%5D%3A%0A%20%20%20%20%20%20%20%20return%20n%0A%20%20%20%20return%20fibonacci(n%20%2D%201)%20%2B%20fibonacci(n%20%2D%202)

from functools import lru_cache

@lru_cache(None)
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

import functools
@functools.lru_cache()
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)



def memoized(f):
    cache = {}
    def wrapped(k):
        v = cache.get(k)
        if v is None:
            v = cache[k] = f(k)
        return v
    return wrapped

@memoized
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)