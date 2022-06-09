class Base:
    def __init__(self, arg1="argument one"):
        self.arg1 = arg1


class Derived(Base):
    pass


b = Base()
print(b.arg1)


d = Derived()
print(d.arg1)


e = Derived("argument changed!")
print(e.arg1 )

#2
class Foo:
    def __init__(self,a, b, c):
        self.a = a
        self.b = b
        self.c = c

#3
class my_class(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def f2(self):
        return self.x + self.y


a = my_class(10, 20)
print(a.f2())

#4
