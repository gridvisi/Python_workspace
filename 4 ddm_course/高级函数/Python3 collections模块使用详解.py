
from collections import *

cnt = Counter()
print(cnt)
wordList = ["a","b","c","c","a","a"]
for word in wordList:
    cnt[word] += 1
print(cnt)

c = Counter("gallahad")
print(c)

print(Counter({'red': 4, 'blue': 2}))
d = Counter(cats = 4,dogs = 8)  #从args初始化counter
print(d)
print(Counter({'dogs': 8, 'cats': 4}))

e = Counter(['eggs','ham'])
print(e)

print(Counter('abracadabra').most_common(3))
print(Counter('abracadabra').most_common(3))

f = Counter({'a': 5, 'b': 4, 'd': 2, 'c': -3})
print(f.values())

#使用deque维护一个序列（右侧添加元素，左侧删除元素）中窗口的平均值；
from collections import deque
import itertools

def moving_average(iterable,n = 3):
    it = iter(iterable)
    d = deque(itertools.islice(it,n-1))
    # 第一次只有两个元素，再右移的过程中，需要先删除最左端的元素，因此现在最左端加入0
    d.appendleft(0)
    s = sum(d)
    for ele in it:
        # 删除最左端的元素，再加上新元素
        s += ele - d.popleft()
        # 右端添加新元素
        d.append(ele)
        yield s / float(n)

array = [40,30,50,46,39,44]
for ele in moving_average(array,n=3):
    print (ele)

#rotate()方法提供了一种实现deque切片和删除的方式，例如，del d[n]依赖于rotate方法的纯Python实现，如下，
from collections import deque

def delete_nth(d,n):
    # 将前n个元素翻转到右侧
    d.rotate(-n)
    # 删除第n个元素
    d.popleft()
    # 再将后n个元素翻转到左侧
    d.rotate(n)

d = deque("abcdefg")
delete_nth(d,n = 3)
print (d)

#slice依赖于rotate方法的纯Python实现，如下，
from collections import deque

def slice(d,m,n):
    # 先将前面m个元素翻转到右侧
    d.rotate(-m)
    i = m
    sliceList = []
    # 依次将[m,n]区间内的元素出栈
    while i < n:
        item = d.popleft()
        sliceList.append(item)
        i+=1
    # 再将出栈的元素扩展到deque右侧
    d.extend(sliceList)
    # 再将后面n个元素翻转到左侧
    d.rotate(n)
    return sliceList

d = deque("abcdefg")
print(slice(d,1,5))

'''
defaultdict
defaultdict是内置数据类型dict的一个子类，基本功能与dict一样，只是重写了一个方法missing(key)
和增加了一个可写的对象变量default_factory。

missing(key)

如果default_factory属性为None，就报出以key作为遍历的KeyError异常；
如果default_factory不为None，就会向给定的key提供一个默认值，这个值插入到词典中，并返回；
如果调用default_factory报出异常，这个异常在传播时不会改变；
这个方法是当要求的key不存在时，dict类中的getitem()方法所调用，无论它返回或者报出什么，最终返回或报出给getitem()；
只有getitem()才能调用missing()，这意味着，如果get()起作用，如普通的词典，将会返回None作为默认值，而不是使用default_factory；
default_factory， 这个属性用于missing()方法，使用构造器中的第一个参数初始化；

使用list作为default_factory，很容易将一个key-value的序列转换为一个关于list的词典；

'''
from collections import *
s = [('yellow',1),('blue',2),('yellow',3),('blue',4),('red',5)]
d = defaultdict(list)
print(d)
for k,v in s:
    d[k].append(v)
print(d.items())
#[('blue', [2, 4]), ('red', [5]), ('yellow', [1, 3])]

'''
当每一个key第一次遇到时，还没有准备映射，首先会使用default_factory函数自动创建一个空的list，
list.append()操作将value添加至新的list中，当key再次遇到时，通过查表，返回对应这个key的list，
list.append()会将新的value添加至list，这个技术要比dict.setdefault()要简单和快速。

'''
e = {}
for k,v in s:
    e.setdefault(k,[]).append(v)
print('e:',e.items())
#[('blue', [2, 4]), ('red', [5]), ('yellow', [1, 3])]
#设置default_factory为int，使得defaultdict可以用于计数，
s = "mississippi"
d = defaultdict(int)
for k in s:
    d[k]+=1
print(d.items())
#[('i', 4), ('p', 2), ('s', 4), ('m', 1)]

'''
当一个字母第一次遇到，默认从default_factory中调用int()用于提供一个默认为0的计数，递增操作会增加每个
字母的计数。
函数int()经常返回0，是常量函数的一种特例。一种更快和更灵活的创建常量函数的方式是使用itertools.repeat()，
可以提供任意常量值（不仅仅是0）

'''
import itertools
value = [1,2,3,4,5]
def constant_factory(value):
    return itertools.repeat(value).next

d = defaultdict(constant_factory('<missing>'))
d.update(name = "John",action = "ran")
s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue',4)]
d = defaultdict(set)
for k,v in s:
    d[k].add(v)
    d.items()
#[('blue', set([2, 4])), ('red', set([1, 3]))]
'''
OrderedDict
OrderedDict类似于正常的词典，只是它记住了元素插入的顺序，当在有序的词典上迭代时，返回的元素就是它们第一次
添加的顺序。
class collections.OrderedDict，返回已给dict的子类，支持常规的dict的方法，OrderedDict是一个记住元素
首次插入顺序的词典，如果一个元素重写已经存在的元素，那么原始的插入位置保持不变，如果删除一个元素再重新插入，
那么它就在末尾。
OrderedDict.popitem(last=True)，popitem方法返回和删除一个(key,value)对，如果last=True，就以LIFO
方式执行，否则以FIFO方式执行。
OrderedDict也支持反向迭代，例如reversed()。
OrderedDict对象之间的相等测试，例如，list(od1.items()) == list(od2.items())，是对顺序敏感的；
OrderedDict和其他的映射对象（例如常规的词典）之间的相等测试是顺序不敏感的，这就允许OrderedDict对象可以在
使用常规词典的地方替换掉常规词典。
OrderedDict构造器和update()方法可以接受关键字变量，但是它们丢失了顺序，因为Python的函数调用机制是将一个
无序的词典传入关键字变量。
一个有序的词典记住它的成员插入的顺序，可以使用排序函数，将其变为排序的词典，
'''
d = {"banana":3,"apple":2,"pear":1,"orange":4}
# dict sorted by key

OrderedDict(sorted(d.items(),key = lambda t:t[0]))
#OrderedDict([('apple', 2), ('banana', 3), ('orange', 4), ('pear', 1)])

# dict sorted by value
print(OrderedDict(sorted(d.items(),key = lambda t:t[1])))
#OrderedDict([('pear', 1), ('apple', 2), ('banana', 3), ('orange', 4)])
# dict sorted by length of key string

a =  OrderedDict(sorted(d.items(),key = lambda t:len(t[0])))
print(a)
#OrderedDict([('pear', 1), ('apple', 2), ('orange', 4), ('banana', 3)])

del a['apple']
print(a)
#OrderedDict([('pear', 1), ('orange', 4), ('banana', 3)])

a["apple"] = 2
print(a)
#OrderedDict([('pear', 1), ('orange', 4), ('banana', 3), ('apple', 2)])

class LastUpdatedOrderedDict(OrderedDict):
    def __setitem__(self,key,value):
        if key in self:
            del self[key]
        OrderedDict.__setitem__(self, key, value)

obj = LastUpdatedOrderedDict()
obj["apple"] = 2
obj["windows"] = 3
print(obj)

LastUpdatedOrderedDict([('apple', 2), ('windows', 3)])
obj["apple"] = 1
print(obj)
LastUpdatedOrderedDict([('windows', 3), ('apple', 1)])

#一个有序的词典可以和Counter类一起使用，counter对象就可以记住元素首次出现的顺序；

class OrderedCounter(Counter,OrderedDict):
    def __repr__(self):
        return "%s(%r)"%(self.__class__.__name__,OrderedDict(self))

    def __reduce__(self):
        return self.__class__,(OrderedDict(self))

#和OrderDict一起使用的Counter对象
obj = OrderedCounter()
wordList = ["b","a","c","a","c","a"]
for word in wordList:
    obj[word] += 1
print (obj)

# 普通的Counter对象
cnt = Counter()
wordList = ["b","a","c","a","c","a"]
for word in wordList:
    cnt[word] += 1
print (cnt)
# 输出
OrderedCounter(OrderedDict([('b', 1), ('a', 3), ('c', 2)]))
Counter({'a': 3, 'c': 2, 'b': 1})


'''
namedtuple
命名的元组，意味给元组中的每个位置赋予含义，意味着代码可读性更强，namedtuple可以在任何常规元素使用的
地方使用，而且它可以通过名称来获取字段信息而不仅仅是通过位置索引。

namedtuple在给csv或者sqlite3返回的元组附上名称特别有用，
'''
from collections import *
import csv

EmployeeRecord = namedtuple('EmployeeRecord','name, age, title, department, paygrade')
for emp in map(EmployeeRecord._make,csv.reader(open("employee.csv","rb"))):
    print (emp.name,emp.title)


from collections import *
Point = namedtuple('Point',['x','y'],verbose = True)
class Point(tuple):
    'Point(x, y)'

    __slots__ = ()

    _fields = ('x', 'y')

    def __new__(_cls, x, y):
        'Create new instance of Point(x, y)'
        return _tuple.__new__(_cls, (x, y))

    @classmethod
    def _make(cls, iterable, new=tuple.__new__, len=len):
        'Make a new Point object from a sequence or iterable'
        result = new(cls, iterable)
        if len(result) != 2:
            raise TypeError('Expected 2 arguments, got %d' % len(result))
        return result

    def __repr__(self):
        'Return a nicely formatted representation string'
        return 'Point(x=%r, y=%r)' % self

    def _asdict(self):
        'Return a new OrderedDict which maps field names to their values'
        return OrderedDict(zip(self._fields, self))

    def _replace(_self, **kwds):
        'Return a new Point object replacing specified fields with new values'
        result = _self._make(map(kwds.pop, ('x', 'y'), _self))
        if kwds:
            raise ValueError('Got unexpected field names: %r' % kwds.keys())
        return result

    def __getnewargs__(self):
        'Return self as a plain tuple.  Used by copy and pickle.'
        return tuple(self)

    __dict__ = _property(_asdict)

    def __getstate__(self):
        'Exclude the OrderedDict from pickling'
        pass

x = _property(_itemgetter(0), doc='Alias for field number 0')

y = _property(_itemgetter(1), doc='Alias for field number 1')
