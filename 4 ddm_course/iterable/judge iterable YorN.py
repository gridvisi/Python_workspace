#判断对象是否可迭代
from collections import Iterable
print(isinstance("你好！", Iterable))# -------> True
print(isinstance(792, Iterable)) #-------> False
print(isinstance([7, 9, 2], Iterable)) #-------> True
print(isinstance((7, 9, 2), Iterable)) #-------> True
print(isinstance({"a": 1, "b": 2, "c":3}, Iterable))# -------> True

for i, v in enumerate(["a", "b", "c"]):
    print("第%d个是%s" % (i, v))

'''
---------------------------------------
第0个是a
第1个是b
第2个是c
'''
for x, y in [[1, 2], [3, 4], [5, 6]]:
    print(x, y)

'''
---------------------------------------
(1, 2)
(3, 4)
(5, 6)
'''
