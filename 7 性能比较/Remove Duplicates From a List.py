#https://stackoverflow.com/questions/480214/how-do-you-remove-duplicates-from-a-list-whilst-preserving-order/39835527#39835527



# duplicates.py

from random import randrange

DUPLICATES = [randrange(100) for _ in range(1_000_000)]

'''
Throwaway variable
If you are wondering what's this _ variable - that's a convention used in Python code 
when you need to declare a variable, but you are not planning to use it (a throwaway variable). 
In the above code, I want to call randrange(100) 1 million times. I can't omit the variable 
and just write randrange(100) for range(1_000_000) - I would get a syntax error. 
Since I need to specify a variable, I name it _ to indicate that I won't use it. 
I could use any other name, but _ is a common convention.

Keep in mind that in a Python REPL, _ actually stores the value of the last executed expression. 
Check out this StackOverflow answer for a more detailed explanation. 

丢弃式变量
如果你想知道这个_变量是什么--这是在Python代码中使用的惯例，当你需要声明一个变量，但你并不打算使用它（一个抛弃式变量）。
在上面的代码中，我想调用randrange(100)100万次。我不能省略这个变量，只写randrange(100) for range(1_000_000) - 
我会得到一个语法错误。因为我需要指定一个变量，所以我把它命名为_来表示我不会使用它。我可以使用任何其它的名字，
但 _ 是一个常见的约定。

请记住，在 Python REPL 中，_ 实际上存储的是最后执行的表达式的值。查看这个 StackOverflow 的答案，可以得到更详细的
解释。

'''
# duplicates.py

def test_for_loop(): # 634 msec per loop
    unique = []
    for element in DUPLICATES:
        if element not in unique:
            unique.append(element)
    return unique

unique = []
print([unique.append(num) for num in DUPLICATES if num not in unique])

'''
In general, this is not a good way to use a list comprehension because we use it only for the side effects. We don’t do anything with the list that we get out of the comprehension. It looks like a nice one-liner (and I might use it in a throwaway code), but:
It hides the intention of the code. List comprehension creates a list. But in our case, we actually hide a “for loop” inside!
It’s wasteful - we create a list (because list comprehension always creates a list) just to discard it immediately.
I try to avoid using list comprehension just for the side effects. “For loop” is much more explicit about the intentions of my code.
Remove duplicates with set()
There is a much simpler way to remove duplicates - by converting our list to a set. Set, by definition, is a “collection of distinct (unique) items.” Converting a list to a set automatically removes duplicates. Then you just need to convert this set back to a list:

一般来说，这不是使用列表理解的好方法，因为我们只用它的副作用。我们不会对从理解中得到的列表做任何事情。它看起来是一个很好的单行道（我可能会在一个甩手掌柜的代码中使用它），但是。
它掩盖了代码的意图。列表理解会创建一个列表。但在我们的例子中，我们实际上隐藏了一个 "for循环 "在里面！这是很浪费的--我们创建了一个列表。
这是一种浪费--我们创建了一个列表（因为list comprehension总是创建一个列表），只是为了立即丢弃它。
我尽量避免使用list comprehension，只是因为副作用。"For循环 "更能明确我代码的意图。
用set()删除重复的内容
有一个更简单的方法来删除重复的项目--将我们的列表转换为一个集合。根据定义，集合是 "不同（唯一）项目的集合"。将一个列表转换为一个集合，会自动删除重复的内容。那么你只需要将这个集合转换回一个列表即可。
'''

# duplicates.py

def test_set():  #11 msec per loop
    return list(set(DUPLICATES))

'''
Which one is faster?
$ python -m timeit -s "from duplicates import test_for_loop" "test_for_loop()"
1 loop, best of 5: 634 msec per loop

$ python -m timeit -s "from duplicates import test_set" "test_set()"
20 loops, best of 5: 11 msec per loop
Converting our list to a set is over 50 times faster (634/11≈57.63) than using a “for loop.” 
And a hundred times cleaner and easier to read 😉.
Unhashable items

This above method of converting a list to a set only works if a list is hashable. So it's 
fine for strings, numbers, tuples, and any immutable objects. But it won't work for unhashable 
elements like lists, sets, or dictionaries. So if you have a list of nested lists, your only 
choice is to use that "bad" for loop. That's why "bad" is in quotes - it's not always bad.
To learn more about the difference between hashable and unhashable objects in Python, 
check out this StackOverflow question: What does "hashable" mean in Python?
'''

'''
Remove duplicates while preserving the insertion order
There is one problem with sets - they are unordered. When you convert a list to a set, 
there is no guarantee that it will keep the insertion order. If you need to preserve the 
original order, you can use this dictionary trick:

在保留插入顺序的同时删除重复的内容
集合有一个问题--它们是无序的。当你把一个列表转换为集合时，不能保证它能保持插入顺序。如果你需要保留原来的顺序，
你可以使用这个字典技巧。
'''

# duplicates.py
def test_dict(): #17.9 msec per loop
    return list(dict.fromkeys(DUPLICATES))
#$ python -m timeit -s "from duplicates import test_dict" "test_dict()"
#20 loops, best of 5: 17.9 msec per loop
'''
It’s 62% slower than using a set (17.9/11≈1.627), but still over 30 times faster than the “for loop” (634/17.3≈35.419).
The above method only works with Python 3.6 and above. If you are using an older version of Python, replace dict with OrderedDict:

Here is what the above code does:
It creates a dictionary using fromkeys() method. Each element from DUPLICATES is a key with a value of None. Dictionaries in Python 3.6 and above are ordered, so the keys are created in the same order as they appeared on the list. Duplicated items from a list are ignored (since dictionaries can’t have duplicated keys).
Then it converts a dictionary to a list - this returns a list of keys. Again, we get those keys in the same order as we inserted into the dictionary in the previous step.
What about the performance?
'''

# duplicates.py
from collections import OrderedDict
def test_ordereddict():
    return list(OrderedDict.fromkeys(DUPLICATES))
#$ python -m timeit -s "from duplicates import test_ordereddict" "test_ordereddict()"
#10 loops, best of 5: 32.8 msec per loop

'''
# duplicates.py
从集合导入OrderedDict

def test_ordereddict().fromkeys(DUPLICATES):
    return list(OrderedDict.fromkeys(DUPLICATES))
$ python -m timeit -s "from duplicates import test_ordereddict" "test_ordereddict()"
10个循环，最好的5个循环：每个循环32.8毫秒。
它的速度大约是 set 的 3 倍 (32.8/11≈2.982)，比 dictionary 慢 83% (32.8/17.9≈1.832)，
但它仍然比 "for 循环" (634/32.8≈19.329) 快得多。
而且OrderedDict可以在Python 2.7和任何Python 3版本中工作。

结论
当你需要从一个项目集合中删除重复的项目时，最好的方法是将该集合转换为一个集合。根据定义，集合包含唯一的项目（除其他功能外，如恒定的成员测试时间）。这将使你的代码更快、更易读。
缺点是什么？集合是无序的，所以如果你需要确保你不会失去插入顺序，你需要使用其他东西。例如--字典!

It’s around 3 times as slow as a set (32.8/11≈2.982) and 83% slower than a dictionary (32.8/17.9≈1.832), but it’s still much faster than a “for loop” (634/32.8≈19.329). And OrderedDict will work with Python 2.7 and any Python 3 version.
Conclusions
When you need to remove duplicates from a collection of items, the best way to do this is to convert that collection to a set. By definition, the set contains unique items (among other features, like the constant membership testing time). This will make your code faster and more readable.
Downsides? Sets are unordered, so if you need to make sure you don’t lose the insertion order, you n
eed to use something else. For example - a dictionary!
'''
