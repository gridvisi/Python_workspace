'''

一种著名的数据结构是堆（heap），它是一种优先队列。优先队列让你能够以任意顺序添加对象，并随时（可能是在两次添加对象之间）找出（并删除）最小的元素。相比于列表方法min，这样做的效率要高得多。
实际上，Python没有独立的堆类型，而只有一个包含一些堆操作函数的模块。这个模块名为heapq（其中的q表示队列），它包含6个函数，其中前4个与堆操作直接相关。必须使用列表来表示堆对象本身。

                                                                             模块heapq中一些重要的函数
                                                               函 数                                                           描 述
                                                      heappush(heap, x)                                        将x压入堆中
                                                        heappop(heap)                                      从堆中弹出最小的元素
                                                        heapify(heap)                                           让列表具备堆特征
                                                  heapreplace(heap, x)                            弹出最小的元素，并将x压入堆中
                                                      nlargest(n, iter)                                       返回iter中n个最大的元素
                                                        nsmallest(n, iter)                                   返回iter中n个最小的元素

函数heappush用于在堆中添加一个元素。请注意，不能将它用于普通列表，而只能用于使用各种堆函数创建的列表。原因是元素的顺序很重要（虽然元素的排列顺序看起来有点随意，并没有严格地排序）。
'''
from heapq import *
sl = [i for i in range(1,4)]
heapify(sl)
print(sl)
heappush(sl,1)
print(sl)
heappush(sl,1)
print(sl)
heappush(sl,1)
print(sl)
heappush(sl,1)
print(sl)
heappop(sl)
print('1st pop:',sl)
heappop(sl)
print('2nd pop:',sl)

sl = [i for i in range(1,11)]
heapify(sl)
print(sl)
heappush(sl,1)
print(sl)

#heapq模块中有6个函数：
#1、heappush(heap, x)：向堆中添加元素


heap = []
for i in range(3):
    heappush(heap, i)
print(heap)   #[0, 1, 2]

heappush(heap, 0.5)
print(heap)    #[0, 0.5, 2, 1]

heappush(heap, 1.5)
print(heap)    #[0, 0.5, 2, 1, 1.5]

#2、heappop(heap)：弹出堆中最小的元素，并且维持剩余元素的堆结构

from heapq import *
heap = []
for i in range(3):
    heappush(heap, i)
print(heap)   #[0, 1, 2]
heappop(heap)
print(heap)    #[1, 2]

#3、heapify(heap)：将列表转换为堆

from heapq import *
heap = [5, 8, 0, 4, 6, 7]
heapify(heap)
print(heap)   #[0, 4, 5, 8, 6, 7]

#4、heapreplace(heap, x)：弹出堆中最小的元素，然后将新元素插入。

from heapq import *
heap = [5, 8, 0, 4, 6, 7]
heapify(heap)
print(heapreplace(heap, 5.5)) #0
print(heap)   #[4, 5.5, 5, 8, 6, 7]


#5、nlargest(n, iter)、nsmallest(n, iter)：
# 用来寻找任何可迭代对象iter中的前n个最大的或前n个最小的元素。

from heapq import *
lst = [5, 8, 0, 4, 6, 7]
print(nsmallest(3, lst))
print(nlargest(3, lst))


from heapq import *
from random import shuffle
data = list(range(10))
shuffle(data)
heap = []
for n in data:
    heappush(heap, n)

print(heap)
#[0, 1, 3, 6, 2, 8, 4, 7, 9, 5]
heappush(heap, 0.5)
print(heap)
#[0, 0.5, 3, 6, 1, 8, 4, 7, 9, 5, 2]

#元素的排列顺序并不像看起来那么随意。它们虽然不是严格排序的，但必须保证一点：位置i处的元素总是大于位置i // 2处的元素
# 反过来说就是小于位置2 * i和2 * i + 1处的元素）。这是底层堆算法的基础，称为堆特征（heap property）
#函数heappop弹出最小的元素（总是位于索引0处），并确保剩余元素中最小的那个位于索引0处（保持堆特征）。
# 虽然弹出列表中第一个元素的效率通常不是很高，但这不是问题，因为heappop会在幕后做些巧妙的移位操作。
heappop(heap)
#0
heappop(heap)
#0.5
heappop(heap)
#1
print(heap)
[2, 5, 3, 6, 9, 8, 4, 7]

#函数heapify通过执行尽可能少的移位操作将列表变成合法的堆（即具备堆特征）。如果你的堆并不是使用heappush创建的，
# 应在使用heappush和heappop之前使用这个函数。
heap = [5, 8, 0, 3, 6, 7, 9, 1, 4, 2]
heapify(heap)
#heap
#[0, 1, 5, 3, 2, 7, 9, 8, 4, 6]

#函数heapreplace用得没有其他函数那么多。它从堆中弹出最小的元素，再压入一个新元素。相比于依次执行函数heappop和heappush，
# 这个函数的效率更高。
heapreplace(heap, 0.5)
#0
print(heap)
#[0.5, 1, 5, 3, 2, 7, 9, 8, 4, 6]

heapreplace(heap, 10)
print(heap)
#0.5

print(heap)
#[1, 2, 5, 3, 6, 7, 9, 8, 4, 10]


# ericlee
print([i for i in range(1,7)])
import heapq
a = []   #创建一个空堆
heapq.heappush(a,1)
heapq.heappush(a,2)
heapq.heappush(a,3)
heapq.heappush(a,4)
heapq.heappush(a,5)
heapq.heappush(a,6)
heapq.heappush(a,1)
heapq.heappush(a,2)
heapq.heappush(a,3)

x = 7
heapq.heappush(a,x)
x = 8
heapq.heappush(a,x)

xl = [9,10]
heapq.heappush(a,xl[0])
heapq.heappush(a,4)
heapq.heappush(a,5)
heapq.heappush(a,6)
heapq.heappush(a,4)
heapq.heappush(a,5)
heapq.heappush(a,6)
heapq.heappush(a,7)
heapq.heappush(a,8)
heapq.heappush(a,9)
print(a)
heapq.heappush(a,10)
heapq.heappush(a,11)
heapq.heappush(a,17)
print(a)
heapq.heappush(a,0)
heapq.heappush(a,1)
heapq.heappush(a,2)
print(a)

heapq.heappush(a,0)
heapq.heappush(a,0)
heapq.heappush(a,0)
heapq.heappush(a,0)
heapq.heappush(a,0)
heapq.heappush(a,0)
print(a)