# https://www.cnblogs.com/panlq/p/9307203.html

# 递归
def Fibonacci_Recursion_tool(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci_Recursion_tool(n - 1) + Fibonacci_Recursion_tool(n - 2)

def Fibonacci_Recursion(n):
    result_list = []
    for i in range(1, n + 1): result_list.append(Fibonacci_Recursion_tool(i))
    return result_list

def Fibonacci_Loop_tool(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1


def Fibonacci_Loop(n):
    result_list = []
    a, b = 0, 1
    while n > 0:
        result_list.append(b)
        a, b = b, a + b
        n -= 1
    return result_list

def Fibonacci_Yield_tool(n):
    a, b = 0, 1
    while n > 0:
        yield b
        a, b = b, a + b
        n -= 1
'''
相比于之前的Fibonacci_Loop,Fibonacci_Yield 明显优雅了很多,yield关键字,
可以在不打断循环的情况下从循环中返回数值,这个特性简直是nice,不过其返回的数据
类型也变得有点特别,变成了generator,那么取值也就比以前不同了一点,这里有两种方
式,第一种是直接转化为list,使用list()即可,这种方式比较快,速度消耗很小.除此之
外还有第二种,return [f for i, f in enumerate(Fibonacci_Yield_tool(n))]
列表解析,这种方式转换速度很慢,在n=1000左右时,在我的电脑上速度接不断接近于1s,但是
让我们只运行Fibonacci_Yield_tool()却会发现,Fibonacci_Yield_tool的运行耗时
只在10的负六次方到五次方之间.而直接转化为list则对计算速度的影响较小,接近于纯粹的计
算耗时本身,几乎不存在影响.在本例子中循环算法与yield关键字(list转换)的速度接近.
'''

class Fibonacci(object):
    """斐波那契数列迭代器"""

    def __init__(self, n):
        """
        :param n:int 指 生成数列的个数
        """
        self.n = n
        # 保存当前生成到的数据列的第几个数据，生成器中性质，记录位置，下一个位置的数据
        self.current = 0
        # 两个初始值
        self.a = 0
        self.b = 1

    def __next__(self):
        """当使用next()函数调用时，就会获取下一个数"""
        if self.current < self.n:
            self.a, self.b = self.b, self.a + self.b
            self.current += 1
            return self.a
        else:
            raise StopIteration

    def __iter__(self):
        """迭代器的__iter__ 返回自身即可"""
        return self


if __name__ == '__main__':
    fib = Fibonacci(15)
    for num in fib:
        print(num)

for x in [1, 2, 3, 4, 5]:
    pass

#相当于：Copy 首先获取可迭代对象
it = iter([1, 2, 3, 4, 5])
while True:
    try:
        next(it)
    except StopIteration:
        # 遇到StopIteration就跳出循环, 且自动频闭StopIteration异常
        break


import numpy as np

### 1
def fib_matrix(n):
    for i in range(n):
        res = pow((np.matrix([[1, 1], [1, 0]], dtype='int64')), i) * np.matrix([[1], [0]])
        print(int(res[0][0]))


# 调用 fib_matrix(50)
### 2
# 使用矩阵计算斐波那契数列
def Fibonacci_Matrix_tool(n):
    Matrix = np.matrix("1 1;1 0", dtype='int64')
    # 返回是matrix类型
    return np.linalg.matrix_power(Matrix, n)

def Fibonacci_Matrix(n):
    result_list = []
    for i in range(0, n):
        result_list.append(np.array(Fibonacci_Matrix_tool(i))[0][0])
    return result_list

# 调用
print(Fibonacci_Matrix(50))
'''
因为幂运算可以使用二分加速，所以矩阵法的时间复杂度为 O(log n)
用科学计算包numpy来实现矩阵法 O(log n)
'''
'''
上下文管理器实现计时器#
装饰器就是 fib(n) = trace(fib)(n), 即将函数当作参数，与此同时，类实现了__call__方法之后也
是一个callable

递归版斐波那契函数要求如下：

1.输出文档说明
2.输出函数每次执行的函数名，所用参数，返回值，执行时间
3.输出总耗时
'''
import time
import functools
def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.clock()
        v = func(*args, **kwargs)
        end = time.clock()
        print('{}, {}, {}, {}, cost: {} seconds'.format(
                func.__name__, args, kwargs , v, (end - start)))
        return v
    return wrapper


class TimeTrace:
    def __init__(self, f):
        self.f = f
        print(f.__doc__)

    def __now(self):
        return time.time()

    def __enter__(self):
        self.start = self.__now()
        return self

    def __exit__(self, exc_type, exc_val, tb):
        self.end = self.__now()
        print('cost {}'.format(self.end - self.start))

    def __call__(self, n):
        start = self.__now()
        val = self.f(n)
        end = self.__now()
        print('{}, {}, {}, cost: {} seconds'.format(self.f.__name__, n, val, (end - start)))
        return val


def fib(n):
    """
    :params n 个数
    :return 当前斐波那契数值
    """
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


with TimeTrace(fib) as fib:
    print(fib(5))