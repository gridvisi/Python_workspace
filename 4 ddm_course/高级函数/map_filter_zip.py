def square(number):
    return number*number
numbers = [1,2,3,4,5]

#Without map()
def square(number):
    return number*number

numbers = [1,2,3,4,5]
squared_numbers = []

for number in numbers:
    squared = square(number)
    squared_numbers.append(squared)
print(squared_numbers)
#With map()
def square(number):
    return number*number

numbers = [1,2,3,4,5]
squared_numbers = list(map(square, numbers))
print(squared_numbers)

'''
Using map() we don't need to create an empty list that we append to in a for loop.
使用map（）我们不需要创建在for循环中附加到的空列表。
We do not need to use square() with parenthesis as the function parameter, as map() 
will call the function for us, we just pass the function object.
我们不需要使用带圆括号的square（）作为函数参数，因为map（）会为我们调用函数，我们只是传递函数对象。
map() will run square() for each item in numbers.
map（）将以数字形式为每个项运行square（）。

Filter
过滤器
Python's filter() function checks a condition of each element in an iterable and returns a filtered data structure only containing elements who match the given conditions.
Python的filter（）函数检查iterable中每个元素的条件，并返回仅包含与给定条件匹配的元素的过滤数据结构。
filter() will take 2 required positional arguments. 1.) A function to run against iterables. 2.) An iterable (ie. list).
filter（）将采用2个必需的位置参数。（1）一个函数，用来运行iterables。（2）一份切实可行的清单。
The function passed to filter() must return a boolean (True or False)

传递给filter（）的函数必须返回布尔值（True或False）
The expected output of this would be a filter object with a memory position which we will then convert to a list().
它的预期输出将是一个具有内存位置的filter对象，然后我们将其转换为list（）。
Lets take an example that applies the function even() to a list of integers. The objective here is to get a list that only contains even numbers.
让我们举一个将even（）函数应用于整数列表的例子。这里的目标是得到一个只包含偶数的列表。
'''

def even(number):
    if (number % 2) == 0:
        return True
    return False
numbers = [1,2,3,4,5]

#Without filter()
def even(number):
    if (number % 2) == 0:
        return True
    return False

numbers = [1,2,3,4,5]

even_numbers = []
for number in numbers:
    if even(number):
        even_numbers.append(number)
print(even_numbers)

#With filter()
def even(number):
    if (number % 2) == 0:
        return True
    return False

numbers = [1,2,3,4,5]
even_numbers = list(filter(even, numbers))
print(even_numbers)
'''
What we observed:
我们观察到：
Using filter() we don't need to create an empty list that we append to in a for loop.
使用filter（）我们不需要创建在for循环中附加到的空列表。
We do not need to use even() with parenthesis as the function parameter, as filter() will call the function for us, we just pass the function object.
我们不需要使用带圆括号的even（）作为函数参数，因为filter（）将为我们调用函数，我们只传递函数对象。
filter() will run even() for each item in numbers and remove all elements that returned False.
filter（）将对每个数字项运行even（），并删除返回False的所有元素。


Zip
Python's zip() function combines elements of 2 lists with matching indexes into an interable of tuples.
Python的zip（）函数将两个列表的元素与匹配的索引组合成一个元组的可循环项。

zip() will take an undefined number of arguments where each argument is an iterable to zip.
zip（）将采用未定义数量的参数，其中每个参数都是zip的iterable。

zip([...], [...], [...], ...)
zip（[…]，[…]，[…]，…）

The expected output of this would be a zip object containing tuples of the same-index element of each iterable with a memory position which we will then convert to a list().
它的预期输出将是一个zip对象，其中包含每个iterable的相同索引元素的元组，并具有一个内存位置，然后将其转换为list（）。

Let's take the above 2 examples combined to create a list of even numbers with their respective squared results.
让我们结合上面的两个例子来创建一个偶数列表及其各自的平方结果。
'''

def even(number):
    if (number % 2) == 0:
        return True
    return False

def square(number):
    return number*number

numbers = [1,2,3,4,5]
even_numbers = list(filter(even, numbers))
even_numbers_squared = list(map(square, even_numbers))
print('mark',even_numbers,even_numbers_squared)

#Without zip()
...
even_numbers = [2,4]
even_numbers_squared = [4, 16]
combined = []

for number in even_numbers:
    squared = even_numbers_squared[even_numbers.index(number)]
    squared_tuple = (number, squared)
    combined.append(squared_tuple)
print('Without zip()',combined)

#With zip()
...
even_numbers = [2,4]
even_numbers_squared = [4, 16]
zipped_result = list(zip(even_numbers, even_numbers_squared))
print('With zip()',zipped_result)


A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]
print(A0,A1,A2,A3,A4,A5,A6)

import numpy as np
arr = np.array([1, 3, 2, 4, 5])
print(arr.argsort()[-3:][::-1])