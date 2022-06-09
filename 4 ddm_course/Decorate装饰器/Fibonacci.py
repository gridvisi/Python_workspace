'''
functools.cached_property 缓存属性 (cached_property) 是一个非常常用的功能，很多知名 Python 项目都自己实现过它，现在终于进入版本库了。
具体的可以看我之前写的文章: functools.cached_property(Python 3.8)
functools.lru_cache作为装饰器时可以不加参数,lru_cache装饰器支持max_size和typed2个参数，如果对默认参数不敏感，过去只能这么用(需要空括号):
https://zhuanlan.zhihu.com/p/86670081

https://zhuanlan.zhihu.com/p/76553221
'''

from functools import lru_cache
import time
# 装饰器+递归法 在range为50时 运行速度为:1.4
@lru_cache()
def fib1(n):
    if n == 0 or n == 1:
        return 1
    return fib1(n - 2) + fib1(n - 1)

start = time.perf_counter()
fib1(50)
stop = time.perf_counter()
print(stop - start)

# 递推法 在range为50时 运行速度为:7.0
start = time.perf_counter()
a, b = 0, 1
for _ in range(50):
    a, b = b, a + b
stop = time.perf_counter()
print(stop - start)

#clock
import time
import functools

def clock(func):

    # functools.wraps(func)装饰器的作用是将func函数的相关属性复制到clock中
    # 比如说__name__, __doc__等等
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print('[%0.8fs] %s(%s) -> %r ' % (elapsed, name, arg_str, result))
        return result

#from clockdeco import clock

@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

if __name__=='__main__':
    print(fibonacci(6))

# why ？ https://blog.csdn.net/xff1994/article/details/89182292
class Solution:
    def combinationSum4(self, candidates, target):
        men = [0]*(target+1)
        for i in range(target+1):
            if i in candidates:
                men[i] += 1
            for x in candidates:
                if i - x >= 0:
                    men[i] += men[i-x]
        return men[target]

'''
https://zhuanlan.zhihu.com/p/76553221
'''
import functools
def memoize(fn):
    print('start memoize')
    known = dict()

    @functools.wraps(fn)
    def memoizer(*args):
        if args not in known:
            print('memorize %s' % args)
            # known[args] = fn(*args)
        for k in known.keys():
            print('%s : %s' % (k, known[k]), end=' ')
        print()
        # return known[args]

    return memoizer


@memoize
def nsum(n):
    print('now is %s' % n)
    assert (n >= 0), 'n must be >= 0'
    return 0 if n == 0 else n + nsum(n - 1)


@memoize
def fibonacci(n):
    assert (n >= 0), 'n must be >= 0'
    return n if n in (0, 1) else fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    print(nsum(10))
    print(fibonacci(10))