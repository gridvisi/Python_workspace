# https://www.python.org/dev/peps/pep-0008/#programming-recommendations


a = True
b = True
print(a is b) #True
# Variables that are identical are always also equal!
print(a == b) #True

# But
a = [1,2,3]
b = [1,2,3]
print(a is b) #False  # Those lists are two different objects
print(a == b)
#True  # Both lists are equal (contain the same elements)

a = 1
# This will print 'yes'
if a is 1:
    print('yes')

b = 1000
# This won't!
if b is 1000:
    print('yes')

'''
How do you check if something is True in Python? There are three ways:
One “bad” way: if variable == True:
Another “bad” way: if variable is True:
And the good way, recommended even in the Programming Recommendations of PEP8: if variable:
The “bad” ways are not only frowned upon but also slower. Let’s use a simple test:
$ python -m timeit -s "variable=False" "if variable == True: pass"
10000000 loops, best of 5: 24.9 nsec per loop

$ python -m timeit -s "variable=False" "if variable is True: pass"
10000000 loops, best of 5: 17.4 nsec per loop

$ python -m timeit -s "variable=False" "if variable: pass"
20000000 loops, best of 5: 10.9 nsec per loop
Using is is around 60% slower than if variable (17.4/10.9≈1.596), but using == is 120% slower (24.9/10.9≈2.284)! It doesn’t matter if the variable is actually True or False - the differences in performance are similar (if the variable is True, all three scenarios will be slightly slower).
Similarly, we can check if a variable is not True using one of the following methods:
if variable != True: (“bad”)
if variable is not True: (“bad”)
if not variable: (good)

如何在Python中检查某事是否为True？有三种方法。
一种 "坏 "方法：如果变量==True。
另一个 "坏 "方法：if变量为真。
而好的方法，甚至在PEP8的编程建议中都有推荐：if变量。
这些 "坏 "的方式不仅不受欢迎，而且速度也比较慢。我们用一个简单的测试。
$ python -m timeit -s "variable=False" "if variable == True: pass"
10000000次循环，5次中的最好一次：每次循环24.9纳秒。

$ python -m timeit -s "variable=False" "if variable is True: pass."
10000000个循环，5个循环中的最佳循环：每个循环17.4纳秒。

$ python -m timeit -s "variable=False" "if变量：pass"
20000000个循环，5个循环中的最佳循环：每个循环10.9纳秒。
使用is比if变量慢60%左右(17.4/10.9≈1.596)，但使用==则慢120%(24.9/10.9≈2.284)! 变量实际上是True还是False并不重要--性能上的差异是相似的（如果变量是True，三种情况都会稍慢）。
同样，我们可以使用以下方法之一检查一个变量是否为非True。
如果变量 != True: ("坏")
如果变量不是True：("坏")
如果不变量。(好)

通过www.DeepL.com/Translator（免费版）翻译

$ python -m timeit -s "variable=False" "if variable != True: pass"
10000000 loops, best of 5: 26 nsec per loop

$ python -m timeit -s "variable=False" "if variable is not True: pass"
10000000 loops, best of 5: 18.8 nsec per loop

$ python -m timeit -s "variable=False" "if not variable: pass"
20000000 loops, best of 5: 12.4 nsec per loop

'''


'''

if not variable wins. is not is 50% slower (18.8/12.4≈1.516) and != takes twice as long (26/12.4≈2.016).
The if variable and if not variable versions are faster to execute and faster to read. They are common idioms that you will often see in Python (or other programming languages).
About the "Writing Faster Python" series

"Writing Faster Python" is a series of short articles discussing how to solve some common problems with different code structures. I run some benchmarks, discuss the difference between each code snippet, and finish with some personal recommendations.
Are those recommendations going to make your code much faster? Not really.
Is knowing those small differences going to make a slightly better Python programmer? Hopefully!
You can read more about some assumptions I made, the benchmarking setup, and answers to some common questions in the Introduction article.

“truthy” and “falsy”
Why do I keep putting “bad” in quotes? That’s because the “bad” way is not always bad (it’s only wrong when you want to compare boolean values, as pointed in PEP8). Sometimes, you intentionally have to use one of those other comparisons.
In Python (and many other languages), there is True, and there are truthy values. That is, values interpreted as True if you run bool(variable). Similarly, there is False, and there are falsy values (values that return False from bool(variable)). An empty list ([]), string (""), dictionary ({}), None and 0 are all falsy but they are not strictly False.
Sometimes you need to distinguish between True/False and truthy/falsy values. If your code should behave in one way when you pass an empty list, and in another, when you pass False, you can’t use if not value.
Take a look at the following scenario:
def process_orders(orders=None):
    if not orders:
        # There are no orders, return
        return
    else:
        # Process orders
        ...
We have a function to process some orders. If there are no orders, we want to return without 
doing anything. Otherwise, we want to process existing orders.
We assume that if there are no orders, then orders parameter is set to None. But, if the orders 
is an empty list, we also return without any action! And maybe it’s possible to receive an 
empty list because someone is just updating the billing information of a past order? Or perhaps 
having an empty list means that there is a bug in the system. We should catch that bug before
 we fill up the database with empty orders! No matter what’s the reason for an empty list, 
 the above code will ignore it. We can fix it by investigating the orders parameter more 
 carefully:
def process_orders(orders=None):
    if orders is None:
        # orders is None, return
        return
    elif orders == []:
        # Process empty list of orders
        ...
    elif len(orders) > 0:
        # Process existing orders
        ...
The same applies to truthy values. If your code should work differently for True than for, 
let’s say, value 1, we can’t use if variable. We should use == to compare the number
 (if variable == 1) and is to compare to True (if variable is True). Sounds confusing? 
 Let’s take a look at the difference between is and ==.
is checks the identity, == checks the value
The is operator compares the identity of objects. If two variables are identical, it means 
that they point to the same object (the same place in memory). They both have the same ID 
(that you can check with the id() function).
The == operator compares values. It checks if the value of one variable is equal to the 
value of some other variable.
Some objects in Python are unique, like None, True or False. Each time you assign a 
variable to True, it points to the same True object as other variables assigned to True. 
But each time you create a new list, Python creates a new object:

if not变量胜出。is not慢了50%(18.8/12.4≈1.516)， !=的时间是它的两倍(26/12.4≈2.016)。
if变量和if not变量版本的执行速度更快，读取速度更快。它们是你在Python（或其他编程语言）中经常会看到的常见习语。
关于《写更快的Python》系列文章

"写更快的Python "是一系列短文，讨论如何用不同的代码结构解决一些常见问题。我运行了一些基准，讨论了每个代码片段之间的差异，最后提出了一些个人建议。
这些建议会让你的代码变得更快吗？不一定。
了解这些细小的差异会让一个Python程序员变得稍微好一点吗? 希望如此!
你可以在导言文章中阅读更多关于我所做的一些假设、基准测试的设置以及一些常见问题的答案。

"真 "与 "假"
为什么我一直把 "坏 "加引号？那是因为 "坏 "的方式并不总是坏的（只有当你想比较布尔值时才是错误的，正如PEP8中指出的那样）。有时，你故意要使用那些其他的比较方式之一。
在Python(和许多其他语言)中，有True，也有truthy值。也就是说，如果你运行 bool(variable) ，就会被解释为 True 的值。类似地，有False，也有falsy值（从bool(variable)返回False的值）。空列表([])、字符串("")、字典({})、None和0都是false，但它们不是严格意义上的False。
有时你需要区分真/假和真/假值。如果你的代码在传递空列表时应该以一种方式表现，而在传递False时应该以另一种方式表现，你就不能使用if not值。
请看下面的场景。
def process_orders(orders=None):
    if not orders:
        # 没有订单，返回
        返回
    否则
        # 处理订单
        ...
我们有一个函数来处理一些订单。如果没有订单，我们希望不做任何事情就返回。否则，我们要处理现有的订单。
我们假设如果没有订单，那么订单参数就设置为None，但是，如果订单是一个空列表，我们也不做任何处理就返回。但是，如果订单是一个空的列表，我们也是不做任何操作就返回。而接收到一个空列表，也许是因为有人只是更新了过去订单的账单信息？也可能出现空单意味着系统有bug。我们应该在数据库被空单填满之前，抓住这个bug! 不管是什么原因导致空单，上面的代码都会忽略它。我们可以通过更仔细地调查 orders 参数来解决这个问题。
def process_orders(orders=None):
    if orders is None:
        # orders is None, return
        返回
    elif orders == []:
        # 处理空的订单列表
        ...
    elif len(orders) > 0:
        # 处理现有订单
        ...
这同样适用于Truthhy值。如果你的代码对于True的工作方式应该和对于比如说值1的工作方式不同，我们就不能使用if变量。我们应该用==来比较这个数字（如果变量==1），用is来比较True（如果变量是True）。听起来很混乱？我们来看看is和==的区别。
is检查身份，==检查值。
is运算符比较对象的身份。如果两个变量相同，意味着它们指向同一个对象（内存中的同一个地方）。它们都有相同的ID（你可以用id()函数检查）。
== 操作符比较值。它检查一个变量的值是否等于其它变量的值。
Python 中的一些对象是唯一的，比如 None、True 或 False。每次你把一个变量赋给True时，它都会和其他赋给True的变量一样，指向同一个True对象。但是每次创建新的列表时，Python都会创建一个新的对象。

通过www.DeepL.com/Translator（免费版）翻译

In the above example, the first block of code will print “yes,” but the second won’t. 
That’s because Python performs some tiny optimizations and small integers share the same 
ID (they point to the same object). Each time you assign 1 to a new variable, it points 
to the same 1 object. But when you assign 1000 to a variable, it creates a new object. 
If we use b == 1000, then everything will work as expected.
Conclusions
To sum up:
To check if a variable is equal to True/False (and you don’t have to distinguish between 
True/False and truthy / falsy values), use if variable or if not variable. It’s the simplest 
and fastest way to do this.
If you want to check that a variable is explicitly True or False (and is not truthy/falsy), 
use is (if variable is True).
If you want to check if a variable is equal to 0 or if a list is empty, use if variable == 0 
or if variable == [].

在上面的例子中，第一个代码块会打印 "yes"，但第二个不会。这是因为Python进行了一些微小的优化，小整数共享同一个
ID（它们指向同一个对象）。每次你把 1 分配给一个新的变量时，它都会指向同一个 1 对象。但是当你给一个变量赋值1000时，
它就会创建一个新的对象。如果我们使用b==1000，那么一切都会按照预期的方式工作。
结论
总结一下。
要检查一个变量是否等于True/False(而且你不必区分True/False和truthhy/falsy值)，使用if variable或if not 
variable。这是最简单、最快的方法。
如果你想检查一个变量是否显式为True或False（并且不是Truthhy/Falsy），使用is（如果变量为True）。
如果你想检查一个变量是否等于0或者一个列表是否为空，使用if variable == 0或者if variable == []。
'''

