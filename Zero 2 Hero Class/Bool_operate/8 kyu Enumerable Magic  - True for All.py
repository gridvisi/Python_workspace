


#1st # all函数命名已经与python内置函数重名！！！
def all(seq, fun):
    return next((False for x in seq if not fun(x)), True)
fun = lambda x:x < 6
print(next((False for x in (1, 2, 3, 4, 5) if not fun(x)),True))

def all(seq, fun):
    return not False in list(map(fun, seq))

def all(seq, fun):
    for item in seq:
        if not fun(item):
            return False
    return True

all0=all
def all(seq, fun):
    return all0(fun(s) for s in seq)


from builtins import all as all_
def all(seq, fun):
    return all_(map(fun, seq))


all=lambda l,f,_=all:_(map(f,l))


def all(seq, func, _all=all):
    return _all(func(item) for item in seq)