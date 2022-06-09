'''
上一次说到，函数是我们对过程进行抽象的基本单位。当我们debug、测试性能或者增强函数功能——例如增加一些输出——时，
我们往往不希望直接在函数内部修改。这是因为：

内部修改耦合程度太高
原函数的功能是业务功能，而新增加的并非业务功能。出于软件设计正交性的考虑，我们也不该将他们放在一起。
这时候，我们就需要用到装饰器，它能便捷的做到业务分离的效果。不过由于装饰器的本质是高阶函数，所以下面
先从高阶函数开始讨论，一步一步地讲清楚如何使用装饰器。

高阶函数
高阶函数，简单来说就是：以函数作为输入，或以函数作为输出的函数。举例如下：

修饰器写法总结
如果是带参数修饰器，参数放在最外面一层。
最内层是增强层，输入应该是被修饰函数（原函数），这一层的返回值应该是原函数返回值。
最内层用functools.wraps修饰一下，达到返回原函数_name_等的效果。
最外层的返回值应该是我们增强后的函数。
也就是说，我们在wrapper中封装、增强原函数，保留原函数功能；最后把增强了的函数作为最终返回值。
'''

def given_5(fn):
    return fn(5)

def add_num(num):
    def _fn(x):
         return x + num
    return _fn

'''
自然高阶函数也能同时以函数作为输入和输出。更多关于高阶函数的知识，推荐大家看sicp相关章节（在下面贴一个链接
'''


def add(x, y):
    return x + y

# 对于任意的x y
# add(x, y) == add_num(x)(y) 么？

def logger(fn):
    print('before')
    res = fn(10, 1)
    print('after')
    return res

print(logger(add))
# before
# after
# 11


@logger
def add(x, y):
    return x + y

'''
传入参数
上面的logger不是我们想要的，因为明显看出，我们不能随意的给add传参数了。如果仅能通过更改logger来穿参数，
我们得到的新add就没啥意义了。
于是我们使用刚刚提到的柯里化，将原函数和原函数的参数分步传入logger。
'''
def logger(fn):
    def wrapper(*args, **kwargs):
        print('before')
        res = fn(*args, **kwargs)
        print('after')
        return res
    return wrapper

@logger
def add(x, y):
    return x + y

'''
带参装饰器与保留原始信息
从上面代码就能看出，对add施加装饰器以后，我们得到的不再是add，而是wrapper（这是因为add是高阶函数的输入，
wrapper是高阶函数的输出。）

所以我们对wrapper再套一层装饰器，用以保留关键信息。
'''
def wraps(src):
    def _wraps(dst):
        dst.__module__ = src.__module__
        dst.__name__ = src.__name__
        dst.__doc__ = src.__doc__
        dst.__annotations__ = src.__annotations__
    return _wraps


def logger(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print('before')
        res = fn(*args, **kwargs)
        print('after')
        return res
    return wrapper

@logger
def add(x, y):
    return x + y