
'''
有一个村落，居民沿河而住，每家距离村口的距离如下所示。新来了一位村民
选择住址，为了最短距离的拜访村里的所有居民，选在哪个位置最后，注意可以多个
居民住在离村口距离相同的位置。


10-12
在游戏节目中，参赛者会得到一个数字。他们可以通过点击一个按钮来增加或减少
一个数字中的一个数字。他们需要在尽可能少的点击次数中使所有的数字都相等。
例如，如果数字114，点击三次, 将一个数字减少三次，给出111。

对于以下每一个数字，使所有数字相等所需的最少点击次数是多少？

A.  2393

B.  99478

C.  5559993321

'''

def disCount(s): #字符串转换位数字数组
    distances = []
    s = [int(i) for i in s]
    for i in range(min(s),max(s)+1):
        distances.append((i,sum([abs(i-j) for j in s])))
    return min(distances,key=lambda x:x[1])
s = '5559993321'
print(disCount(s))

s = '99478'
print(disCount(s))

s = '2393'
print(disCount(s))
