
'''
在这里，你定义了 square_root() ，它需要一个数字列表作为参数。在 square_root() 中，你创建了一个名为 result 的空列表，并开始一个 for 循环，在数字中的项目上进行迭代。在每次迭代中，你使用 math.sqrt() 计算当前数字的平方根，然后使用 .append() 将结果添加到 result 中。一旦循环结束，你就返回结果列表。
注意：在上面的例子中，你使用了 math 的 sqrt() 。Python 的数学模块包含在标准库中，提供与数学有关的功能。如果你想更深入地了解数学，那么请查看 The Python math Module: 你需要知道的一切。
这种填充列表的方式在 Python 中相当常见。然而，该语言提供了一些方便的结构体，可以使这个过程更有效，更有Pythonic特色。这些结构之一是列表理解，在下一节中你将看到它的作用。
使用列表理解
在实践中，当你从头开始创建一个列表并填充它时，你经常用列表理解来代替 .append() 。使用列表理解，你可以像这样重新实现 square_root() 。

square_root()中的列表理解功能为numbers中的每个数字创建了一个包含数字平方根的列表。这读起来几乎和普通英语一样。而且，这个新的实现在处理时间上将比使用 .append() 和 for 循环的实现更有效率。
注意：Python 还提供了其它种类的理解，例如集合理解、字典理解和生成器表达式。
要把 .append() 变成一个列表理解，你只需要把它的参数和循环头 (没有冒号) 放在一对方括号内。
切换回 .append()
尽管在填充列表时，列表理解比 .append() 更具可读性和效率，但在某些情况下， .append() 是一个更好的选择。
假设你需要 square_root() 为你的用户提供关于输入的数字列表的平方根的计算进度的详细信息。为了报告操作进度，你可以使用print()。
'''

mixed = [1, 2]

mixed.append(3)
mixed
#[1, 2, 3]

mixed.append("four")
mixed
#[1, 2, 3, 'four']

mixed.append(5.0)
mixed
#[1, 2, 3, 'four', 5.0]

numbers = [1, 2, 3]

# Equivalent to numbers.append(4)
numbers[len(numbers):] = [4]
numbers
#[1, 2, 3, 4]

numbers = [1, 2, 3]

numbers[len(numbers):] = [4, 5, 6]
numbers
#[1, 2, 3, 4, 5, 6]

x = [1, 2, 3, 4]
y = (5, 6)

x.append(y)
x
#[1, 2, 3, 4, (5, 6)]

x = [1, 2, 3, 4]
y = x.append(5)
y is None
True
x
#[1, 2, 3, 4, 5]

'''
现在想想如何把 square_root() 的主体变成一个列表理解。在列表理解中使用 print() 似乎并不连贯，甚至不可能，除非你把部分代码包在一个辅助函数中。所以，在这个例子中，使用 .append() 是正确的选择。
上述例子背后的寓意是，在某些情况下，你不能用列表理解或任何其它结构来代替 .append() 。
用 Python 的 .append() 创建堆栈和队列
到目前为止，你已经学会了如何使用 .append() 向列表中添加一个单项或从头开始填充列表。现在到了一个不同的、更具体的例子了。在这一节中，你将学习如何使用 Python 列表来创建堆栈和队列数据结构，并使用 .append() 和 .pop() 的最低要求功能。
实现一个堆栈
堆栈是一个数据结构，它将项目存储在彼此的上面。项目以后进先出（LIFO）的方式进入和离开堆栈。通常情况下，堆栈实现了两个主要的操作。
push 将一个项目添加到堆栈的顶部，或末端。
pop 移除并返回堆栈顶部的项目。
在列表中，.append()等同于推送操作，所以你可以用它把项目推到堆栈中。列表还提供了 .pop()，它可以选择接受一个整数的索引作为参数。它返回底层列表中该索引的项目，同时也删除该项目。

'''
import math

def square_root(numbers):
    result = []
    for number in numbers:
        result.append(math.sqrt(number))
    return result

numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81]
square_root(numbers)
[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]


import math

def square_root(numbers):
    result = []
    n = len(numbers)
    for i, number in enumerate(numbers):
        print(f"Processing number: {number}")
        result.append(math.sqrt(number))
        print(f"Completed: {int((i + 1) / n * 100)}%")
    return result


numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81]
square_root(numbers)

numbers = [1, 2, 3]
numbers.pop(1)
2
numbers
[1, 3]

numbers.pop()
3
numbers
[1]

numbers.pop()
1
numbers
[]
'''
numbers.pop()
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    numbers.pop()
IndexError: pop from empty list
'''

'''
在Stack中，你首先初始化实例属性._items。这个属性持有一个空列表，你将用它来存储栈中的项目。然后你编码.push()，它使用._items上的.append()来实现推送操作。
你也可以通过调用底层列表._items上的.pop()来实现pop操作。在这种情况下，你使用 try 和 except 块来处理当你在一个空列表上调用 .pop() 时发生的 IndexError。
注意：在 Python 中，使用异常来控制程序的流程是一种常见的模式。Python 开发者喜欢这种编码风格，称为 EAFP (Easier to Ask for Forgiveness than Permission)，而不是称为 LBYL (Look Before You Leap) 的编码风格。
EAFP可以帮助你防止竞赛条件，提高程序或代码片段的总体性能，并防止错误无声地通过。
特殊方法 .__len__() 提供了检索内部列表 ._items 的长度所需的功能。特殊方法 .__repr__() 允许你在向屏幕打印数据结构时提供一个用户友好的堆栈字符串表示。
下面是一些关于你如何在实践中使用Stack的例子。
'''

class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        try:
            return self._items.pop()
        except IndexError:
            print("Empty stack")

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return f"Stack({self._items})"


stack = Stack()

# Push items onto the top of the stack
stack.push(1)
stack.push(2)

# User-friendly printing format
stack
Stack([1, 2])
print(stack)
Stack([1, 2])

# Retrieve the length of the stack
len(stack)
2

# Pop items from the top of the stack
stack.pop()
2
stack.pop()
1
stack.pop()
#Empty stack
stack
Stack([])

'''
这就是了! 你已经编码了一个堆栈数据结构，实现了推送和弹出操作。
它还提供了获得底层列表的长度的功能，并以用户友好的方式打印整个堆栈。

实现一个队列
队列是数据结构，通常以先进先出（FIFO）的方式管理其项目。队列的工作方式就像一个管道，你在一端推入新项目，而旧项目从另一端弹出。
在队列的末端添加一个项目被称为enqueue操作，而从队列的前端或开始删除一个项目被称为dequeue操作。
你可以用.append()对项目进行排队，用.pop()对项目进行脱队。这一次，你需要提供0作为参数给.pop()，只是为了让它检索到列表中的第一个项目而不是最后一个项目。下面是一个实现队列数据结构的类，它使用一个列表来存储其项目。

这个类与你的Stack很相似。主要的区别是 .pop() 将 0 作为参数返回，并删除底层列表 ._items 中的第一个项目，而不是最后一个。
注意：在 Python 列表上使用 .pop(0) 并不是消耗列表项的最有效方法。幸运的是，Python 的集合模块提供了一个叫做 deque() 的数据结构，它实现了 .popleft() ，是一种从 deque() 开始消耗项目的有效方式。
在本教程的稍后部分，你会学到更多关于使用 deque 的知识。
其余的实现几乎是相同的，但使用了适当的名称，如.enqueue()用于添加项目，.dequeue()用于删除它们。你可以像在上一节中使用Stack一样使用Queue：只要调用.enqueue()来添加项目，调用.dequeue()来检索和删除项目。
在其它数据结构中使用 .append()
其他 Python 数据结构也实现了 .append() 。其操作原理与列表中传统的 .append() 相同。该方法在底层数据结构的末端添加一个单项。然而，有一些微妙的区别。
在接下来的两节中，你将学习.append()如何在其他数据结构中工作，如array.array()和collections.deque()。
array.append()
Python 的 array.array() 提供了一个类似序列的数据结构，可以紧凑地表示一个数组的值。这些值必须具有相同的数据类型，这仅限于 C-风格的数据类型，如字符、整数和浮点数。
array.array()需要以下两个参数。
'''

class Queue:
    def __init__(self):
        self._items = []

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        try:
            return self._items.pop(0)
        except IndexError:
            print("Empty queue")

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return f"Queue({self._items})"

#array
'''
要创建一个数组，你需要提供一个单字符代码来定义数组中数值的数据类型。你也可以提供一个可选的具有适当类型的值的列表来初始化数组。
数组支持大多数列表操作，比如切片和索引。像列表一样，array.array()也提供了一个叫做.append()的方法。这个方法的工作原理与列表类似，在底层数组的末端添加一个单一的值。然而，这个值的数据类型必须与数组中的现有值兼容。否则，你会得到一个TypeError。
例如，如果你有一个包含整数的数组，那么你就不能使用.append()向该数组添加一个浮点数字。
'''
from array import array

# Array of integer numbers
int_array = array("i", [1, 2, 3])
int_array
array('i', [1, 2, 3])
int_array[0]
1
int_array[:2]
array('i', [1, 2])
int_array[2] = 4
int_array
array('i', [1, 2, 4])



from array import array

a = array("i", [1, 2, 3])
a
array('i', [1, 2, 3])

# Add a floating-point number
a.append(1.5)
'''
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    a.append(1.5)
TypeError: integer argument expected, got float
'''


from array import array

float_array = array("f", [1.0, 2.0, 3.0])
float_array
array('f', [1.0, 2.0, 3.0])

# Add and integer number
float_array.append(4)
float_array
array('f', [1.0, 2.0, 3.0, 4.0])
'''
deque.append() 和 deque.appendleft()
collections.deque()是另一种数据结构，它实现了.append()的变化。deque是对堆栈和队列的一种概括，它被特别设计用来支持在其两边进行快速和节省内存的append和pop操作。所以如果你需要创建一个具有这些特性的数据结构，那么可以考虑使用deque而不是list。
注意：deque这个名字的发音是 "deck"，代表着双头队列。
collections.deque() 接受以下两个可选参数。
参数内容
iterable 一个作为初始化器的迭代器
maxlen 一个整数，用于指定 deque 的最大长度。
如果你为maxlen提供了一个值，那么你的deque将只存储到maxlen的项目。一旦deque满了，添加一个新的项目将自动导致deque另一端的项目被丢弃。另一方面，如果你没有为maxlen提供一个值，那么deque可以增长到任意数量的项目。
在deque中，.append()也会在底层数据结构的末端或右侧添加一个项目。
'''

from collections import deque

d = deque([1, "a", 3.0])
d
deque([1, 'a', 3.0])

d.append("b")
d
deque([1, 'a', 3.0, 'b'])

'''
像列表一样，deque可以容纳不同类型的项目，所以.append()将任意的项目
添加到deque的结尾。换句话说，通过 .append()，你可以向 deque 中添
加任何对象。
除了.append()，deques还提供了.appendleft()，它可以在deque的开
头或左侧添加一个单项。同样地，deques还提供了.pop()和.popleft()，
分别从deque的右边和左边移除项目。
'''

from collections import deque

d = deque([1, "a", 3.0])
d.appendleft(-1.0)
d
deque([-1.0, 1, 'a', 3.0])

d.pop()
3.0

d.popleft()
-1.0

d
deque([1, 'a'])

'''
对 .appendleft() 的调用在 d 的左边添加了 -1.0。另一方面，
.pop() 返回并删除 d 中的最后一个项目，而 .popleft() 返回并删除
第一个项目。作为一个练习，你可以尝试用 deque 而不是 list 来实现你自己的栈或队列。要做到这一点，你可以利用你在《用 Python 的 .append() 创建堆栈和队列》一节中看到的例子。
总结
Python 提供了一个叫做 .append() 的方法，你可以用它来将项目添加
到给定列表的末尾。这个方法被广泛用于向一个列表的末尾添加一个单项，
或者使用 for 循环来填充一个列表。学习如何使用 .append() 将有助
于你在程序中处理列表。
在本教程中，你学到了。
.append()如何工作
如何使用.append()和for循环来填充列表
什么时候用列表理解法取代.append()？
.append()如何在array.array()和collection.deque()中工作
此外，你还编码了一些关于如何使用.append()来创建数据结构的例子，
如堆栈和队列。这些知识将使你能够使用.append()来高效地增长你的列表。

'''