'''
https://switowski.com/blog/find-item-in-a-list
Find a number
If you want to find the first number that matches some criteria, what do you do? The easiest way is to write a loop that checks numbers one by one and returns when it finds the correct one.
Let’s say we want to get the first number divided by 42 and 43 (that’s 1806). If we don’t have a predefined set of elements (in this case, we want to check all the numbers starting from 1), we might use a “while loop”.
'''

# find_item.py

def while_loop():
    item = 1
    # You don't need to use parentheses, but they improve readability
    while True:
        if (item % 42 == 0) and (item % 43 == 0):
            return item
        item += 1

'''
It’s pretty straightforward:
Start from number 1
Check if that number can be divided by 42 and 43. 
If yes, return it (this stops the loop)
Otherwise, check the next number
Find a number in a list
If we have a list of items that we want to check, we will use a “for loop” instead. 
I know that the number I’m looking for is smaller than 10 000, so let’s use that as 
the upper limit:
'''

# find_item.py

def for_loop():
    for item in range(1, 10000):
        if (item % 42 == 0) and (item % 43 == 0):
            return item

'''
Let’s compare both solutions (benchmarks are done with Python 3.8 - I describe the whole 
setup in the Introduction article):
$ python -m timeit -s "from find_item import while_loop" "while_loop()"
2000 loops, best of 5: 134 usec per loop

$ python -m timeit -s "from find_item import for_loop" "for_loop()"
2000 loops, best of 5: 103 usec per loop
“While loop” is around 30% slower than the “for loop” (134/103≈1.301).
Loops are optimized to iterate over a collection of elements. Trying to manually do 
the iteration (for example, by referencing elements in a list through an index variable) 
will be a slower and often over-engineered solution.

让我们比较一下这两种解决方案 (基准是用Python 3.8完成的 - 我在介绍文章中描述了整个设置)。
$ python -m timeit -s "from find_item import while_loop" "while_loop()"
2000个循环，5个循环中的最佳循环：每个循环134微秒。

$ python -m timeit -s "from find_item import for_loop" "for_loop()"
2000个循环，5个循环中的最佳循环：每循环103微秒。
"While循环 "比 "for循环"（134/103≈1.301）慢30%左右。
循环被优化为在元素集合上迭代。试图手动进行迭代(例如，通过索引变量引用列表中的元素)将是一个较慢且经常被过度设计的解决方案。
'''

def while_loop2():
    item = 1
    while True:
        if (item % 98 == 0) and (item % 99 == 0):
            return item
        item += 1

def for_loop2():
    for item in range(1, 10000):
        if (item % 98 == 0) and (item % 99 == 0):
            return item

'''
This time, we are looking for number 9702, which is at the very end of our list. Let’s 
measure the performance:
$ python -m timeit -s "from find_item import while_loop2" "while_loop2()"
500 loops, best of 5: 710 usec per loop

$ python -m timeit -s "from find_item import for_loop2" "for_loop2()"
500 loops, best of 5: 578 usec per loop
There is almost no difference. “While loop” is around 22% slower this time (710/578≈1.223). 
I performed a few more tests (up to a number close to 100 000 000), and the difference was 
always similar (in the range of 20-30% slower).
Find a number in an infinite list
So far, the collection of items we wanted to iterate over was limited to the first 10 000 numbers.
 But what if we don’t know the upper limit? In this case, we can use the count function from the 
 itertools library.
 
这次我们要找的是9702号，它在我们榜单的最后。让我们来测量一下性能。
$ python -m timeit -s "from find_item import while_loop2" "while_loop2()"
500个循环，5个循环中最好的一个：每个循环710微秒。

$ python -m timeit -s "from find_item import for_loop2" "for_loop2()"
500个循环，5个循环中的最佳循环：每个循环578微秒
几乎没有区别。"While循环 "这次大约慢了22%（710/578≈1.223）。我又进行了几次测试(到接近100 000 000的数字)，差别总是相似的(在慢20-30%的范围内)。
在无限列表中找一个数字
到目前为止，我们想要迭代的项目集合仅限于前10000个数字。但如果我们不知道上限怎么办？在这种情况下，我们可以使用itertools库中的count函数。
'''

from itertools import count

def count_numbers():
    for item in count(1):
        if (item % 42 == 0) and (item % 43 == 0):
            return item

'''
count(start=0, step=1) will start counting numbers from the start parameter, adding the step in each iteration. In my case, I need to change the start parameter to 1, so it works the same as the previous examples.
count works almost the same as the “while loop” that we made at the beginning. How about the speed?
$ python -m timeit -s "from find_item import count_numbers" "count_numbers()"
2000 loops, best of 5: 109 usec per loop
It’s almost the same as the “for loop” version. So count is a good replacement if you need an infinite counter.
What about a list comprehension?
A typical solution for iterating over a list of items is to use a list comprehension. But we want to exit the iteration as soon as we find our number, and that’s not easy to do with a list comprehension. It’s a great tool to go over the whole collection, but not in this case.
Let’s see how bad it is:

count(start=0, step=1)将从起始参数开始计数，在每次迭代中增加步数。在我的例子中，我需要将start参数改为1，
所以它的工作原理和前面的例子一样。
count的工作原理和我们一开始做的 "while循环 "几乎一样。那速度呢？
$ python -m timeit -s "from find_item import count_numbers" "count_numbers()"
2000个循环，5个循环中的最佳循环：每循环109微秒。
它和 "for loop "版本几乎一样。所以，如果你需要一个无限的计数器，count是一个很好的替代品。
那列表理解呢？
对一个项目列表进行迭代的典型解决方案是使用列表理解。但是我们希望一找到我们的数字就退出迭代，而用列表
理解法就不容易做到。它是一个很好的工具，可以遍历整个集合，但在这种情况下就不行了。
让我们看看它有多糟糕。
'''

def list_comprehension():
    return [item for item in range(1, 10000) if (item % 42 == 0) and (item % 43 == 0)][0]
'''
$ python -m timeit -s "from find_item import list_comprehension" "list_comprehension()"
500 loops, best of 5: 625 usec per loop
That’s really bad - it’s a few times slower than other solutions! It takes the same amount of time, no matter if we search for the first or last element. And we can’t use count here.
But using a list comprehension points us in the right direction - we need something that returns the first element it finds and then stops iterating. And that thing is a generator! We can use a generator expression to grab the first element matching our criteria.
Find item with a generator expression


$ python -m timeit -s "from find_item import list_comprehension" "list_comprehension()"
500个循环，5个循环中最好的一个：每个循环625usec。
这真的很糟糕--它比其他的解决方案慢了几倍！无论我们搜索第一个或最后一个元素，都需要同样的时间。无论我们搜索第一个元素还是最后一个元素，所花费的时间都是一样的。而且我们在这里不能使用计数。
但是使用list comprehension为我们指明了正确的方向--我们需要一个东西，它能返回找到的第一个元素，然后停止迭代。而这个东西就是一个生成器! 我们可以使用生成器表达式来抓取符合我们标准的第一个元素。
用生成器表达式查找项目
'''

#Find item with a generator expression

def generator(): #110 usec per loop
    return next(item for item in count(1) if (item % 42 == 0) and (item % 43 == 0))
'''
The whole code looks very similar to a list comprehension, but we can actually use count. Generator expression will execute only enough code to return the next element. Each time you call next(), it will resume work in the same place where it stopped the last time, grab the next item, return it, and stop again.
$ python -m timeit -s "from find_item import generator" "generator()"
2000 loops, best of 5: 110 usec per loop
It takes almost the same amount of time as the best solution we have found so far. And I find this syntax much easier to read - as long as we don’t put too many ifs there!
Generators have the additional benefit of being able to “suspend” and “resume” counting. We can call next() multiple times, and each time we get the next element matching our criteria. If we want to get the first three numbers that can be divided by 42 and 43 - here is how easily we can do this with a generator expression:

整个代码看起来和列表理解非常相似，但实际上我们可以使用count。生成器表达式只会执行足够的代码来返回下一个元素。
每次调用next()，它都会在上次停止的地方继续工作，抓取下一个项目，返回，然后再次停止。
$ python -m timeit -s "from find_item import generator" "generator()"
2000个循环，5个循环中的最佳循环：每循环110微秒。
它所花费的时间几乎和我们目前找到的最佳解决方案一样。而且我发现这种语法更容易读懂--只要我们不在那里放太多的if就可以了
生成器还有一个好处，就是可以 "暂停 "和 "恢复 "计数。我们可以多次调用next()，每次都能得到下一个符合我们标准的元素。
如果我们想得到可以被42和43整除的前三个数字--下面是我们如何用生成器表达式轻松地做到这一点。
'''


def generator_3_items(): #342 usec per loop
    gen = (item for item in count(1) if (item % 42 == 0) and (item % 43 == 0))
    return [next(gen), next(gen), next(gen)]

#Compare it with the “for loop” version:
def for_loop_3_items():  #349 usec per loop
    items = []
    for item in count(1):
        if (item % 42 == 0) and (item % 43 == 0):
            items.append(item)
            if len(items) == 3:
                return items
'''
$ python -m timeit -s "from find_item import for_loop_3_items" "for_loop_3_items()"
1000 loops, best of 5: 323 usec per loop

$ python -m timeit -s "from find_item import for_loop_flat" "for_loop_flat()"
500 loops, best of 5: 613 usec per loop
If you forget to nest ifs, your code will be 90% slower (613/323≈1.898). 

Let’s benchmark both versions:
$ python -m timeit -s "from find_item import for_loop_3_items" "for_loop_3_items()"
1000 loops, best of 5: 342 usec per loop

$ python -m timeit -s "from find_item import generator_3_items" "generator_3_items()"
1000 loops, best of 5: 349 usec per loop
Performance-wise, both functions are almost identical. So when would you use one over the other? 
“For loop” lets you write more complex code. You can’t put nested “if” statements or multiline 
code with side effects inside a generator expression. But if you only do simple filtering, 
generators can be much easier to read.
Be careful with nested ifs!
Nesting too many "if" statements makes code difficult to follow and reason about. And it's 
easy to make mistakes.

In the last example, if we don't nest the second if, it will be checked in each iteration. 
But we only need to check it when we modify the items list. It might be tempting to write 
the following code:

1000个循环，5个循环中的最佳循环：每个循环349微秒。
从性能上来说，两个功能几乎是一样的。那么什么时候你会用一个而不是另一个呢？"For循环 "可以让你编写更复杂的代码。
你不能把嵌套的 "if "语句或带有副作用的多行代码放在生成器表达式里面。但如果你只做简单的过滤，生成器可以更容易阅读。
小心嵌套的 "if "语句!
嵌套太多的 "if "语句会使代码难以遵循和推理。而且很容易犯错。

在最后一个例子中，如果我们不嵌套第二个if，它将在每次迭代中被检查。但我们只需要在修改项目列表时检查它。
可能很想写下面的代码。
'''

def generator(): #110 usec per loop
    return next(item for item in count(1) if (item % 42 == 0) and (item % 43 == 0))


def for_loop_flat():
    items = []
    for item in count(1):
        if (item % 42 == 0) and (item % 43 == 0):
            items.append(item)
        if len(items) == 3:
            return items
'''
This version is easier to follow, but it's also much slower!

$ python -m timeit -s "from find_item import for_loop_3_items" "for_loop_3_items()"
1000 loops, best of 5: 323 usec per loop

$ python -m timeit -s "from find_item import for_loop_flat" "for_loop_flat()"
500 loops, best of 5: 613 usec per loop
If you forget to nest ifs, your code will be 90% slower (613/323≈1.898).

Conclusions
Generator expression combined with next() is a great way to grab one or more elements based on specific criteria. It’s memory-efficient, fast, and easy to read - as long as you keep it simple. When the number of “if statements” in the generator expression grows, it becomes much harder to read (and write).
With complex filtering criteria or many ifs, “for loop” is a more suitable choice that doesn’t sacrifice the performance.
Don't miss new articles

总结
生成器表达式与next()相结合是一种基于特定标准抓取一个或多个元素的好方法。它的内存效率高、速度快、易读--只要你保持简单。当生成器表达式中的 "if语句 "数量增加时，它就会变得更难读（和写）。
对于复杂的过滤标准或许多if，"for循环 "是一个更合适的选择，不会牺牲性能。
不要错过新文章
'''