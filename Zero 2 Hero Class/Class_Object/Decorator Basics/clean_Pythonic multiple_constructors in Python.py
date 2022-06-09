'''
https://stackoverflow.com/questions/682504/what-is-a-clean-pythonic-way-to-have-multiple-constructors-in-python
'''

'''
Suppose I have a class called Cheese with the number_of_holes property. 
How can I have two ways of creating cheese objects...

One that takes a number of holes like this: parmesan = Cheese(num_holes = 15)
And one that takes no arguments and just randomizes the number_of_holes property: 
gouda = Cheese()
I can think of only one way to do this, but this seems clunky:
'''

class Cheese():
    def __init__(self, num_holes = 0):
        if (num_holes == 0):
            #Randomize number_of_holes
        else:
            number_of_holes = num_holes

class Cheese():
    def __init__(self, *args, **kwargs):
        #args -- tuple of anonymous arguments
        #kwargs -- dictionary of named arguments
        self.num_holes = kwargs.get('num_holes',random_holes())


import random
class Cheese(object):
    def __init__(self, num_holes=0):
        "defaults to a solid cheese"
        self.number_of_holes = num_holes

    @classmethod
    def random(cls):
        return cls(randint(0, 100))

    @classmethod
    def slightly_holey(cls):
        return cls(randint(0, 33))

    @classmethod
    def very_holey(cls):
        return cls(randint(66, 100))

gouda = Cheese()
emmentaler = Cheese.random()
leerdammer = Cheese.slightly_holey()


# super
from functools import singledispatchmethod as overload
# or the following more flexible method after `pip install multimethod`
# from multimethod import multidispatch as overload


class MyClass:

    @overload  # type: ignore[misc]
    def __init__(self, a: int = 0, b: str = 'default'):
        self.a = a
        self.b = b

    @__init__.register
    def _from_str(self, b: str, a: int = 0):
        self.__init__(a, b)  # type: ignore[misc]

    def __repr__(self) -> str:
        return f"({self.a}, {self.b})"


print([
    MyClass(1, "test"),
    MyClass("test", 1),
    MyClass("test"),
    MyClass(1, b="test"),
    MyClass("test", a=1),
    MyClass("test"),
    MyClass(1),
    # MyClass(),  # `multidispatch` version handles these 3, too.
    # MyClass(a=1, b="test"),
    # MyClass(b="test", a=1),
])