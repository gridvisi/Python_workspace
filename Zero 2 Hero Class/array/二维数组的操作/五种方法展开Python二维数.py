
# 12名同学平均分4组询价购买3种文具，汇总的结果如下arr
# 要求按照每一组价格总和从小到大排序，并且每一组的价格也排序
arr = [[7, 2, 3],
       [4, 9, 6],
       [6, 3, 5],
       [2, 4, 3]]

print(list(map(sorted,sorted(arr,key=lambda x:sum(x)))))


arr = [[1, 2, 3],
       [4, 5, 6],
       [1, 3, 5],
       [2, 4, 8]]

print('sum:',sorted(arr,key=lambda x:sum(x)))

#1 列表推导式
print([i for j in arr for i in j])

#2 sum
print(sum(arr,[]))

#3 reduce
import operator
from functools import reduce
print(reduce(operator.add, arr))

#4 chain
from itertools import chain
print(list(chain.from_iterable(arr)))

arr = [[1, 2, 3],
       [4, 5, 6],
       [1, 3, 5],
       [2, 4, 8]]
#5 flatten
from numpy import *
import numpy as np
arr = array(arr)
ans = arr.flatten()
print('flatten:',ans)

print('sum:',sorted(arr,key=lambda x:sum(x)))

sl = [[6, [1, 2, 3]], [15, [4, 5, 6]], [9, [1, 3, 5]], [14, [2, 4, 8]]]
print([i[1] for i in sl])
#print(sum([i[1] for i in sl],[]))
#print(sum(sl,[]))


import numpy as np
a = np.eye(3,4).T
data = a.flatten()
#print(data )
