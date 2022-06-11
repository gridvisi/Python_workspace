# https://www.codewars.com/kata/5c8bfa44b9d1192e1ebd3d15/train/python

#https://blog.csdn.net/sunxb10/article/details/81036693
'''
Wolves have been reintroduced to Great Britain.
You are a sheep farmer, and are now plagued by
wolves which pretend to be sheep. Fortunately,
you are good at spotting them.

Warn the sheep in front of the wolf that it is
about to be eaten. Remember that you are standing
at the front of the queue which is at the end of
the array:

[sheep, sheep, sheep, sheep, sheep, wolf, sheep, sheep]      (YOU ARE HERE AT THE FRONT OF THE QUEUE)
   7      6      5      4      3            2      1
If the wolf is the closest animal to you, return "Pls go away and stop eating my sheep". Otherwise, return "Oi! Sheep number N! You are about to be eaten by a wolf!" where N is the sheep's position in the queue.
Note: there will always be exactly one wolf in the array.

Tags:

FUNDAMENTALS ARRAYS LOOPS CONTROLFLOW BASIC LANGUAGE FEATURES

Examples
Input: ["sheep", "sheep", "sheep", "wolf", "sheep"]
Output: "Oi! Sheep number 1! You are about to be eaten by a wolf!"

Input: ["sheep", "sheep", "wolf"]
Output: "Pls go away and stop eating my sheep"
'''
sheeps = ['sheep', 'wolf', 'pig','sheep', 'sheep', 'sheep', 'sheep', 'sheep']
print(sheeps.index('wolf'))
print(f"Oi! Sheep number {sheeps.index('wolf')+1}! You are about to be eaten by a wolf!")


# Tips f-string大括号内所用的引号不能和大括号外的引号定界符冲突，可根据情况灵活切换 ' 和 "：

name = 'Eric'
f'Hello, my name is {name}'
'Hello, my name is Eric'

number = 7
f'My lucky number is {number}'
'My lucky number is 7'

price = 19.99
f'The price of this book is {price}'
'The price of this book is 19.99'
f'A total number of {24 * 8 + 4}'
'A total number of 196'

f'Complex number {(2 + 2j) / (2 - 3j)}'
'Complex number (-0.15384615384615388+0.7692307692307692j)'

name = 'ERIC'
f'My name is {name.lower()}'
'My name is eric'

import math
f'The answer is {math.log(math.pi)}'
'The answer is 1.1447298858494002'


'''
f"He said {"I'm Eric"}"
f"He said {"I'm Eric"}"
                ^
SyntaxError: invalid syntax

'''

f"""He said {"I'm Eric"}"""
"He said I'm Eric"
print(f'''He said {"I'm Eric"}''')
"He said I'm Eric"


#大括号外的引号还可以使用 \ 转义，但大括号内不能使用 \ 转义：

f'''He\'ll say {"I'm Eric"}'''
"He'll say I'm Eric"
#f'''He'll say {"I\'m Eric"}'''
#  File "<stdin>", line 1
#SyntaxError: f-string expression part cannot include a backslash

#f-string大括号外如果需要显示大括号，则应输入连续两个大括号 {{ 和 }}：

f'5 {"{stars}"}'
'5 {stars}'
f'{{5}} {"stars"}'
'{5} stars'

#上面提到，f-string大括号内不能使用 \ 转义，事实上不仅如此，f-string大括号内根本就不允许出现 \。如果确实需要 \，则应首先将包含 \ 的内容用一个变量表示，再在f-string大括号内填入变量名：
'''
f"newline: {ord('\n')}"
  File "<stdin>", line 1
SyntaxError: f-string expression part cannot include a backslash
'''



newline = ord('\n')
print(f'newline: {newline}')
'newline: 10'

#多行f-string  f-string还可用于多行字符串：

name = 'Eric'
age = 27

f"Hello!" \
print(f"I'm {name}." \
        ... f"I'm {age}.")

"Hello!I'm Eric.I'm 27."
print(f"""Hello!
...     I'm {name}.
...     I'm {age}.""")
"Hello!\n    I'm Eric.\n    I'm 27."
