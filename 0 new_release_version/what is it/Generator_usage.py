# https://www.php.cn/python-tutorials-361081.html
# https://blog.csdn.net/u011318077/article/details/93749143?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.add_param_isCf&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.add_param_isCf
'''
生成器
利用迭代器，我们可以在每次迭代获取数据（通过next()方法）时按照特定的规律进行生成。
但是我们在实现一个迭代器时，关于当前迭代到的状态需要我们自己记录，进而才能根据当前状态生成下一个数据。
为了达到记录当前状态，并配合next()函数进行迭代使用，我们可以采用更简便的语法，即生成器(generator)。
生成器是一类特殊的迭代器。
创建生成器方法1
要创建一个生成器，有很多种方法。第一种方法很简单，只要把一个列表生成式的 [ ] 改成 ( )

作者：DevOps海洋的渔夫
链接：https://www.jianshu.com/p/6868cb724ba7
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

创建生成器方法2
generator非常强大。如果推算的算法比较复杂，用类似列表生成式的 for 循环无法实现的时候，
还可以用函数来实现。可以用斐波那契数列来举例：
'''

def fib_infinit():  # 无限迭代Fib
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a+b

def fib(n):  # 迭代Fib
    i = 0
    a, b = 1, 1
    while i<n:
        yield a
        a, b = b, a+b
        i += 1 #
for i in fib(10):
    print(i,end=',')


'''
上面的例子来自08年的PyCon一个讲座。gen_words gen_data_from_file是数据生产者，
而count_words count_total_chars是数据的消费者。可以看到，数据只有在需要的时候去拉取的，
而不是提前准备好。另外gen_words中 (w for w in line.split() if w.strip()) 
也是产生了一个generator

使用场景二：　　
一些编程场景中，一件事情可能需要执行一部分逻辑，然后等待一段时间、或者等待某个异步的
结果、或者等待某个状态，然后继续执行另一部分逻辑。比如微服务架构中，服务A执行了一段逻辑之后，去服务B
请求一些数据，然后在服务A上继续执行。或者在游戏编程中，一个技能分成分多段，先执行一部分动作（效果），
然后等待一段时间，然后再继续。对于这种需要等待、而又不希望阻塞的情况，

我们一般使用回调（callback）的方式。下面举一个简单的例子：
'''

def do(a):
    print('do', a)
    #.callback(5, lambda a=a: post_do(a))

'''
这里的CallBackMgr注册了一个5s后的时间，5s之后再调用lambda函数，可见一段逻辑被分裂到两个函数，
而且还需要上下文的传递（如这里的参数a）。我们用yield来修改一下这个例子，yield返回值代表等待的时间。

使用场景二：
一些编程场景中，一件事情可能需要执行一部分逻辑，然后等待一段时间、或者等待某个异步的结果、
或者等待某个状态，然后继续执行另一部分逻辑。比如微服务架构中，服务A执行了一段逻辑之后，
去服务B请求一些数据，然后在服务A上继续执行。或者在游戏编程中，一个技能分成分多段，
先执行一部分动作（效果），然后等待一段时间，然后再继续。对于这种需要等待、
而又不希望阻塞的情况，我们一般使用回调（callback）的方式。下面举一个简单的例子：
'''

@yield_dec
def do(a):
    print ('do', a)
    yield 5
    print ('post_do', a)

def post_do(a):
    print('post_do', a)

#Generator
def gen_generator():
    yield 1

def gen_value():
    return 1

if __name__ == '__main__':
    ret = gen_generator()
    print(ret, type(ret))  # <generator object gen_generator at 0x02645648> <type 'generator'>
    ret = gen_value()
    print(ret, type(ret))  # 1 <type 'int'>

'''
从上面的代码可以看出，gen_generator函数返回的是一个generator实例，generator有以下特别：
遵循迭代器（iterator）协议，迭代器协议需要实现__iter__、next接口
能过多次进入、多次返回，能够暂停函数体中代码的执行面看一下测试代码：
'''
def gen_example():
    print('before any yield')
    yield 'first yield'
    print('between yields')
    yield 'second yield'
    print('no yield anymore')
gen = gen_example()
#gen.next()

from collections.abc import Iterator
class FibIterator(object):
    """斐波那契数列迭代器"""
    def __init__(self, n):
        """
        :param n: int, 指明生成数列的前n个数
        """
        self.n = n
        # current用来保存当前生成到数列中的第几个数了
        self.current = 0
        # num1用来保存前前一个数，初始值为数列中的第一个数0
        self.num1 = 0
        # num2用来保存前一个数，初始值为数列中的第二个数1
        self.num2 = 1

    def next(self):
        """被next()函数调用来获取下一个数"""
        if self.current < self.n:
            num = self.num1
            self.num1, self.num2 = self.num2, self.num1+self.num2
            self.current += 1
            return num
        else:
            raise StopIteration

    def __iter__(self):
        """迭代器的__iter__返回自身即可"""
        return self

'''
if __name__ == '__main__':
    fib = FibIterator(10)
    for num in fib:
        print(num)

    li = list(FibIterator(15))
    print(li)

    tp = tuple(FibIterator(6))
    print(tp)
'''


'''
在使用生成器实现的方式中，我们将原本在迭代器__next__方法中实现的基本逻辑放到一个函数中来实现，但是
将每次迭代返回数值的return或者print换成了yield，此时新定义的函数便不再是函数，而是一个生成器了。

简单来说：只要在def中有yield关键字的 就称为 生成器

此时按照调用函数的方式( 案例中为F = fib(5) )使用生成器就不再是执行函数体了，而是会返回一个生成器对象
（ 案例中为F ），然后就可以按照使用迭代器的方式来使用生成器了。

总结

使用了yield关键字的函数不再是函数，而是生成器。（使用了yield的函数就是生成器）
yield关键字有两点作用：

保存当前运行状态（断点），然后暂停执行，即将生成器（函数）挂起
将yield关键字后面表达式的值作为返回值返回，此时可以理解为起到了return的作用
可以使用next()函数让生成器从断点处继续执行，即唤醒生成器（函数）
Python3中的生成器可以使用return返回最终运行的返回值，而Python2中的生成器不允许使用 return返回一个返回值（即可以使用return从生成器中退出，但return后不能有任何表达式）。
使用send唤醒
我们除了可以使用next()函数来唤醒生成器继续执行外，还可以使用send()函数来唤醒执行。使用send()函数的一个好处是可以在唤醒的同时向断点处传入一个附加数据。

例子：执行到yield时，gen函数作用暂时保存，返回i的值; temp接收下次c.send("python")，send发送过来的值，c.next()等价c.send(None)

使用send()方法示例：

作者：DevOps海洋的渔夫
链接：https://www.jianshu.com/p/6868cb724ba7
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

def gen():
    i = 0
    while i < 5:
        temp = yield i
        print(temp)
    i += 1

f = gen()
next(f)
#0

f.send('haha')
#haha
# 1

f.next()
#None
# 2

#f.send('haha')
#haha
#3

f.next()
#None
# 4
'''
