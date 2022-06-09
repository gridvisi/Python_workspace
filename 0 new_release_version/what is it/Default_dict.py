'''
https://blog.csdn.net/u010700415/article/details/17919289?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.nonecase
默认值可以很方便
众所周知，在Python中如果访问字典中不存在的键，会引发KeyError异常（JavaScript中如果对象中不存在某个属性，
则返回undefined）。但是有时候，字典中的每个键都存在默认值是非常方便的。例如下面的例子：

'''
from collections import defaultdict
bill = 139
f_value = (100,50,20,10)
counts = {}
for kw in f_value:
    if bill >= kw:
        counts[kw] = counts.setdefault(kw, 0) + bill//kw
        bill -= kw * counts[kw]
        print(bill)
print(counts,bill)

#re = [counts.setdefault(kw, 0) + bill//kw for kw in f_value if bill >= kw]
#print(re,counts)


strings = ('puppy', 'kitten', 'puppy', 'puppy',
           'weasel', 'puppy', 'kitten', 'puppy')
counts = {}

#for kw in strings:
#    counts[kw] += 1
#print(counts)
'''
该例子统计strings中某个单词出现的次数，并在counts字典中作记录。单词每出现一次，在counts相对应的键所存的值数字加1。
但是事实上，运行这段代码会抛出KeyError异常，出现的时机是每个单词第一次统计的时候，因为Python的dict中不存在默认值的说法，
可以在Python命令行中验证：
'''
# solution 1
strings = ('puppy', 'kitten', 'puppy', 'puppy',
           'weasel', 'puppy', 'kitten', 'puppy')
counts = {}

for kw in strings:
    if kw not in counts:
        counts[kw] = 1
    else:
        counts[kw] += 1
print(counts)

# solution 2
strings = ('puppy', 'kitten', 'puppy', 'puppy',
           'weasel', 'puppy', 'kitten', 'puppy')
counts = {}

for kw in strings:
    counts.setdefault(kw, 0)
    counts[kw] += 1
print(counts)

# counts:
# {'puppy': 5, 'weasel': 1, 'kitten': 2}
strings = ('puppy', 'kitten', 'puppy', 'puppy',
           'weasel', 'puppy', 'kitten', 'puppy')
counts = {}

for kw in strings:
    counts[kw] = counts.setdefault(kw, 0) + 1
print(counts)



from collections import defaultdict
s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
d = defaultdict(set)
for k, v in s:
    d[k].add(v)
print('\n',d)
print('except',d['blue'])
print('except',d['yellow'])
a=sorted(d.items())
print('\n',a)



#Trait of clean python
'''
from collections import defaultdict

class CallCount:
    def __init__(self):
        self._counts = defaultdict(int)

    def __call__(self):
        self._counts[argument] += 1
        return self._counts[argument]

c = CallCount()
print(c())
'''


class defaultdict(dict):
    def __init__(self, default_factory=None, *a, **kw):
        dict.__init__(self, *a, **kw)
        self.default_factory = default_factory

    def __getitem__(self, key):
        try:
            return dict.__getitem__(self, key)
        except KeyError:
            return self.__missing__(key)

    def __missing__(self, key):
        self[key] = value = self.default_factory()
        return value
