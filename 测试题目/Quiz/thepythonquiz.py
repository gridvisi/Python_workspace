

#1 What is the correct command to shuffle the list below?
fruit=['apple', 'banana', 'papaya', 'cherry']
'''
random.shuffle(fruit)
fruit.shuffle()
random.shufflelist(fruit)
shuffle(fruit)


Comment on Twitter:
What is the correct command to shuffle the list below?
fruit=['apple', 'banana', 'papaya', 'cherry']

random.shuffle(fruit)

fruit.shuffle()

random.shuffleList(fruit)

shuffle(fruit)#python #python3 #pythonprogramming #learnpython

— The Python Quiz (@thepythonquiz) September 20, 2020
'''

#2 How many protocols does Pickle have?
'''
pickle has 5 protocols. The latest protocol version 5 was added in Python 3.8. 
(docs.python.org/3/library/pickle.html#pickle-protocols)


'''

#3
'''
What it the output of the code snippet below?
print(float(False))

What it the output of the code snippet below?
print(float(False))

It will throw a ValueError error.

0.0

0
The float() function casts True to 1.0 and False to 0.0 . 
(docs.python.org/3/library/functions.html#float)
'''

#4
'''
What is the output of the code snippet below?
class Foo(object):
    def __init__(self):
        self.__method()
    def __method(self):
        print('42')

class MoreFoo(Foo):
    def __method(self):
        print('41')

MoreFoo()

rong!👎

As __method() is a private method (recognisable by the double 
underscores __ ), it cannot be overridden by simply defining 
it as __method(self) in the subclass (to avoid accidental override). 
To force overridding, it has to be redefined as def _Foo__method(self): . 
This is called name mangling. 
(stackoverflow.com/questions/14898197/override-private-met...)


由于__method()是一个私有方法（可以通过双下划线__来识别），它不能通过在子类中简单地定
义为__method(self)而被重写（以避免意外的重写）。为了强制覆盖，它必须被重新定义为 
def _Foo__method(self): 。这就是所谓的名称混用。
(stackoverflow.com/questions/14898197/overrid-private-met...)
'''
class Person(object):
    def __init__(self):
        self.__method()

    def __method(self):
        print('I am student')

class Moreperson(Person):
    def __method(self):
        print('I am teacher')

Moreperson()

'''
#开放-封闭原则说：永远不要重写代码。

L：利斯科夫替代原则。(LSP)

BaseType必须可以被它的subTypes所替代

这个原则定义了子类的对象必须可以替代其超类的对象而不破坏应用。

这要求子类的对象具有与它们的超类相同的行为，如果一个超类可以做某项工作，那么子类有必要可以做与它的超类相同的工作。

利斯科夫替代原则与继承密切相关。它通过关注超类及其子类型的行为，扩展了开放-封闭原则。

通过一个例子可以很好地理解这个原则。想象一下，有一个执行以下操作的类Animal：

说话

吃东西

走路

我们有一个子类，猫，它是一种动物，继承了超类动物，并且有它的行为，说话、吃东西和走路。
因此，这适用于利斯科夫替代原则。

'''
class Animal:  #(object)
    def __init__(self,talk,eat,walk):
        self.talk = talk
        self.eat = eat
        self.walk = walk

cat = Animal('喵喵','鱼','猫步')
print(cat.talk)
print(cat.eat)
print(cat.walk)

snail = Animal('不能说话','叶子','爬行')
print(snail.talk)
'''

但是我们假设有一个子类，蜗牛，它仍然是一个动物，但是不能说话，
所以它不能继承超类的动物。这就破坏了Liskov替代原则。

总而言之，如果你对父类型说的是真的，那么它在整个链条中都必须是真的。
如果你说父类型可以做某事，那么所有的子类型也需要能够做这件事。

'''
class Circle(object):
   __pi = 3.14

   def __init__(self, r):
       self.r = r

   @classmethod
   def pi(cls):
       return cls.__pi

   def area(self):
       """
圆的面积
       """
       return self.r ** 2 * self.__pi

print(Circle.pi())  # 没有实例化 能直接访问pi() 方法
circle1 = Circle(2)
print(circle1.pi()) # 也可以通过实例访问pi()方法
print(circle1.area()) #12.56

# 无法通过实例访问 pi
# 不使用classmethod
class Circle(object):
   __pi = 3.14

   def __init__(self, r):
       self.r = r

   #@classmethod
   #def pi(cls):
   #    return cls.__pi

   def area(self):
       """
圆的面积
       """
       return self.r ** 2 * self.__pi

print(circle1.area()) # 成功输出 12.56
#print(Circle.pi())  # 直接访问pi()方法
circle1 = Circle(2)
#print(circle1.pi()) # 通过实例访问pi()方法


# Circle类下的pi()方法被 @classmethod 装饰后，
# 我们能通过Circle.pi() 直接运行方法，不用实例化类。
# 示例：重构构造__init__() 方法应用, 格式化创建时间实例
import datetime
class Date(object):
   day = 0
   month = 0
   year = 0

   def __init__(self, year=0, month=0, day=0):
       self.day = day
       self.month = month
       self.year = year

   @classmethod
   def from_string(cls, date_as_string):
       year, month, day = date_as_string.split('-')
       date = cls(year, month, day)
       return date

d = datetime.date.today()
print(d)

d = "2022-4-21"
date1 = Date.from_string(d)  #  直接使用固定格式的字符串就能创建Date的实例
print(date1.year, date1.month, date1.day)

#5
'''
A function can access a variable defined out of the function 
even if is not set as global.

Correct!👍

This is true, as long as the function does not change the value 
of the variable. To do so, the variable has to be set as global 
with the global keyword. 
(geeksforgeeks.org/global-keyword-in-python)

这是真的，只要函数不改变变量的值。
要做到这一点，必须用global关键字将该变量设置为全局变量。
(geekforgeeks.org/global-keyword in-python)
'''

#6 Which one of these modules doesn't have the ability to copy files?
'''
filecamp
shutil
subprocess
os

shutil , os and subprocess have functions allowing to copy files, 
in different ways. filecmp has another utility, it defines functions 
used to compare files and directories. 
(stackoverflow.com/questions/123198/how-do-i-copy-a-file-i...)
'''

#7 Which command starts the Django local development server?
'''
Wrong!👎

manage.py runserver starts a Django development server on a local machine. 
Do not use this in production! (docs.djangoproject.com/fr/3.0/ref/django-admin)
'''

#8 The Python standard library supports more numerical types than NumPy.
'''
NumPy supports a much greater variety of numerical types than Python does. The NumPy data types are called dtypes. 
(tutorialspoint.com/numpy/numpy_data_types.htm)
'''

#9
'''
What is the output of the code snippet below?
a = 1
a -= 2 + 3
print(a)
'''

#10
'''
What is the output of the code snippet below?
print(list("hello"))

'''

'''
What is the type of the returned object in the code snippet below?
def foo(*args):
    return args


foo(1, 2, 3)

which?
dict
list
tuple
'''

#12
'''
What is the output of the code snippet below?
number = 28
for num in range(25, 30):
    if number > num:
        print(num)
    else:
        print(num)
        break
'''

'''
What it the output of the code snippet below?
print(float("56%"))

Correct!👍

The float() option cannot cast a string containing the % character. 
(docs.python.org/3/library/functions.html#float)
'''

#13
'''
This question is sponsored by NordVPN.

What encryption technology does NordVPN use to secure its traffic?

Correct!👍

NordVPN uses military-grade AES-256-GCM encryption to secure its traffic, using only the most secure protocols: OpenVPN (UDP and TCP), IKEv2/IPSec and NordLynx (based on WireGuardⓒ).


Start navigating privately and securely today with NordVPN.
'''

#14
'''
Which one of those is not a Web Framework for Python?

Angular

web2py

TurboGears

Angular is a JavaScript Web Framework! 
(wiki.python.org/moin/WebFrameworks)
'''

'''
Which sentence is part of The Zen of Python?

Complex is better than simple.

Simple is better than complicated.

Simple is better than complex.

Complicated is better than simple.

Correct!👍

In Python console, typing import this will display 
the Zen of Python poem: Beautiful is better than ugly. 
Explicit is better than implicit. Simple is better than complex. 
Complex is better than complicated. Flat is better than nested. 
Sparse is better than dense. Readability counts. 
Special cases aren't special enough to break the rules. 
Although practicality beats purity. Errors should never pass silently. 
Unless explicitly silenced. 
In the face of ambiguity, refuse the temptation to guess. 
There should be one-- and preferably only one --obvious way to do it. 
Although that way may not be obvious at first unless you're Dutch. 
Now is better than never. 
Although never is often better than *right* now. 
If the implementation is hard to explain, it's a bad idea. 
If the implementation is easy to explain, it may be a good idea. 
Namespaces are one honking great idea -- let's do more of those! 
(python.org/dev/peps/pep-0020)

'''

#16
'''
What it the output of the code snippet below?
print(float(""))

0.0

0

None

It will throw a ValueError error.
'''

#17
'''
What is the output of the code snippet below?
print(max(3, 0, 3.0, 0.3, 0))

3

3.0

0

0.0

0.3

Within the max() function, elements are separated by comas. Hence, the maximum elements are 3 and 3.0 . The max() function works in a way that an integer will be detected as max over a float with the same value. 
(thepythonguru.com/python-builtin-functions/max)
'''

#18
'''
In the Python world, what does ORM stand for?

Oklahoma Railway Museum

Optimal Resource Mapping

Optically Remote Module

Operational Risk Manager

Object Relational Mapper

In the Python world, an object-relational mapper (ORM) is a code library that automates the transfer of data stored in relational database tables into objects that are more commonly used in application code.
 (fullstackpython.com/object-relational-mappers-orms.html)
'''

#19
'''
CPython is:

interpreted.

compiled.

Both

CPython is both compiled and interpreted. When CPython is asked to run code, it first: compiles the code the bytecode (.pyc files). Bytecode is platform-independent. Then, CPython routes the bytecode to the Python Virtual Machine (PVM) for execution. The PVM is an interpreter, that can be seen as the runtime engine of Python. 
(https://stackoverflow.com/questions/6889747/is-python-interpreted-or-compiled-or-both)
'''

#19
'''
Is this code correct?
while true:
print("Hello, world!")

Yes

No

This code snippet is not correct. True represents the true value of the bool built-in type. It is always written with an uppercase T. 
(docs.python.org/3/library/constants.html)
'''

#21
'''
Which sentence is part of The Zen of Python?

Nested is better than flat.

Flat is better than nested
'''

#22
'''
What is the output of the code snippet below?
result = 0


def find_sum(num1, num2):
    if num1 != num2:
        result = num1+num2
    else:
        result = 2*(num1+num2)
        
        
find_sum(3, 4)
print(result)
find_sum(5, 5)
print(result)

In both calls of the find_sum() function, 
result is only modified within the scope of the function 
(it doesn't have the global keyword). 
Within the scope of the module, result still equals to 0. 
(w3schools.com/python/gloss_python_global_variables.asp)
'''

result = 0
def find_sum(num1, num2):
    if num1 != num2:
        result = num1 + num2
    else:
        result = 2 * (num1 + num2)

find_sum(3, 4)
print(result)
find_sum(5, 5)
print(result)

# return

result = 0
def find_sum(num1, num2):
    if num1 != num2:
        result = num1 + num2
        return result
    else:
        result = 2 * (num1 + num2)
        return result

find_sum(3, 4)
print(result)
find_sum(5, 5)
print(result)



#2 return

result = 0
def find_sum(num1, num2):
    if num1 != num2:
        result = num1 + num2
        #return result
    else:
        result = 2 * (num1 + num2)
    return result

print(find_sum(3, 4))
print(result)

print(find_sum(5, 5))
print(result)


#3 return

#result = 0
def find_sum(num1, num2):
    if num1 != num2:
        result = num1 + num2
        return result
    else:
        result = 2 * (num1 + num2)
        return result

find_sum(3, 4)
print(result)
find_sum(5, 5)
print(result)
