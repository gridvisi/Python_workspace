
x = [range(3*i, 3*i+5) for i in range(2)]
print(x)
x = list(map(list, x))
print(x)
x = list(map(list, zip(*x)))
print(x)
#答：首先生成一个包含列表的列表，然后模拟矩阵转置。

import string
x = string.ascii_letters + string.digits
print(x)
import random
print("".join(random.sample(x, 10)))

def demo():
    x = 5
    x = 3
print(demo())
print(x)
