# https://realpython.com/python-program-structure/#multiple-statements-per-line


'''
s = 'a' + 'b'
    + 'c' + 'd'
    + 'e' + 'f'

任何包含开头小括号 ('(')、方括号 ('[') 或大括号 ('{') 的语句都会被
Python 解释器理解为不完整，可以跨行继续，直到遇到相应的小括号、大括号
或小括号。因为小括号、大括号和大括号对 Python 语法来说是如此不可或缺，
这给了你充分的机会进行隐式续行。

在整个表达式周围分组的小括号在语法上可能是不必要的，但往往还是包括在内，
以便语句可以跨行继续。

PEP 8 推荐在可行的时候使用隐式续行。
'''

s = ('a' + 'b'
    + 'c' + 'd'
    + 'e' + 'f'
)

s = 'a' + 'b' \
    + 'c' + 'd' \
    + 'e' + 'f'
'''
明确的续行是通过在要续行的每一行的末尾指定一个反斜杠字符（\）来实现的。

记住，反斜杠必须是续行的最后一个字符。它后面不能有任何东西--甚至不能有空白。

>>> print('foo', 'bar', \)  
  文件"<stdin>"，第1行
    print('foo', 'bar', \)
                            ^
语法错误：在行的延续字符后有意外字符
(在高亮行的反斜杠后有两个空格字符)。
'''


'''
关于Python中每行的多条语句，以下哪些是真的。


PEP 8不鼓励将多个语句放在一行中。

不正确

在一行中指定一个以上的语句通常不被认为是Pythonic的，但如果它能提高可读性，则可以接受。

正确

同一行中的多个语句用&字符隔开。


只有变量赋值语句可以在一行中重复出现。


正确答案
PEP 8通常不鼓励在一行中放置多个语句。在你可能考虑这样做的情况下，
通常有一个更符合Pythonic的方法来实现你的愿望。

另一方面，PEP 8还说："愚蠢的一致性是小脑袋的恶魔"。知道什么时候不一致是合适的是很好的。最重要的是，可读性是最重要的。

不正确的答案
用来分隔同一行的语句的字符是分号（；），而不是&。

任何简单的语句都可以在一行中出现多条。这包括变量赋值语句，但不限于它们。

回顾一下。每行多条语句
'''

'''
列举了Python代码的风格准则的Python增强提案(PEP)是。


PEP 8000


PEP 257


PEP 8

纠正

PEP 20


Python代码的风格指南在PEP 8中列出。关于Docstring约定的相关信息在PEP 257中规定。

有关其他PEP的列表，请参见PEP索引。

回顾一下。续行
'''


'''
Which one of the following comments is syntactically incorrect:


x = 1 + 2 + 3 \  # Comment
    + 4 + 5
Incorrect

d = {'a': 1, 'b': 2}  # Comment

        # Comment

s = set([
    'foo',
    'bar',  # Comment
    'baz'
])
Incorrect

# Comment

A comment may appear at the end of a statement, and on a line by itself. A comment may also appear within a statement that spans multiple lines by implicit line continuation.

But a comment can’t follow the backslash character that signifies 
explicit line continuation. With explicit line continuation, the 
backslash character must be the final character on the line.

注释可以出现在语句的末尾，也可以单独出现在一行。注释也可以出现在一个跨越多行的语句中，通过隐式续行。

但是注释不能出现在表示显式行延续的反斜杠字符之后。在显式行延续中，反斜杠字符必须是该行的最后一个字符。
'''

'''
Which one of the following statements about block comments is true:


Block comments should always be specified using triple-quoted multiline string literals.


There is no way to create a multiline block comment in Python.


You can create a block comment in Python by using a triple-quoted 
multiline string literal. However, PEP 8 discourages the practice 
because, by convention, that type of free-standing triple-quoted 
string literal is reserved for function docstrings.
'''

'''
Which of the following conform to the PEP 8 recommendations for whitespace in expressions and statements:


print(x) ; print(y)

a.insert (1, 100)
Incorrect

x = a[1::2]
Correct

d = {'foo': 100, 'bar': 200}
Correct

t = (100, )

Correct Answers
d = {'foo': 100, 'bar': 200}
There should not be whitespace immediately inside curly braces, nor immediately before a colon.
x = a[1::2]
Colons in slice notation should have equal amounts of space on each side. When a slice parameter is omitted, the space is omitted.
Incorrect Answers
All of the following are syntactically correct; they all work. But they are stylistically discouraged:

a.insert (1, 100)
Whitespace between a function or method name and the opening parenthesis is definitely frowned upon.
t = (100, )
PEP 8 specifically recommends against whitespace between the trailing comma and closing parenthesis when defining a singleton tuple.
print(x) ; print(y)
This one actually fails on two counts. Whitespace immediately before a semicolon is not recommended. And, of course, neither is two statements on the same line.
Review: Whitespace

正确答案
d = {'foo': 100, 'bar': 200}。
大括号内不能有空白，冒号前也不能有空白。
x = a[1::2]
分片符号中的冒号应该在两边有等量的空间。当一个切片参数被省略时，空格也被省略了。
不正确的答案
以下所有的句法都是正确的，它们都可以使用。但从风格上来说，它们是不受欢迎的。

a.insert (1, 100)
在函数或方法的名称和开头的小括号之间留白是绝对不可取的。
t = (100, )
PEP 8特别建议在定义单子元组时，不要在尾部逗号和结尾小括号之间留白。
print(x) ; print(y)
这条建议实际上在两个方面都失败了。不建议在分号前留白。当然，在同一行中的两个语句也是如此。
回顾一下。空白

'''

'''
Consider the following sequence of statements:

x, y = 1, 2
    z = 3

print(x, y, z)
Execution of these statements will:


Succeed without error


Generate an exception

Correct

This question was probably a gimme. But this is really an important concept in Python: leading whitespace in front of a statement is significant. Indentation is used to determine grouping of statements.

>>> x, y = 1, 2
>>>     z = 3
  File "<stdin>", line 1
    z = 3
    ^
IndentationError: unexpected indent

>>> print(x, y, z)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'z' is not defined
You can’t just indent statements at will in Python.
'''

