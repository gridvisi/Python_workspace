
'''
Which keyword prevents changing variables in a nested function?
The keyword nonlocal indicates that a variable inside a nested
function does not belong to the scope of that inner function
but to the function encapsulating it.

```
def myfunc1():
    x = "John" def myfunc2():
    x = "hello" myfunc2()
    return x print(myfunc1())

    ``` will output: ```
    John
    ``` The keyword global is different.
    It indicates that the scope of a variable is defined at the module level
'''

def myfunc1():
    x = "John"
    def myfunc2():
        x = "hello"
    myfunc2()
    return x
print(myfunc1())

global x
x = "Hello"
def myfunc1():
    def myfunc2():
        x = "John"
    myfunc2()
    return x
print(myfunc1())

#What is the output of the code snippet below?

a = {}
b = {}
print(a is b)
# https://towardsdatascience.com/assignment-shallow-or-deep-a-story-about-pythons-memory-management-b8fad87bfa6c


#In Python, 'Hello', is the same as "Hello".

False

True
# https://www.geeksforgeeks.org/single-and-double-quotes-python/
print("'WithQuotes'")
print("Hello 'Python'")
print('"WithQuotes"')
print('Hello "Python"' )


'''
A decorator can be decorated with itself.
Wrong!👎

A decorator cannot be decorated with itself. Something like:


@my_decorator
def my_decorator(a_function):
    print("This is decorated")
    return a_function

will throw a NameError exception. 
'''

# bit operator
'''
https://www.geeksforgeeks.org/python-bitwise-operators/
https://stackoverflow.com/questions/7075082/what-is-future-in-python-used-for-and-how-when-to-use-it-and-how-it-works


10 位操作符合？
如果其中一个位是1，另一个位是0，哪个位运算符给出1，否则返回假？
Which bitwise operator gives 1 if one of the bit is 1 and other is 0 else returns False?
```
AND

XOR

NOT

OR

None of the above
'''

'''
正确！👍
https://stackoverflow.com/questions/22224094/can-python-list-and-dictionary-be-nested-infinitely

字典可以无限地嵌套。唯一的限制是可用的内存。
'''

##14  字典可以无限地嵌套吗？
#正确！👍字典可以无限地嵌套。唯一的限制是可用的内存。

a = {'a1':[{'a2':{'a3':[4,5,6]}}]}

eval(70*'['+70*']')
#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[
# [[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
# ]]]]]]]]]]]

#下面的代码片断的输出是什么？
print(reversed("hello") == "olleh")
# https://www.programiz.com/python-programming/methods/built-in/reversed

#What is the output of the code snippet below?
print("python"[-4:0:-2])
#https://stackoverflow.com/questions/509211/understanding-slicing


def make_bold(fn):
    return lambda: "<b>" + fn() + "</b>"

def make_italic(fn):
    return lambda: "<i>" + fn() + "</i>"

@make_bold
@make_italic
def hello():
    return "hello world"

helloHTML = hello()
print(helloHTML)

#What is the outputofthefollowingcodesnippet?
f = None
with open("data.txt", "w") as f:
    pass
print(f.closed)

#20  subclass()可以接受类实例作为属性吗？No!
class MyDict(dict):
    pass

print(issubclass(MyDict, dict))

#However, this will throw a TypeError exception:

class MyDict(dict):
    pass

my_dict = MyDict()
a_dict = dict()

print(issubclass(my_dict, a_dict))
