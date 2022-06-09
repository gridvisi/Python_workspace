'''
Decorators
Decorators are convenient for factoring out common prologue, epilogue, and/or
exception-handling code in similar functions (much like context managers and the
"with" statement), such as:

Acquiring and releasing locks (e.g. a "@with_lock(x)" decorator)
Entering a database transaction (and committing if successful, or rolling back
upon encountering an unhandled exception)
Asserting pre- or post-conditions (e.g. "@returns(int)")
Parsing arguments or enforcing authentication (especially in web application
servers like Pylons where there's a global request and/or cookies object that
might accompany formal parameters to a function)
Instrumentation, timing or logging, e.g. tracing every time a function runs
They are also used as shorthand to define class methods (@classmethod) and
static methods (@staticmethod) in Python classes.

装饰器可以方便地在类似的函数中分解出常见的序幕、尾声和/或异常处理代码
（很像上下文管理器和 "with "语句），例如。

获取和释放锁（例如，"@with_lock(x) "装饰器
进入数据库事务（如果成功则提交，如果遇到未处理的异常则回滚）。
断言前条件或后条件（例如"@returns(int)"）。
解析参数或强制认证（特别是在像Pylons这样的Web应用服务器中，有一个全局
请求和/或cookies对象，可能伴随着函数的正式参数
仪表、计时或记录，例如，每次函数运行时的跟踪。
它们也被用作Python类中定义类方法（@classmethod）和静态方法（@staticmethod）的简写。
'''

def p_decorate(func):
   def func_wrapper(*args, **kwargs):
       return "<p>{0}</p>".format(func(*args, **kwargs))
   return func_wrapper

class Person(object):
    def __init__(self):
        self.name = "John"
        self.family = "Doe"

    @p_decorate
    def get_fullname(self):
        return self.name+" "+self.family

my_person = Person()

print(my_person.get_fullname())

#2
def decorator_func(n):
    def wrapper(*args, **kwargs):
        return 'the head of ouput:',n(*args, **kwargs)
    return wrapper
#print(type(f))
@decorator_func
def hello_world(x):
    return 'Hello World! ' + x
x = 'eric'

print(hello_world(x))
#print(decorator_func(f))

#3
a,b = 2,3
def square(func):
    def wrapper(*args,**kwargs):
        return 'game over',func(*args,**kwargs)
    return wrapper
@square
def add(a,b):
    return a + b

print(add(a,b))


# classic case_study Fabnacci
def memo(fn):
    cache = {}
    miss = object()

    def wrapper(*args):
        result = cache.get(args, miss)
        if result is miss:
            result = fn(*args)
            cache[args] = result
            print(result,cache)
        return result

    return wrapper

@memo
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(7))
print(object())