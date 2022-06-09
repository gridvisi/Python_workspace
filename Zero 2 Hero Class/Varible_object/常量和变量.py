# 每天做饭是谁？
# 常量，值是妈妈
# 每天做饭的人心情如何？
# 变量

son_age = 11
father_age = 44


# 多少年后，父亲是儿子年龄的两倍
# 32
year = 0  # 2022年

father_age += 1
print('step-1:',father_age)

father_age = father_age + 1
print('2:',father_age)

son_age = 11
father_age = 54
for i in range(50):
    print(i)
    father_age += 1
    son_age += 1
    if father_age == son_age * 2: #条件判断
        print('father_age,son_age:',father_age,son_age,i)
else:
    print('不存在这样的可能')



print()


zhyu = 10
xing = 10

print('zhyu = 10:',type(zhyu))
zhyu = '周宏宇'
print('zhyu = 周宏宇:',type(zhyu))
zhyu = ['周宏宇']
print('zhyu = [周宏宇]:',type(zhyu))

zhyu = {'name':'周宏宇','age':11,'game':"minecraft",'gender':'boy',}
#key ,value: 键值，值

zhyu['age'] = 10
print(zhyu,'leixing:',type(zhyu))
#Integer 字符串 list
print(id(xing),id(zhyu))

wjzz_key = ['name','grade','gender','favorite']
wjzz_value = ['王君梓竹','k6','female','unknow']
wjzz_dict = dict(zip(wjzz_key,wjzz_value))
print(wjzz_dict)
print(zip(wjzz_key,wjzz_value))

call_no = {'114':'inquiry','110':'police'}
print(call_no.get('111','unkown'))
#print(call_no['111'])


x = 2 * 2
y = 16 ** 0.5
print(x == y)
print(id(x),id(y))


ada, henry = 10, 9
ada,henry = henry,ada
print('the first solution:',ada,henry)
print(id(ada),id(henry))

ada, henrys = 10, 9
temp = ada #
ada = henry
henry = ada
print('second solution:',ada,henry)
print(id(ada),id(henry))

employeenumber = 4398

EmployeeNumber = 4398

employeeNumber = 4398
print(id(employeeNumber),id(EmployeeNumber),id(employeenumber))

home_address = 1
route66 = 2
#ver1.3 = 3
wangzizhu = [6,31]
wangzizhu.append('girl')
#return = 4
#4square = 5
#w-z-zh = 10

name = "王君梓竹"
print(id(name))

name = 'mama' #string 类型
name = 'baba' # 'lili", 1,

name = 50
name = ['mama',50]


'''

使用is注意python关于字符串的intern机制存储 
    注意python中创建两个内容一样的变量时（变量名不一样）
一般都会在内存中分配两个内存地址分别给这两个变量。即两个变量的内容
虽然样，但是变量的引用地址不一样。所以两个变量使用==比较成立，
但是使用 is比较不成立。

但是在python中有两个意外情况：
1.使用python命令行时对于小整数[-5,256]区间内的整数,
python会创建小整数对象池，这些对象一旦创建，就不会回收，
所有新创建的在这个范围的整数都是直接引用他即可。所以造成在
[-5,256]区间内的整数不同变量只要值相同，引用地址也相同。
此范围外的整数同样遵循新建一个变量赋予一个地址。

2.python中虽然字符串对象也是不可变对象,但python有个intern机制，
简单说就是维护一个字典，这个字典维护已经创建字符串(key)和它的字符
串对象的地址(value),每次创建字符串对象都会和这个字典比较,没有就创
建，重复了就用指针进行引用就可以了。相当于python对于字符串也是采用
了对象池原理。(但是注意：如果字符串（含有空格），不可修改，没开启
intern机制，不共用对象。比如"a b"和"a b",这种情况使用is不成立的形式
只有在命令行中可以。使用pycharm同样是True，因为做了优化)


'''

'''
Python课有5个同学，名字和年龄分别是：ada，alex，henry，zhou，xing，
和 9，9，10，8，9

Step 1：可否以英文名作为变量名？
	    9ada可以作为变量名吗，alex9.2呢？
	    新来的一个同学的英文名可以从下列名单里选，哪些是合乎规		    则的变量名字？

备选项：range，while，eric，
'''
x, y = 257,257
print(x is y)
print(x == y)
# Pycharm 里做了优化，超过256还是True

#from sys import intern
a = 'hello world'
b = 'hello world'

print(a is b)
#False

print(id(a))
#1603648396784

print(id(b))
# 1603648426160

from sys import intern
a = 'hello world'
b = 'hello world'
a = intern(a)
b = intern(b)
print(a is b)
#True

print(id(a))
#1603648396784

print(id(b))
#1603648396784


#is 和 == 的比较输出结果
a = 256
b = 256
print(a is b)
#True

print(id(a))
#1638894624

print(id(b))
#1638894624

a = 257
b = 257
print(a is b)
#False

print(id(a))
#2570926051952

print(id(b))
#2570926051984

# 哪些数字恰好能是整数的平方得到？

import math
num = [16,9,144,56,72]
print(int(1.6),round(1.6),round(1.4))

s = 1.9
print(s == int(s))

'''
XOR (for integers)
x = x ^ y
y = y ^ x
x = x ^ y
Or concisely,

x ^= y
y ^= x
x ^= y
Temporary variable
w = x
x = y
y = w
del w
Tuple swap
x, y = y, x
'''
x,y = 0,1
x = x ^ y
y = y ^ x
x = x ^ y

print("x,y = ",x,y)


from copy import copy

def swapper(x, y):
  return (copy(y), copy(x))


swapper = lambda x, y: (copy(y), copy(x))
x, y = swapper(y, x)
