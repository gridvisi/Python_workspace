# Ultimate Guide to Data Classes in Python 3.7
# https://realpython.com/python-data-classes/

'''
Table of Contents

Alternatives to Data Classes
Basic Data Classes
More Flexible Data Classes
Immutable Data Classes
Inheritance
Optimizing Data Classes
Conclusion & Further Reading
'''

from dataclasses import dataclass
@dataclass
class DataClassCard:
    rank: str
    suit: str

queen_of_hearts = DataClassCard('Q', 'Hearts')
print(queen_of_hearts.rank)
#'Q'
print(queen_of_hearts)
DataClassCard(rank='Q', suit='Hearts')
print(queen_of_hearts == DataClassCard('Q', 'Hearts'))
#True

class RegularCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit


queen_of_hearts = RegularCard('Q', 'Hearts')
print(queen_of_hearts.rank)
#'Q'
print(queen_of_hearts)
# __main__.RegularCard object at 0x7fb6eee35d30>
print(queen_of_hearts == RegularCard('Q', 'Hearts'))
#False

class RegularCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'(rank={self.rank!r}, suit={self.suit!r})')

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.rank, self.suit) == (other.rank, other.suit)

'''
Alternatives to Data Classes
For simple data structures, you have probably already used a tuple or a dict.
You could represent the queen of hearts card in either of the following ways:
'''

queen_of_hearts_tuple = ('Q', 'Hearts')
queen_of_hearts_dict = {'rank': 'Q', 'suit': 'Hearts'}

from collections import namedtuple
NamedTupleCard = namedtuple('NamedTupleCard', ['rank', 'suit'])
'''
它是有效的。然而，作为一个程序员，它给你带来了很多责任。

你需要记住Queen_of_hearts_... 变量代表一张牌.
对于_tuple版本，你需要记住属性的顺序。写('黑桃'，'A')会搞乱你的程序，但可能不会给你一个容易理解的错误信息。
如果你使用_dict，你必须确保属性的名称是一致的。例如{'value': 'A', '花色': '黑桃'}将不会像预期的那样工作。
此外，使用这些结构并不理想。
It works. However, it puts a lot of responsibility on you as a programmer:

You need to remember that the queen_of_hearts_... variable represents a card.
For the _tuple version, you need to remember the order of the attributes. Writing ('Spades', 'A') will mess up your program but probably not give you an easily understandable error message.
If you use the _dict, you must make sure the names of the attributes are consistent. For instance {'value': 'A', 'suit': 'Spades'} will not work as expected.
Furthermore, using these structures is not ideal:
'''
print(queen_of_hearts_tuple[0])  # No named access
'Q'
print(queen_of_hearts_dict['suit'])  # Would be nicer with .suit
'Hearts'

'''
一个更好的选择是namedtuple。它早已被用来创建可读的小型数据结构。事实上，我们可以使用这样的
namedtuple重新创建上面的数据类例子。
A better alternative is the namedtuple. It has long been used to create readable s
mall data structures. We can in fact recreate the data class example above using a 
namedtuple like this:
'''
from collections import namedtuple

NamedTupleCard = namedtuple('NamedTupleCard', ['rank', 'suit'])

'''
This definition of NamedTupleCard will give the exact same output as our DataClassCard example did:
'''
queen_of_hearts = NamedTupleCard('Q', 'Hearts')
print(queen_of_hearts.rank)
'Q'
print(queen_of_hearts)
NamedTupleCard(rank='Q', suit='Hearts')
print(queen_of_hearts == NamedTupleCard('Q', 'Hearts'))
'True'

'''
那么，为什么还要用数据类呢？首先，数据类的功能比你目前看到的要多得多。同时，namedtuple还有一些其他的功能不一定是可取的。
从设计上看，namedtuple是一个普通的元组。这一点可以在比较中看出来，比如说。
So why even bother with data classes? First of all, data classes come with many more features 
than you have seen so far. At the same time, the namedtuple has some other features that are 
not necessarily desirable. By design, a namedtuple is a regular tuple. 
This can be seen in comparisons, for instance:
'''
print(queen_of_hearts == ('Q', 'Hearts'))
'True'

# While this might seem like a good thing, this lack of awareness about its own type can lead to subtle and hard-to-find bugs, especially since it will also happily compare two different namedtuple classes:
# 虽然这看起来似乎是件好事，但这种对自身类型缺乏认识的情况可能会导致微妙而难以发现的错误，尤其是它还会很乐意比较两个不同的 namedtuple 类。
Person = namedtuple('Person', ['first_initial', 'last_name'])
ace_of_spades = NamedTupleCard('A', 'Spades')
ace_of_spades == Person('A', 'Spades')
'True'

#The namedtuple also comes with some restrictions. For instance, it is hard to add default values to some of the fields in a namedtuple. A namedtuple is also by nature immutable. That is, the value of a namedtuple can never change. In some applications, this is an awesome feature, but in other settings, it would be nice to have more flexibility:
# namedtuple也有一些限制。例如，很难给命名tuple中的一些字段添加默认值。命名tuple在本质上也是不可改变的。也就是说，namedtuple的值永远不会改变。在某些应用程序中，这是一个很棒的功能，但在其他设置中，如果能有更多的灵活性就更好了。
card = NamedTupleCard('7', 'Diamonds')
card.rank = '9'
#AttributeError: can't set attribute

#Data classes will not replace all uses of namedtuple. For instance, if you need your data structure to behave like a tuple, then a named tuple is a great alternative!
'''
数据类不会取代namedtuple的所有用途。例如，如果你需要你的数据结构表现得像一个元组，那么命名元组就是一个很好的替代方案！
数据类的另一个替代方案是attrs项目，它是数据类的灵感之一。

另一种选择，也是数据类的灵感来源之一，是attrs项目。安装了attrs后（pip install attrs），
你可以写一个卡片类，如下所示。
Another alternative, and one of the inspirations for data classes, is the attrs project. With attrs installed (pip install attrs), you can write a card class as follows:
'''

import attr

@attr.s
class AttrsCard:
    rank = attr.ib()
    suit = attr.ib()

'''
这可以和前面的DataClassCard和NamedTupleCard例子的使用方法完全一样。attrs项目非常棒，它确实支持一些数据类
不支持的功能，包括转换器和验证器。此外，attrs已经存在了一段时间，并且在Python 2.7以及Python 3.4以上的版本中
都有支持。然而，由于attrs不是标准库的一部分，它确实为你的项目增加了一个外部依赖。通过数据类，类似的功能将随处可见。

除了 tuple、dict、namedtuple 和 attrs，还有许多其他类似的项目，包括 typing.NamedTuple、namedlist、attrdict、plumber 和 fields。虽然数据类是一个很好的新选择，但仍有一些用例，其中一个旧的变体更适合。例如，如果你需要与期待元组的特定API兼容，或者需要数据类不支持的功能。
This can be used in exactly the same way as the DataClassCard and NamedTupleCard examples earlier. 
The attrs project is great and does support some features that data classes do not, including 
converters and validators. Furthermore, attrs has been around for a while and is supported in 
Python 2.7 as well as Python 3.4 and up. However, as attrs is not a part of the standard library, 
it does add an external dependency to your projects. Through data classes, similar functionality 
will be available everywhere.

In addition to tuple, dict, namedtuple, and attrs, there are many other similar projects, including typing.NamedTuple, namedlist, attrdict, plumber, and fields. While data classes are a great new alternative, there are still use cases where one of the older variants fits better. For instance, if you need compatibility with a specific API expecting tuples or need functionality not supported in data classes.
'''

'''
基本数据类
让我们回到数据类。举个例子，我们将创建一个Position类，用名字以及经纬度来表示地理位置。
Basic Data Classes
Let us get back to data classes. As an example, we will create a Position class that will represent geographic positions with a name as well as the latitude and longitude:
'''
from dataclasses import dataclass

@dataclass
class Position:
    name: str
    lon: float
    lat: float

'''
是什么让它成为一个数据类呢，就是类定义上方的@dataclass装饰符。在类的Position:行下面，
你只需在数据类中列出你想要的字段。字段使用的 : 符号是使用了 Python 3.6 中的一个新特性，
叫做变量注解。我们很快就会详细讨论这个符号，以及为什么我们要指定 str 和 float 这样的数据类型。

这几行代码就是你所需要的。新类已经可以使用了。
What makes this a data class is the @dataclass decorator just above the class definition.
 Beneath the class Position: line, you simply list the fields you want in your data class. 
 The : notation used for the fields is using a new feature in Python 3.6 called 
 variable annotations. 
 We will soon talk more about this notation and why we specify data types like str and float.

Those few lines of code are all you need. The new class is ready for use:
'''

pos = Position('Oslo', 10.8, 59.9)
print(pos)
Position(name='Oslo', lon=10.8, lat=59.9)
print(pos.lat)
'59.9'
print(f'{pos.name} is at {pos.lat}°N, {pos.lon}°E')
'Oslo is at 59.9°N, 10.8°E'

'''
您也可以创建数据类，类似于创建命名元组的方式。下面的内容（几乎）等同于上面的Position的定义。
You can also create data classes similarly to how named tuples are created. 
The following is (almost) equivalent to the definition of Position above:
'''

#方法不能单独使用，而是要配合对象来使用。

from dataclasses import make_dataclass
Position = make_dataclass('Position', ['name', 'lat', 'lon'])

'''
A data class is a regular Python class. The only thing that sets it apart is that it has basic data model methods like .__init__(), .__repr__(), and .__eq__() implemented for you.

Default Values
It is easy to add default values to the fields of your data class:
'''
# https://realpython.com/python-data-classes/#basic-data-classes

from dataclasses import dataclass

@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0

print(Position('Null Island'))
Position(name='Null Island', lon=0.0, lat=0.0)
Position('Greenwich', lat=51.8)
Position(name='Greenwich', lon=0.0, lat=51.8)
Position('Vancouver', -123.1, 49.3)
Position(name='Vancouver', lon=-123.1, lat=49.3)

'''
稍后你将学习default_factory，它提供了一种提供更复杂的默认值的方法。

类型提示
到目前为止，我们并没有大惊小怪，数据类支持开箱即用的类型。你可能已经注意到，
我们在定义字段的时候有一个类型提示：name: str表示name应该是一个文本字符串（str类型）。

事实上，在定义数据类中的字段时，添加某种类型提示是必须的。如果没有类型提示，该字段将不会成为数据类的一部分。但是，如果你不想在你的数据类中添加显式类型，可以使用 typing.Any。
Later you will learn about default_factory, which gives a way to provide more complicated default values.

Type Hints
So far, we have not made a big fuss of the fact that data classes support typing out of the box. 
You have probably noticed that we defined the fields with a type hint: name: str says that name 
should be a text string (str type).

In fact, adding some kind of type hint is mandatory when defining the fields in your data class. 
Without a type hint, the field will not be a part of the data class. However, 
if you do not want to add explicit types to your data class, use typing.Any:
'''
from dataclasses import dataclass
from typing import Any

@dataclass
class WithoutExplicitTypes:
    name: Any
    value: Any = 42

'''
虽然在使用数据类时，你需要以某种形式添加类型提示，但这些类型在运行时并不强制执行。下面的代码在运行时没有任何问题。
While you need to add type hints in some form when using data classes, 
these types are not enforced at runtime. The following code runs without any problems:
'''
Position(3.14, 'pi day', 2018)
Position(name=3.14, lon='pi day', lat=2018)

'''
这就是Python中的类型化通常是如何工作的。Python 是而且将永远是一种动态类型化的语言。为了实际捕获类型错误，
可以在源代码上运行 Mypy 这样的类型检查器。

This is how typing in Python usually works: Python is and will always be a dynamically 
typed language. To actually catch type errors, type checkers like Mypy can be run on your 
source code.
'''


'''
结论和进一步阅读
数据类是 Python 3.7 的新特性之一。有了数据类，您不必编写模板代码来为您的对象获得正确的初始化、表示和比较。

你已经看到了如何定义自己的数据类，以及。

如何为数据类中的字段添加默认值。
如何自定义数据类对象的排序？
如何使用不可变的数据类
数据类的继承是如何工作的
如果你想深入了解数据类的所有细节，可以看看PEP 557以及GitHub原始回帖中的讨论。

此外，Raymond Hettinger的PyCon 2018演讲Dataclasses。结束所有代码生成器的代码生成器非常值得一看。

如果你还没有Python 3.7，还有一个针对Python 3.6的数据类回传。现在，去少写点代码吧!

🐍 Python 技巧 💌
'''