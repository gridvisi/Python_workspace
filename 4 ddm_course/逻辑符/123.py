
'''
1 and 2 and 3 返回3
1 and 2 and '' 返回''
'' and 2 and 0 返回''

1 or '' or 0 返回1
'' or 0 or [] 返回[]
'''

def func(a, b, c):
    print(vars())

func(1, 2, 3)  # {"a":1,"b":2,"c":3}

import functools

def add(a, b):
    return a + b
print(add(4, 2))  # 6

plus3 = functools.partial(add, 3)
print(plus3(1))  # 4