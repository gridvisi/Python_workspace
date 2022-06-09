# https://switowski.com/blog/for-loop-vs-list-comprehension

'''
Many simple “for loops” in Python can be replaced with list comprehensions. You can often hear that list comprehension is “more Pythonic” (almost as if there was a scale for comparing how Pythonic something is, compared to something else 😉). In this article, I will compare their performance and discuss when a list comprehension is a good idea, and when it’s not.
Filter a list with a “for loop”
Let’s use a simple scenario for a loop operation - we have a list of numbers, and we want to remove the odd ones. One important thing to keep in mind is that we can’t remove items from a list as we iterate over it. Instead, we have to create a new one containing only the even numbers:
在Python中很多简单的 "for循环 "都可以用列表理解来代替。你经常可以听到列表理解是 "更Pythonic"(几乎就像有一个标尺，用来比较某件事的Pythonic程度，与其他东西相比😉)。在本文中，我将比较它们的性能，并讨论什么时候列表理解是一个好主意，什么时候不是。
用 "for循环 "过滤一个列表
让我们用一个简单的场景来进行循环操作--我们有一个数字列表，我们想删除奇数。需要记住的一件重要事情是，我们不能在迭代列表时从列表中删除项目。相反，我们必须创建一个只包含偶数的新列表。
if not element % 2 is equivalent to if element % 2 == 0, but it’s slightly faster. I will write a separate article about comparing boolean values soon.
Let’s measure the execution time of this function. I’m using Python 3.8 for benchmarks (you can read about the whole setup in the Introduction article):
$ python -m timeit -s "from filter_list import for_loop" "for_loop()"
5 loops, best of 5: 65.4 msec per loop
It takes 65 milliseconds to filter a list of one million elements. How fast will a list comprehension deal with the same task?
'''

# filter_list.py

MILLION_NUMBERS = list(range(1_000_000))

def for_loop():
    output = []
    for element in MILLION_NUMBERS:
        if not element % 2:
            output.append(element)
    return output

# filter_list.py

MILLION_NUMBERS = list(range(1_000_000))

def list_comprehension():  #44.5 msec per loop
    return [number for number in MILLION_NUMBERS if not number % 2]

'''
$ python -m timeit -s "from filter_list import list_comprehension" "list_comprehension()"
5 loops, best of 5: 44.5 msec per loop
“For loop” is around 50% slower than a list comprehension (65.4/44.5≈1.47). And we just reduced five lines of code to one line! Cleaner and faster code? Great!
Can we make it better?
Filter a list with the “filter” function
Python has a built-in filter function for filtering collections of elements. This sounds like a perfect use case for our problem, so let’s see how fast it will be.

# filter_list.py

MILLION_NUMBERS = list(range(1_000_000))

def filter_function():
    return filter(lambda x: not x % 2, MILLION_NUMBERS)
    
$ python -m timeit -s "from filter_list import filter_function" "filter_function()" 。
1000000个循环，5个循环中的最佳循环：每个循环284纳秒。
284纳秒？太快了! 原来，过滤器函数返回的是一个迭代器。它不会立即超过100万个元素，但当我们要求它时，它将返回下一个值。
为了一次性得到所有的结果，我们可以把这个迭代器转换成一个列表。
'''

# filter_list.py
MILLION_NUMBERS = list(range(1_000_000))
def filter_function():  #每个循环284纳秒
    return filter(lambda x: not x % 2, MILLION_NUMBERS)


# filter_list.py
MILLION_NUMBERS = list(range(1_000_000))
def filter_return_list():  #104 msec per loop
    return list(filter(lambda x: not x % 2, MILLION_NUMBERS))
'''
$ python -m timeit -s "from filter_list import filter_return_list" "filter_return_list()"
2 loops, best of 5: 104 msec per loop

Now, its performance is not so great anymore. It’s 133% slower than the list comprehension
 (104/44.5≈2.337) and 60% slower than the “for loop” (104/65.4≈1.590).
While, in this case, it’s not the best solution, an iterator is an excellent alternative to 
a list comprehension when we don’t need to have all the results at once. If it turns out 
that we only need to get a few elements from the filtered list, an iterator will be a 
few orders of magnitude faster than other “non-lazy” solutions.

现在，它的性能已经不那么好了。它比
list comprehension(104/44.5≈2.337)慢了133%，
"for循环"(104/65.4≈1.590)慢了60%。
虽然在这种情况下，它并不是最好的解决方案，但当我们不需要一次得到所有结果时，迭代器是列表理解
的一个很好的替代方案。如果事实证明
我们只需要从过滤后的列表中获取几个元素，迭代器会比其他 "非懒惰 "的解决方案快几个数量级。
'''

#filterfalse()
#We could use the filterfalse() function from the itertools library to simplify the
# filtering condition. filterfalse returns the opposite elements than filter. It picks those elements that evaluate to False. Unfortunately, it doesn't make any difference when it comes to performance:
from itertools import filterfalse

def filterfalse_list():
    return list(filterfalse(lambda x: x % 2, MILLION_NUMBERS))
'''
$ python -m timeit -s "from filter_list import filterfalse_list" "filterfalse_list()"
2 loops, best of 5: 103 msec per loop
'''


'''
More than one operation in the loop
List comprehensions are often faster and easier to read, but they have one significant limitation. What happens if you want to execute more than one simple instruction? List comprehension can’t accept multiple statements (without sacrificing readability). But in many cases, you can wrap those multiple statements in a function.
Let’s use a slightly modified version of the famous “Fizz Buzz” program as an example. We want to iterate over a list of elements and for each of them return:
“fizzbuzz” if the number can be divided by 3 and 5
“fizz” if the number can be divided by 3
“buzz” if the number can be divided by 5
the number itself, if it can’t be divided by 3 or 5
Here is a simple solution:
'''

# filter_list.py

def fizz_buzz():
    output = []
    for number in MILLION_NUMBERS:
        if number % 3 == 0 and number % 5 == 0:
            output.append('fizzbuzz')
        elif number % 3 == 0:
            output.append('fizz')
        elif number % 5 == 0:
            output.append('buzz')
        else:
            output.append(number)
    return output

#Here is the list comprehension equivalent of the fizz_buzz():

print(['fizzbuzz' if x % 3 == 0 and x % 5 == 0 else 'fizz' if x % 3 == 0 else 'buzz' if x % 5 == 0 else x for x in MILLION_NUMBERS])
# It’s not easy to read - at least for me. It gets better if we split it into multiple lines:
print([
    "fizzbuzz" if x % 3 == 0 and x % 5 == 0
    else "fizz" if x % 3 == 0
    else "buzz" if x % 5 == 0
    else x
    for x in MILLION_NUMBERS
])

'''
But if I see a list comprehension that spans multiple lines, I try to refactor it. 
We can extract the “if” statements into a separate function:
'''

# filter_list.py

def transform(number):
    if number % 3 == 0 and number % 5 == 0:
        return 'fizzbuzz'
    elif number % 3 == 0:
        return 'fizz'
    elif number % 5 == 0:
        return 'buzz'
    return number

def fizz_buzz2():
    output = []
    for number in MILLION_NUMBERS:
        output.append(transform(number))
    return output

'''
Now it’s trivial to turn it into a list comprehension. And we get the additional 
benefit of a nice separation of logic into a function that does the “fizz buzz” 
check and a function that actually iterates over a list of numbers and applies 
the “fizz buzz” transformation.
Here is the improved list comprehension:

现在把它变成一个列表理解是很简单的。而且我们还得到了额外的好处，那就是将逻辑很好地分离为一个进行 
"嘶嘶声 "检查的函数和一个实际迭代一个数字列表并应用 "嘶嘶声 "转换的函数。
下面是改进后的列表理解。
'''
def fizz_buzz2_comprehension():
    return [transform(number) for number in MILLION_NUMBERS]
'''
Let’s compare all three versions:
$ python -m timeit -s "from filter_list import fizz_buzz" "fizz_buzz()"
2 loops, best of 5: 191 msec per loop

$ python -m timeit -s "from filter_list import fizz_buzz2" "fizz_buzz2()"
1 loop, best of 5: 285 msec per loop

$ python -m timeit -s "from filter_list import fizz_buzz2_comprehension" "fizz_buzz2_comprehension()"
1 loop, best of 5: 224 msec per loop

Extracting a separate function adds some overhead. List comprehension with a separate transform() function is around 17% slower than the initial “for loop”-based version (224/191≈1.173). But it’s much more readable, so I prefer it over the other solutions.
And, if you are curious, the one-line list comprehension mentioned before is the fastest solution:
提取一个单独的函数会增加一些开销。使用单独的transform()函数理解列表比最初的基于 "for循环 "的版本（224/191≈1.173）慢了17%左右。但它的可读性更强，所以我更喜欢它，而不是其他的解决方案。
而且，如果你好奇的话，之前提到的单行列表理解是最快的解决方案。

'''
def fizz_buzz_comprehension():
    return [
        "fizzbuzz" if x % 3 == 0 and x % 5 == 0
        else "fizz" if x % 3 == 0
        else "buzz" if x % 5 == 0
        else x
        for x in MILLION_NUMBERS
    ]
'''
$ python -m timeit -s "from filter_list import fizz_buzz_comprehension" "fizz_buzz_comprehension()"
2 loops, best of 5: 147 msec per loop

Fastest, but also harder to read. If you run this code through a code formatter 
like black (which is a common practice in many projects), it will further obfuscate 
this function:
'''

print([
    "fizzbuzz"
    if x % 3 == 0 and x % 5 == 0
    else "fizz"
    if x % 3 == 0
    else "buzz"
    if x % 5 == 0
    else x
    for x in MILLION_NUMBERS
])

'''
There is nothing wrong with black here - we are simply putting too much logic inside the list comprehension. If I had to say what the above code does, it would take me much longer to figure it out than if I had two separate functions. Saving a few hundred milliseconds of execution time and adding a few seconds of reading time doesn’t sound like a good trade-off 😉.
Clever one-liners can impress some recruiters during code interviews. But in real life, separating logic into different functions makes it much easier to read and document your code. And, statistically, we read more code than we write.
Conclusions
List comprehensions are often not only more readable but also faster than using “for loops.” They can simplify your code, but if you put too much logic inside, they will instead become harder to read and understand.
Even though list comprehensions are popular in Python, they have a specific use case: when you want to perform some operations on a list and return another list. And they have limitations - you can’t break out of a list comprehension or put comments inside. In many cases, “for loops” will be your only choice.
I only scratched the surface of how useful list comprehension (or any other type of “comprehension” in Python) can be. If you want to learn more, Trey Hunner has many excellent articles and talks on this subject (for example, this one for beginners).

这里的黑没有什么问题，我们只是在列表理解里面放了太多的逻辑。如果要我说上面的代码是做什么的，那我要花的时间比我有两个独立的函数要长得多。节省几百毫秒的执行时间，增加几秒的读取时间，听起来并不是一个好的取舍"■▄。
在代码面试时，聪明的一语中的，可以打动一些招聘人员。但在现实生活中，将逻辑分离成不同的函数会让你的代码更容易阅读和记录。而且，据统计，我们读的代码比写的代码多。
结论
列表理解通常不仅比使用 "for循环 "更易读，而且速度更快。它们可以简化你的代码，但如果你在里面放了太多的逻辑，它们反而会变得更加难以阅读和理解。
尽管列表理解在Python中很流行，但它们有一个特定的用例：当你想在一个列表上执行一些操作并返回另一个列表时。而且它们有局限性--你不能脱离一个列表理解，也不能在里面加注释。在很多情况下，"for循环 "将是你唯一的选择。
我只是对列表理解(或Python中任何其他类型的 "理解")的有用性做了一个小结。如果你想了解更多，Trey Hunner 有很多关于这个主题的优秀文章和讲座 (例如，这个初学者的文章)。

'''