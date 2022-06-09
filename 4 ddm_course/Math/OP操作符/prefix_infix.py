'''

你可能已经知道，有3种运算符的调用符号：前缀（+3
5）、英缀（3 + 5）和后缀（3
5 +）

前缀（以及后缀）运算符在LISP / Scheme等语言中使用，它有一个很好的特性，就是不需要小括号 - -只有一种方法来阅读像3
5 + 2 * 这样的表达式，这与3 + 5 * 2
不同。另一方面，它降低了代码的可读性和运算符及其参数的位置性。这就是为什么我们都喜欢infix运算符。

现在想象一下，我有一个函数，add(x, y)，我有一个类似add(add(add(5, 6), 7), 8)
的表达式......如果我可以在这里使用infix符号，那不是很酷吗？遗憾的是，Python
不允许你定义新的运算符或改变函数获取参数的方式......但这并不意味着我们必须放弃

例如，Haskell
允许你定义自定义运算符并设置它们的优先级，以及将
"正常 "
函数作为
infix
运算符来调用。假设你有一个函数f(x, y) - -你可以像f
5
6
或5
`f`
6
那样调用它（使用反符号）。这样我们就可以把我们之前的表达式，add(add(add(5, 6), 7), 8)，变成5
`add`
6
`add`
7
`add`
8，这样更容易阅读。但是我们怎样才能在Python中做到这一点呢？

好吧，有一个Cookbook，提供了一个非常好的方法来实现Python中的相同功能（由我稍作调整）。
```

'''
from functools import partial


class Infix(object):
    def __init__(self, func):
        self.func = func

    def __or__(self, other):
        return self.func(other)

    def __ror__(self, other):
        return Infix(partial(self.func, other))

    def __call__(self, v1, v2):
        return self.func(v1, v2)



'''

使用这个奇特的类的实例，我们现在可以使用一种新的
"语法 "
来调用函数作为infix运算符。

'''



@Infix
def add(x, y):
    return x + y


print(5 | add | 6)
#11


#用（bitwise ORs）包围装饰的函数，可以使它们以infix方式获取参数。利用这一点，我们可以做各种很酷的事情。

instanceof = Infix(isinstance)
if 5 | instanceof | int:
    print("yes")

#yes

curry = Infix(partial)


def f(x, y, z):
    return x + y + z


print(f | curry | 3)


#functools.partial object at 0xb7733dec >
g = f | curry | 3 | curry | 4 | curry | 5
print(g())
#12


#这不是很酷吗？

