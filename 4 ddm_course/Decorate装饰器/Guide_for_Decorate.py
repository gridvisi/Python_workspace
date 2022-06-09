#https://www.jb51.net/article/168276.htm

# 这是装饰函数
def logger(func):
    def wrapper(*args, **kw):
        print('我准备开始计算：{} 函数了:'.format(func.__name__))

        # 真正执行的是这行。
        func(*args, **kw)

        print('啊哈，我计算完啦。给自己加个鸡腿！！')

    return wrapper
@logger
def add(x, y):
    print('{} + {} = {}'.format(x, y, x+y))
print(add(13,17))
'''
03. 入门用法：时间计时器
再来看看 时间计时器
实现功能：顾名思义，就是计算一个函数的执行时长。
'''
# 这是装饰函数
def timer(func):
    def wrapper(*args, **kw):
        t1 = time.time()
        # 这是函数真正执行的地方
        func(*args, **kw)
        t2 = time.time()

        # 计算下时长
        cost_time = t2 - t1
        print("花费时间：{}秒".format(cost_time))
    return wrapper

#假如，我们的函数是要睡眠10秒。这样也能更好的看出这个计算时长到底靠不靠谱。
import time
@timer
def want_sleep(sleep_time):
    time.sleep(sleep_time)
print(want_sleep(1))


def american():
    print("I am from America.")

def chinese():
    print("我来自中国。")

def say_hello(contry):
    def wrapper(func):
        def deco(*args, **kwargs):
            if contry == "china":
                print("你好!")
            elif contry == "america":
                print('hello.')
            else:
                return

            # 真正执行函数的地方
            func(*args, **kwargs)

        return deco

    return wrapper


@say_hello("china")
def chinese():
    print("我来自中国。")

@say_hello("america")
def american():
    print("I am from America.")
print(american(),chinese())