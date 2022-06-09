__author__ = 'Administrator'


#dict()
#以键对方式构造字典
d1 = dict(one = 1, two = 2, a = 3)
print(d1)

#以映射函数方式来构造字典
d2 = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
print(d2)


def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate

@static_vars(counter = 0)
def foo():
    foo.counter += 1

dicts = [
    {'name': 'Michelangelo',
     'food': 'PIZZA'},
    {'name': 'Garfield',
     'food': 'lasanga'},
    {'name': 'Walter',
     'food': 'pancakes'},
    {'name': 'Galactus',
     'food': 'worlds'}
]
dict1 = {'Tom', 'Jerry', 'Peter'}
print(static_vars(**d2))