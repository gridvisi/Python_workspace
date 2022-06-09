# https://realpython.com/quizzes/python-data-types/viewer/
#1
'''
In Python 3, the maximum value for an integer is 263 - 1:


True

Incorrect

False

Incorrect

In Python 2, there was an internal limit to how large an
integer value could be. But that limit was removed in Python 3.

This means there is no explicitly defined limit, but the
amount of available address space forms a practical limit
depending on the machine Python runs on.

在Python 2中，有一个内部限制，即一个整数可以有多大。
整数值的内部限制。但是这个限制在Python 3中被取消了。

这意味着没有明确定义的限制，但是
可用的地址空间的数量形成了一个实际的限制
取决于 Python 运行的机器。
'''

#2
'''
How would you express the hexadecimal value a5 as a base-16 integer constant in Python?

hex('a5')
Incorrect
TypeError: 'str' object cannot be interpreted as an integer

This is what we expected to see:
0xa5

'''

#3
'''
How would you express the constant floating-point 
value 3.2 × 10-12 in Python:

32*10**-12
Incorrect
3.2e-11 != 3.2e-12

This is what we expected to see:
3.2e-12

We’re looking for a constant value, so an 
expression like 3.2 * 10 ** -12 would not be a valid 
answer in this case.
'''

#4
'''
Which of the following are valid ways to specify 
the string literal foo'bar in Python:


'foo''bar'


"""foo'bar"""

Correct

'foo'bar'


'foo\'bar'

Incorrect

"foo'bar"

Correct
为一个由下列ASCII字符组成的字符串字头写一个表达式。

水平制表符
换行符（ASCII换行符）字符
十六进制值为7E的字符

为一个由下列ASCII字符组成的字符串字头写一个表达式。

水平制表符
换行符（ASCII换行符）字符
十六进制值为7E的字符
ox7E
不正确
NameError: name 'ox7E' is not defined

这就是我们期望看到的。
"\t\n\x7E"

'\t'是水平制表符的转义序列。

\n'是换行字符的转义序列。

要通过十六进制值指定一个字符，使用'\xhh'，其中hh指定十六进制数字。

下面是几个可能的正确答案。

"\t\n\x7E"
'\t\n\x7E
''''\t\nx7E''''。
""\t\nx7E""
'''

#5
'''
Consider this statement:

>>> print(r'foo\\bar\nbaz')
Which of the following is the correct REPL output?


foo\\barnbaz


foo\\bar\nbaz


foo\bar
baz


foo\bar\nbaz


The r character preceding the string indicates a raw string. Escape sequences are stripped of their special meaning.
'''

#6
'''
Which of the following is not a Python built-in function:


repr()

Incorrect

map()


round()


diff()

Incorrect

isinstance()

python3编程基础：str()、repr()的区别

python中转换成字符有两种方法：str()和repr()，这两种又有什么区别？什么时候用str？什么时候用repr?
str()函数：将值转化为适于人阅读的字符串的形式
repr()函数：将值转化为供解释器读取的字符串形式

代码示例
下面我们用例子来说明两个函数是差异点，还有就是print输出字符串时需要注意的点

将整型转换为字符串
原文链接：https://blog.csdn.net/kongsuhongbaby/article/details/87398394
'''

class Test:
    pass

print(str(Test()))
print(repr(Test()))
print(str(Test()) == repr(Test()))

class Test1:
    def __str__(self):
        return "Test1.__str__"

print(str(Test1()))
print(repr(Test1()))
print(str(Test1()) == repr(Test1()))

class Test2:
    def __repr__(self):
        return "Test2.__str__"

print(str(Test2()))
print(repr(Test2()))
print(str(Test2()) == repr(Test2()))
'''
通过上述两个例子的对比，我们可以知道: 当仅定义 __repr__ 的时候， 
__repr__ == __str__, 但是仅定义 __str__ 的情况下，两者不相等
'''

#两者均定义
class Test3:
    def __repr__(self):
        return "Test3.__repr__"
    def __str__(self):
        return "Test3.__str__"


print(str(Test3()))
print(repr(Test3()))
print(str(Test3()) == repr(Test3()))

'''
两者的区别
_str_用于为最终用户创建输出，而 _repr_ 主要用于调试和开发。 _repr_ 的目标是明确无误，_str_ 是可读的
_repr_ 用于推断对象的"官方"字符串表示形式（包含有关对象的所有信息的表示, _str_ 用于推断对象的“非正式”字符串表示形式（对打印对象有用的表示形式
再通过一个例子说明问题:
'''

import datetime
today = datetime.datetime.now()

print(str(today))
print(repr(today))
'''
输出结果如下:

>>> print(str(today))
2018-08-22 16:52:37.403320
>>> print(repr(today))
datetime.datetime(2018, 8, 22, 16, 52, 37, 403320)
'''
#https://stackoverflow.com/questions/1436703/what-is-the-difference-between-str-and-repr
#https://docs.python.org/3/reference/datamodel.html#object.__repr__



#https://www.geeksforgeeks.org/str-vs-repr-in-python/

import datetime

today = datetime.datetime.now()

# Prints readable format for date-time object
print(str(today))

# prints the official format of date-time object
print(repr(today))


# Python program to demonstrate writing of __repr__ and
# __str__ for user defined classes

# A user defined class to represent Complex numbers
class Complex:

    # Constructor
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # For call to repr(). Prints object's information
    def __repr__(self):
        return 'Rational(%s, %s)' % (self.real, self.imag)

        # For call to str(). Prints readable form

    def __str__(self):
        return '%s + i%s' % (self.real, self.imag)

    # Driver program to test above


t = Complex(10, 20)

# Same as "print t"
print(str(t))
print(repr(t))