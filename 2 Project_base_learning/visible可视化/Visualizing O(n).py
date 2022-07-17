'''
https://www.geeksforgeeks.org/python-visualizing-on-using-python/?ref=rp

Python | 使用Python实现O(n)的可视化

难度等级：困难

最后更新：2019年9月17日

简介

算法的复杂性可能是一个很难掌握的概念，即使有令人信服的数学论据。本文介绍了一个小小的Python程序，显示了几个典型函数的相对复杂性。它可以很容易地适用于其他函数。

复杂度。为什么它很重要？

计算复杂性是计算机科学中一个古老的主题。它可以被定义为一个算法解决一个问题实例所需的时间和空间的数量。

计算复杂性的基础是数学，但其影响却非常实际。有一些问题是 "难以解决的"。它们不是不可能的（即不可判定的），但对它们没有有效的算法是已知的。也就是说：用现在的技术，甚至用可预见的技术，它们都很难解决。

通常情况下，最坏情况是最好的。

计算复杂性中最流行的分析是最坏情况。尽管它是悲观的，但它是非常合理的：愿意解决的问题的大小随着时间的推移而增加。我们希望处理PB级的数据，而不是兆级的。所以，规模是算法复杂性的一个重要因素。

将输入规模视为自变量，增长率为因变量，并尝试在输入规模增长到无限大时分析其性能。这种分析被称为big-Oh，有许多规则，你可以在任何好的算法教科书中查阅。最重要的一条是，常数不会影响大输入的算法性能。原因还是在于，输入的大小是最重要的因素，而常数并不取决于输入的大小。

比较 Python 中的函数增长

初次接触计算理论的人常常被这样的事实所迷惑：指数函数如e^{n}比多项式函数如n^{100}更差。
这一点从大Oh函数的数学定义中可以看出，但除非我们认为占很大的n，否则不容易看到。

下面的Python代码直观地显示了随着问题实例（N）的增加，几个函数的增长情况：
log n、n、n^{3}、e^{n}。请注意，n^{3}被认为是一个糟糕的性能，因为它需要
10^{9}的操作来处理1000个输入。一般来说，k>=2时，n^{k}被认为是不好的。

这段代码使用了NumPy和MatPlotLib库，并采用了一种叫做currying的函数式编程技术
来计算常数为k的n^{k}，通过修改列表FUNCTIONS来计算其他函数也很容易。

代码: Python代码解释了几个函数的渐近行为。


'''

# Python code that compares the
# asymptotic behaviour of several functions

import numpy as np
import matplotlib.pyplot as plt


# Returns a function that computes x ^ n for a given n
def poly(n):
    def polyXN(x):
        return x ** n

    return polyXN


# Functions to compare and colors to use in the graph
FUNCTIONS = [np.log, poly(1), poly(2), poly(3), np.exp]
COLORS = ['c', 'b', 'm', 'y', 'r']


# Plot the graphs
def compareAsymptotic(n):
    x = np.arange(1, n, 1)
    plt.title('O(n) for n =' + str(n))
    for f, c in zip(FUNCTIONS, COLORS):
        plt.plot(x, f(x), c)
    plt.show()


compareAsymptotic(3)
compareAsymptotic(5)
compareAsymptotic(10)
compareAsymptotic(20)
