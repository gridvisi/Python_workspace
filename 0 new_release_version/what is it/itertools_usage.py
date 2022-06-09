import time
def timer(func): #timer(test1) func=test1
    def deco(*args,**kwargs):  #非固定参数
        start_time=time.time()
        func(*args,**kwargs) #run test1()
        stop_time = time.time()
        print("the func run time is %s" %(stop_time-start_time))
    return deco
@timer #test1=timer(test1) 把deco的内存地址返回给test1
def test1():
    time.sleep(1)
    print('in the test1')

@timer # test2 = timer(test2) = deco test2(name) =deco(name)
def test2(name,age):
    print("test2:",name,age)

test1() #实际上是在执行deco
test2("alex",22)




from itertools import cycle
from itertools import islice
colors = cycle(['red','black','blue'])
limited = islice(colors,0,4)
for x in limited:
    print(x)

'''
装饰器
器，代表函数的意思

原则：
1 不能修改被装饰的函数的源代码
2 不能修改被装饰的函数的调用方式
实现装饰器知识储备：

1 函数即“变量”
2 高阶函数
a 把一个函数名当做实参传给另一个函数
b 返回值中包含函数名

高阶函数
'''

#高阶函数
#嵌套函数

x = 0
def grandpa():
    x = 1
    print(x)
    def dad():
        x =2
        print(x)
        def son():
            x =3
            print(x)
        son()
    dad()

grandpa()

#高阶函数+嵌套函数 = 装饰器

import time
def timer(func): #timer(test1) func=test1
    def deco(*args,**kwargs):  #非固定参数
        start_time=time.time()
        func(*args,**kwargs) #run test1()
        stop_time = time.time()
        print("the func run time is %s" %(stop_time-start_time))
    return deco
@timer #test1=timer(test1) 把deco的内存地址返回给test1
def test1():
    time.sleep(1)
    print('in the test1')

@timer # test2 = timer(test2) = deco test2(name) =deco(name)
def test2(name,age):
    print("test2:",name,age)

test1() #实际上是在执行deco
test2("alex",22)

'''
类装饰器
没错，装饰器不仅可以是函数，还可以是类，相比函数装饰器，类装饰器具有灵活度大、高内聚、封装性等优点。
使用类装饰器主要依靠类的__call__方法
'''

class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        print ('class decorator runing')
        self._func()
        print ('class decorator ending')

@Foo
def bar():
    print ('bar')
bar()

'''
装饰器可以把与业务逻辑无关的代码抽离出来，让代码保持干净清爽，而且装饰器还能被多个地方重复利用。
比如一个爬虫网页的函数，
如果该 URL 曾经被爬过就直接从缓存中获取，否则爬下来之后加入到缓存，防止后续重复爬取。
'''
import urllib
def web_lookup(url, saved={}):
    if url in saved:
        return saved[url]
    page = urllib.urlopen(url).read()
    saved[url] = page
    return page

#2 pythonic
import urllib.request as urllib  # py3
def cache(func):
    saved = {}

    def wrapper(url):
        if url in saved:
            return saved[url]
        else:
            page = func(url)
            saved[url] = page
            return page

    return wrapper

@cache
def web_lookup(url):
    return urllib.urlopen(url).read()

'''
用装饰器写代码表面上感觉代码量更多，但是它把缓存相关的逻辑抽离出来了，可以给更多的函数调用，
这样总的代码量就会少很多，而且业务方法看起来简洁了。
带参数的decorator
'''
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('execute')
def now():
    print('2015-3-25')

now()
now.__name__

'''
因为返回的那个wrapper()函数名字就是’wrapper’，所以，需要把原始函数的__name__等属性复制到wrapper()
函数中，否则，有些依赖函数签名的代码执行就会出错。

不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个
事的，所以，一个完整的decorator的写法如下：
'''
import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('execute')
def now():
    print('2015-3-25')
now()
now.__name__

# 那么不带参数decorator，也是一样的
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

#实例—登录认证
import functools


user,passwd = 'sun' ,'123'
def auth(auth_type):
    print("auth func:",auth_type)
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            print('wrapper func args:',*args,**kwargs)
            if auth_type == 'local':
                username = input('Username:').strip()
                password = input("Password:").strip()
                if user == username and passwd == password:
                    print("\033[32;1mUser has passed authentication\033[0m")
                    res = func(*args, **kwargs)
                    print("--after authentication--")
                    return res
                else:
                    exit("\033[31;1mInvalid username or password\033[0m")
            elif auth_type == 'ldap':
                res = func(*args, **kwargs)
                print("搞毛线ldap,不会。。。。")
                return res

        return wrapper
    return decorator

def index():
    print("welcome to index page")

@auth(auth_type='local')
def home():
    print("welcome to home page")
    return 'from home'

@auth(auth_type='ldap')
def bbs():
    print("welcome to bbs page")


index()
print(home())  #wrapper
bbs()
