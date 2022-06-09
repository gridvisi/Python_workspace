# https://brilliant.org/daily-problems/os-make-18/



operators = ["+", "-", "*", "/"]

def calc(n, op):
    global counter
    if n == 4:
        result = "2" + op[0] + "2" + op[1] + "2" + op[2] + "2" + op[3] + "2"
        if eval(result) == 18:
            counter += 1
            print(result)
        return
    else:

        for operator in operators:
            op[n] = operator
            print(op)
            calc(n+1, op)

counter = 0
calc(0, ["", "", "", ""])
print(counter)

from itertools import product
print([p for p in product(('+','-','*','/'), repeat = 4) if eval('2'+'2'.join(p)+'2') == 18])

print(list(eval('2'+'2'.join(p)+'2'+'2') for p in ('+','-','*','/')))
print(list(('2'.join(p)+'2'+'2') for p in ('+','-','*','/')))

print(list('2'.join(p) for p in ('+','-','*','/')))

print('join1:','2'.join('1 2 3 4'))
print('join2:','  '.join('1234'))
print('join3:','  '.join(['1234']))
print('join3:','<'.join(['1','2','3','4']))

p = ['+','-','*','/','+']
print('2'.join(p))
print('2'+'2'.join(p)+'2')
print(eval('2'+'2'.join(p)+'2'))

'''
eval(expression[, globals[, locals]])
expression ： 表达式。
globals ： 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
locals ： 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。

命名空间
python是用命名空间来记录变量的轨迹的，命名空间是一个dictionary，键是变量名，值是变量值。
在一个 Python 程序中的任何一个地方，都存在几个可用的名字空间。每个函数都有着自已的名字空间，
叫做局部名字空间，它记录了函数的变量，包括函数的参数和局部定义的变 量。
每个模块拥有它自已的名字空间，叫做全局名字空间，它记录了模块的变量，包括函数、类、其它导入的模块、
模块级的变量和常量。还有就是内置名字空间， 任何模块均可访问它，它存放着内置的函数和异常。


python的全局名字空间存储在一个叫globals()的dict对象中；局部名字空间存储在一个叫locals()的dict对象中。
可以用print (locals())来查看该函数体内的所有变量名和变量值。

参数查找
当后两个参数都为空时，很好理解，就是一个string类型的算术表达式，计算出结果即可。等价于eval(expression)。
当locals参数为空，globals参数不为空时，先查找globals参数中是否存在变量，并计算。
当两个参数都不为空时，先查找locals参数，再查找globals参数。

1、简单表达式
print(eval('1+2'))
输出结果：3

2、字符串转字典
print(eval("{'name':'linux','age':18}")
输出结果：{'name':'linux','age':18}

3、传递全局变量
print(eval("{'name':'linux','age':age}",{"age":1822}))
输出结果：{'name': 'linux', 'age': 1822}


4、传递本地变量
age=18
print(eval("{'name':'linux','age':age}",{"age":1822},locals()))
输出结果：{'name': 'linux', 'age': 18}

总结
eval虽然方便，但是要注意安全性，可以将字符串转成表达式并执行，就可以利用执行系统命令，删除文件等操作。

'''