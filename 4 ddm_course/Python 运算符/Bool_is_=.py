
name1 = 'ada'
name2 = 'ada'

print(name1 == name2)
print(name1 is name2)

a = 500
b = 500
print(a == b)
print(a is b)

#1. == 是比较两个对象的内容是否相等，即两个对象的“值“”是否相等，不管两者在内存中的引用地址是否一样。
#1.地址一样，值也一样。所以 == 成立。
st1 = 'aaaaa'
st2 = 'bbbbb'
st3 = 'bbbbb'
st4 = st3
print(st1 == st2, st2 == st3, st3 == st4)  # False True True
print(id(st2) == id(st3), st2 == st3)  # True True

#2.引用地址不一样，但是只要值一样即可 == 成立。
val1 = 2000
val2 = 2001
val3 = val1 + 1
print(id(val3) == id(val2), val3 == val2)
#False
#True

#3.对于类的实例比较

class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print("can run")

stu1 = Student("tom", 19)
stu2 = Student("tom", 19)
stu3 = stu2
print(id(stu1) == id(stu2), stu1 == stu2)  # False False
# 注意这里stu1和stu2的值是不等的，虽然初始化创建对象格式一样。
print(id(stu2) == id(stu3), stu2 == stu3)  # True True

#2. is 比较的是两个实例对象是不是完全相同，它们是不是同一个对象，占用的内存地址是否相同。即is比较两个条件：
# 1.内容相同。2.内存中地址相同
#1.is成立的前提要是内容相同，内存中地址相同
st1 = 'aaaaa'
st2 = 'bbbbb'
st3 = 'bbbbb'
st4 = st3
print(st1 is st2, st2 is st3, st3 is st4)  # False True True
print(id(st1), id(st2), id(st3), id(st4))
# 2439382008080 2439382008192 2439382008192 2439382008192

#2.光值相同不同，内存地址也要相同，才会成立。
a = 1
a = 1000
b = 1000
print(id(a), id(b))
#2625727620144
#2625727619248
print(a is b)
#False
print(a == b)
#True


#3.类实例的比较，也要内存地址一致。

class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print("can run")


stu1 = Student("tom", 19)
stu2 = Student("tom", 19)
stu3 = stu2
print(id(stu1), id(stu2), id(stu3))
print(stu1 is stu2, stu2 is stu3)
print("== == == == == == == == == == == == == == == == == == == == =")

#使用is注意python对于小整数使用对象池存储问题
#1.举个例子，在python命令行模式下：为什么同样值a, b与c, d的结果却不一样呢？
a = 1000
b = 1000
print(a is b)
#False
c = 10
d = 10
print(c is d)
#True

#注意，因为python对小整数在内存中直接创建了一份，不会回收，所有创建的小整数变量直接从对象池中引用他即可。
#但是注意Python仅仅对比较小的整数对象进行缓存（范围为范围[-5, 256]）缓存起来，而并非是所有整数对象。
#也就说只有在这个[-5, 256]范围内创建的变量值使用is比较时候才会成立。

e, d, f, g = -5, -5, -6, -6
print(e is d) #True
print(f is g)  # 超过-5的范围不成立
#False

#注意：注意：上面对于python小整数对象池的使用仅仅是在命令行中执行可以，而在Pycharm或者保存为文件执行，结果是不一样的，这是
# 因为解释器做了一部分优化。下面使用pycharm, 即使整数超过256，使用is也是成立的。


#4.使用is注意python关于字符串的intern机制存储注意python中创建两个内容一样的变量时（变量名不一样），一般都会在内存中
# 分配两个内存地址分别给这两个变量。即两个变量的内容虽然样，但是变量的引用地址不一样。所以两个变量使用 == 比较成立，但是使用
#is比较不成立。

#但是在python中有两个意外情况：1.
#使用python命令行时对于小整数[-5, 256]
#区间内的整数, python会创建小整数对象池，这些对象一旦创建，就不会回收，所有新创建的在这个范围的整数都是直接引用他即可。所以造成在[-5, 256]
#区间内的整数不同变量只要值相同，引用地址也相同。此范围外的整数同样遵循新建一个变量赋予一个地址。

#2.python中虽然字符串对象也是不可变对象, 但python有个intern机制，简单说就是维护一个字典，这个字典维护已经创建字符串(key)
#和它的字符串对象的地址(value), 每次创建字符串对象都会和这个字典比较, 没有就创建，重复了就用指针进行引用就可以了。相当于python对于字符串也是采用了对象池原理。(但是注意
#如果字符串（含有空格），不可修改，没开启intern机制，不共用对象。比如"a b"和"a b", 这种情况使用is不成立的形式 只有在命令行中可以。使用pycharm同样是True，因为做了优化)
a = 'abc'  # 没有空格内容一样的两个变量，在命令行模式下is 结果True
b = 'abc'
print(a == b) #True
print(a is b) #True

c = 'a b '  # 有空格内容一样的两个变量，在命令行模式下is 结果false
d = 'a b '
print(c == d) #True
print(c is d)
#False

#总结：所以在python中如果创建了多个变量(不同变量名，此外不是通过变量引用方式创建的变量)，那么这些变量的引用地址都是不一样的。那么这些变量之间使用is
#去比较的话，就是False的结果。但是除了小整数和字符串除外。如果是通过引用的方式创建的变量的话，那么可以参考
#变量引用在内存中的复制存储原理博客：python变量的引用以及在底层存储原理

ls = [1, 2, 3]  ###值虽然一样，但是两个变量，内存中分配了两个地址。
ls1 = [1, 2, 3]
print(ls == ls1)
#True
print(ls is ls1)
#False

t1 = (1, 2, 3)  ##值虽然一样，但是两个变量，内存中分配了两个地址。
t2 = (1, 2, 3)
print(t1 == t2)
#True
print(t1 is t2)
#False

d1 = {"1": 2, "3":4}  ##值虽然一样，但是两个变量，内存中分配了两个地址。
d2 = {"1": 2, "3":4}
print(d1 == d2)
#True

print(d1 is d2) #False
print(id(d1), id(d2))


st1 = 'abc'  # 注意这里st1 和st2,值一样，内存地址也一样。因为字符串的intern机制。
st2 = 'abc'
print(st1 == st2)
#True

print(st1 is st2)
#True

f1 = 3.14  # 值虽然一样，但是两个变量，内存中分配了两个地址。
f2 = 3.14
print(f1 == f2)
#True

print(f1 is f2)
#False

a = 1000  # 超出[-5,256]范围值虽然一样，但是两个变量，内存中分配了两个地址。
b = 1000
print(a is b, a == b)
#(False, True)

a = 1  # 值在小整数对象池范围内，所以值一样，内存地址一样。
b = 1
print(a is b, a == b)
#(True, True)

#5.python中对于None值的比较：使用is
a = ""
print(a is None)
#False

print(b == "aa")
print(b is None)
#False
print(b is not None)
#True

#统一声明：关于原创博客内容，可能会有部分内容参考自互联网，如有原创链接会声明引用；
# 如找不到原创链接，在此声明如有侵权请联系删除哈。关于转载博客，如有原创链接会声明；如
# 找不到原创链接，在此声明如有侵权请联系删除哈。