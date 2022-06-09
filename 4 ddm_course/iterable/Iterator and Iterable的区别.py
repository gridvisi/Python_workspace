
'''
Python中 list，truple，str，dict这些都可以被迭代，但他们并不是迭代器。为什么？

因为和迭代器相比有一个很大的不同，list/truple/map/dict这些数据的大小是确定的，
也就是说有多少事可知的。但迭代器不是，迭代器不知道要执行多少次，所以可以理解为
不知道有多少个元素，每调用一次next()，就会往下走一步，是惰性的。
判断是不是可以迭代，用Iterable

'''

for x in [1,2,3,4,5]:
    pass

# 等价于
#先获取iterator对象

it = iter([1,2,3,4,5])
while True:
    try:
        #获取下一个值
        x = next(it);
    except StopIteration:
        # 遇到StopIteration就退出循环
        break

'''
py:18: DeprecationWarning: Using or importing the ABCs from 'collections' 
instead of from 'collections.abc' is deprecated since Python 3.3, 
and in 3.9 it will stop working from collections import Iterator


“如果蜜蜂从地球上消失，人类将只能再存活4年。没有蜜蜂，没有授粉，没有植物，没有动物，也就没有人类。”
— 阿尔伯特 爱因斯坦

"If All the bees die on earth, we would die due to not enough food sustain the living"  
--- Albert Einstein

据说人类饭桌上三分之一的食物都要感谢蜜蜂给植物授粉，这句广泛流传的话是否出自阿尔伯特 爱因斯坦，大有争议。
当我们用程序验证暗含其中的密码，从中发现了一个巧合，大喵倾向认为这句话是鼎鼎大名的物理学家的金句。
如何验证？

'''

str = "If all the bees die on earth, we would die due to not enough food sustain the living"
name = "Albert Einstein"

# 变量c再取下一个值 c==p,条件判断p不是空格，执行next(st)，

def name_in_str(str, name):
    it = iter(str.lower())
    #print(next(it))
    #print(list(it))
    return all(c in it for c in name.lower())

print(name_in_str(str, name))

s = iter('abcd')
if 'b' in s:
    print(next(s))
'''
from collections.abc import Iterator
from collections import Iterable

py:18: DeprecationWarning: 从'collections'而不是从'collections.abc'中使用或导入ABC，
从Python 3.3开始就被废弃了，在3.9中它将停止'collections'导入Iterator
'''


#判断是不是迭代器，用Iterable

from collections.abc import Iterable
from collections.abc import Iterator

isinstance({}, Iterable) #--> True
isinstance((), Iterable) #--> True
isinstance(100, Iterable) #--> False

#判断是不是迭代器，用Iterator
#from collections import Iterator
isinstance({}, Iterator) # --> False
isinstance((), Iterator) # --> False
isinstance((x for x in range(10)), Iterator) # --> True

'''

所以，
凡是可以for循环的，都是Iterable
凡是可以next()的，都是Iterator
集合数据类型如list，truple，dict，str，
都是Itrable,但不是Iterator，但可以通过iter()函数获得一个Iterator对象
Python中的for循环就是通过next实现的

'''