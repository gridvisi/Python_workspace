# https://switowski.com/blog/ordered-dictionaries

from collections import OrderedDict
d1 = {'a':1, 'b':2}
d2 = {'b':2, 'a':1}
print(d1 == d2)
#True

ord_d1 = OrderedDict(a=1, b=2)
ord_d2 = OrderedDict(b=2, a=1)
ord_d1 == ord_d2
#False
'''
如果你使用 Python 2 或 Python 3 的早期版本，你可能还记得，在过去，字典是没有顺序的。如果你想拥有一个保留插入顺序的字典，常用的解决方案是使用集合模块的 OrderedDict。
在 Python 3.6 中，字典被重新设计以提高其性能 (其内存使用量减少了大约 20-25%)。这个变化有一个有趣的副作用--字典变得有序了(尽管这个顺序并没有得到官方的保证)。"不是官方保证 "意味着这只是一个实现细节，可以在未来的Python版本中删除。
但从Python 3.7开始，插入顺序的保存已经在语言规范中得到了保证。如果你是从Python 3.7或更新的版本开始的，你可能不知道这个世界上需要一个单独的数据结构来保存字典中的插入顺序。
那么，如果不需要使用OrderedDict，为什么它还包含在集合模块中呢？也许这样做更有效率? 让我们一探究竟吧!
OrderedDict vs dict
对于我的基准，我将执行一些典型的字典操作。
创建一个100个元素的字典
添加一个新项目
检查一个项目是否存在于字典中
用get方法抓取一个现有的和不存在的项目。
为了简化代码，我将步骤2-4封装在一个接受字典（或OrderedDictionary）作为参数的函数中。

If you worked with Python 2 or an early version of Python 3, you probably remember that, in the past, dictionaries were not ordered. If you wanted to have a dictionary that preserved the insertion order, the go-to solution was to use OrderedDict from the collections module.
In Python 3.6, dictionaries were redesigned to improve their performance (their memory usage was decreased by around 20-25%). This change had an interesting side-effect - dictionaries became ordered (although this order was not officially guaranteed). “Not officially guaranteed” means that it was just an implementation detail that could be removed in the future Python releases.
But starting from Python 3.7, the insertion-order preservation has been guaranteed in the language specification. If you started your journey with Python 3.7 or a newer version, you probably don’t know the world where you need a separate data structure to preserve the insertion order in a dictionary.
So if there is no need to use the OrderedDict, why is it still included in the collections module? Maybe it’s more efficient? Let’s find out!
OrderedDict vs dict
For my benchmarks, I will perform some typical dictionary operations:
Create a dictionary of 100 elements
Add a new item
Check if an item exists in a dictionary
Grab an existing and nonexistent item with the get method
To simplify the code, I wrap steps 2-4 in a function that accepts a dictionary (or OrderedDictionary) as an argument.
'''

# dictionaries.py

def perform_operations(dictionary):
    dictionary[200] = 'goodbye'
    is_50_included = 50 in dictionary
    item_20 = dictionary.get(20)
    nonexistent_item = dictionary.get('a')

def ordereddict():
    dictionary = OrderedDict.fromkeys(range(100), 'hello world')
    perform_operations(dictionary)

def standard_dict():
    dictionary = dict.fromkeys(range(100), 'hello world')
    perform_operations(dictionary)

'''
$ python -m timeit -s "from dictionaries import ordereddict" "ordereddict()"
50000 loops, best of 5: 8.6 usec per loop

$ python -m timeit -s "from dictionaries import standard_dict" "standard_dict()"
50000 loops, best of 5: 4.7 usec per loop
OrderedDict is over 80% slower than the standard Python dictionary (8.6/4.7≈1.83).
What happens if the dictionary size grows to 10 000 elements?
'''

# dictionaries2.py

from collections import OrderedDict

def perform_operations(dictionary):
    dictionary[20000] = 'goodbye'
    is_5000_included = 5000 in dictionary
    item_2000 = dictionary.get(2000)
    nonexistent_item = dictionary.get('a')

def ordereddict():
    dictionary = OrderedDict.fromkeys(range(10000), 'hello world')
    perform_operations(dictionary)

def standard_dict():
    dictionary = dict.fromkeys(range(10000), 'hello world')
    perform_operations(dictionary)

'''
$ python -m timeit -s "from dictionaries import ordereddict" "ordereddict()"
200个循环，5个循环中的最佳循环：每循环1.07毫秒。

$ python -m timeit -s "from dictionary import standard_dict" "standard_dict()"
500个循环，5个循环中最好的一个：每循环547usec
在将字典大小增加 100 倍后，两个函数之间的差异保持不变。OrderedDict执行同样的操作所需的时间仍然是标准Python字典的近两倍。
测试再大的字典也没有意义。如果你需要一个真正的大字典，你应该使用 Numpy 或 Pandas 库中更高效的数据结构。
什么时候使用OrderedDict？
如果OrderedDict比较慢，你为什么要使用它？我可以想到至少有两个原因。
你还在使用一个不能保证字典中的顺序的 Python 版本 (3.6 之前)。在这种情况下，你别无选择。
你想使用OrderedDict提供的额外功能。例如，它可以被逆转。如果你试图在标准字典上运行reversed()函数，你会得到一个错误，但OrderedDict会很好地返回一个反转的版本。
在比较字典时，你实际上关心的是排序。正如 Ned Batchelder 在他的 "Ordered dict surprises "一文中指出的那样，当你比较两个具有相同项目但顺序不同的字典时，Python 将它们报告为相等。但如果你比较两个具有相同项的OrderedDict对象的顺序不同，它们就不相等。请看这个例子。
$ python -m timeit -s "from dictionaries import ordereddict" "ordereddict()"
200 loops, best of 5: 1.07 msec per loop

$ python -m timeit -s "from dictionaries import standard_dict" "standard_dict()"
500 loops, best of 5: 547 usec per loop
After increasing the dictionary size by 100x times, the difference between both functions stays the same. OrderedDict still takes almost twice as long to perform the same operations as a standard Python dictionary.
There is no point in testing even bigger dictionaries. If you need a really big dictionary, you should use more efficient data structures from the Numpy or Pandas libraries.
When to use OrderedDict?
If the OrderedDict is slower, why would you want to use it? I can think of at least two reasons:
You are still using a Python version that doesn’t guarantee the order in dictionaries (pre 3.6). In this case, you don’t have a choice.
You want to use additional features that OrderedDict offers. For example, it can be reversed. If you try to run reversed() function on a standard dictionary, you will get an error, but OrderedDict will nicely return a reversed version of itself.
You actually care about the ordering when comparing dictionaries. As pointed out by Ned Batchelder in his “Ordered dict surprises” article, when you compare two dictionaries with the same items, but in a different order, Python reports them as equal. But if you compare two OrderedDict objects with the same items in a different order, they are not equal. See this example:
'''

