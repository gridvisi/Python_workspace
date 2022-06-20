
#As written, the following statement is invalid because
# it is split across several lines. Modify it so it doesn’t
# raise an exception, using implicit line continuation:
'''
下面的语句是无效的，因为它被分成了几行。修改它，使它不会引发异常，使用隐式续行。

#1 s = 'a' + 'b'
    + 'c' + 'd'
    + 'e' + 'f'
'''
s = ('a' + 'b'
    + 'c' + 'd'
    + 'e' + 'f'
)

'''
任何包含开头小括号 ('(')、方括号 ('[') 或大括号 ('{') 的语句都会被 
Python 解释器理解为不完整，可以跨行继续，直到遇到相应的小括号、大括号
或小括号。因为小括号、大括号和大括号对 Python 语法来说是如此不可或缺，
这给了你充分的机会进行隐式续行。

在整个表达式周围分组的小括号在语法上可能是不必要的，但往往还是包括在内，
以便语句可以跨行继续。

PEP 8 推荐在可行的时候使用隐式续行。
'''


s = 'a' + 'b' \
    + 'c' + 'd' \
    + 'e' + 'f'
'''
明确的续行是通过在要续行的每一行的末尾指定一个反斜杠字符（\）来实现的。

记住，反斜杠必须是续行的最后一个字符。它后面不能有任何东西--甚至不能有
空白。

>>> print('foo', 'bar', \)  
  文件"<stdin>"，第1行
    print('foo', 'bar', \)
                            ^
语法错误：在行的延续字符后有意外字符
(在高亮行的反斜杠后有两个空格字符)。
'''


