'''
https://www.codewars.com/kata/lazy-repeater/train/python
abc = make_looper('abc')
abc() # should return 'a' on this first call
abc() # should return 'b' on this second call
abc() # should return 'c' on this third call
abc() # should return 'a' again on this fourth call
'''

st = 'abc'

from itertools import cycle
def make_looper(s):
    g = cycle(s)
    return lambda: next(g)


from itertools import cycle
class make_looper(cycle):
    def __call__(self):
        return self.__next__()

def make_looper(string):
    def generator():
        while True:
            for char in string:
                yield char
    return generator().next

from itertools import cycle
def make_looper(string):
    return cycle(string).__next__

from itertools import cycle
def make_looper(string):
    c = cycle(string)
    return lambda: next(c)
from itertools import cycle
def make_looper(s):
    class C:
        def __init__(self, s):
            self.s = cycle(s)
        def __call__(self):
            return next(self.s)
    return C(s)

class make_looper: #MakeLooper
    def __init__(self, a):
        from itertools import cycle
        self.a = cycle(a)

    def __call__(self):
        return next(self.a)

from itertools import cycle


def make_looper(string):
    generator = cycle(string)
    return lambda: next(generator)

class make_looper:
  def __init__(self, s):
    self.s = s
  def __call__(self):
    char = self.s[0]
    self.s = self.s[1:] + char
    return char




# eric work code
def make_looper(st):
    it = iter(st)
    return next(it)
make_looper(st)
print('mark:',make_looper(st))
print('mark:',make_looper(st))
print('mark:',make_looper(st))


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= len(st):
            x = self.a
            self.a += 1
            return st[x-1]
        else:
            self.a = 1
make_looper = MyNumbers()
myiter = iter(make_looper)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

print('-'*77)
it = iter(list(st))
print(next(it))
print(next(it))
print(next(it))


class Classmate:
    def __init__(self):
        self.names = []
        self.num = 0

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        return self

    def __next__(self):
        if self.num < len(self.names):
            ret = self.names[self.num]
            self.num += 1
            return ret
        else:
            raise StopIteration

c = Classmate()
c.add("张三")
c.add("李四")
c.add("王五")


#from collections import Iterator,Iterable,Generator