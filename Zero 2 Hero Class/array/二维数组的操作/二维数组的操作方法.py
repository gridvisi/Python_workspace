# http://www.manongjc.com/detail/19-vuddoaxvcfedzfs.html
#1. 最基础的 for 循环
def transpose_2d(data):
    transposed = []
    for i in range(len(data[0])):
        new_row = []
        for row in data:
            new_row.append(row[i])
        transposed.append(new_row)
    return transposed

#2. 使用列表推导式 List Comprehension
# 这个其实是第一种方法的高级简化写法。

def transpose_2d(data):
    transposed = [[row[i] for row in data] for i in range(len(data[0]))]
    return transposed


data = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(transpose_2d(data))

# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
# [Finished in 0.1s]


#3. 使用 zip(*iterable) 函数（推荐）
#一种高效的写法，因为 list, map, zip 都是 Python 内建的函数
# (Built-ins)。

def transpose_2d(data):
    # transposed = list(zip(*data))
    # [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
    # 注意 zip 本身返回的数据类型为 tuple 元组
    # 其中符号 * 号可以对元素进行解压或展开

    transposed = list(map(list, zip(*data)))
    return transposed


data = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(transpose_2d(data))

# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
# [Finished in 0.1s]

#4. 使用 numpy 的 T 转置
from numpy import transpose

data = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

transposed = transpose(data).tolist()
print(transposed)

# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
# [Finished in 0.3s]
# 速度中规中矩，毕竟 numpy 用来处理数学更好

#from pandas import DataFrame

data = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

transposed = DataFrame(data).T.values.tolist()
print(transposed)

# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
# [Finished in 0.7s]
# 可能因为 pandas 本身调用了其他的库，这里明显感觉偏慢，杀鸡用牛刀了
'''
总结
综上，在一般情况下，我们直接使用 Python 内置的 zip(*) 函数就可以快速实
现二维矩阵转置了，当然使用其他一些专用的库也是可以的，在性能和便捷程度上
做好取舍就可以了，希望对需要的朋友有帮助，感谢支持~
'''



data = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(transpose_2d(data))

# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
# [Finished in 0.1s]

#创建一个宽度为3，高度为4的数组
#[[0,0,0],
# [0,0,0],
# [0,0,0],
# [0,0,0]]
myList = [[0] * 3] * 4

# 转置二维数组
a = [[1, 2, 3], [4, 5, 6]]
b = []

for i in range(3):
    b.append([0] * 2)
print(b)

for i in range(len(b)):
    for j in range(len(b[i])):
        b[i][j] = a[j][i]
print(b)

# 转置二维数组
a = [[1, 2, 3], [4, 5, 6]]
b = []

for i in range(len(a[0])):  # 行数
    t = []
    for j in range(len(a)):
        t.append(a[j][i])
    b.append(t)
print(b)
#原文链接：https: // blog.csdn.net / weixin_43778797 / article / details / 90450211