'''
https://www.codewars.com/kata/5f8341f6d030dc002a69d7e4/train/python

Task
Given an array of numbers and an index, return the index of the least number
larger than the element at the given index, or -1 if there is no such index
 ( or, where applicable, Nothing or a similarly empty value ).

Notes
Multiple correct answers may be possible. In this case, return any one of them.
The given index will be inside the given array.
The given array will, therefore, never be empty.
任务
给定一个数组和一个索引，返回比给定索引的元素大的最小数的索引，如果没有这样的索引，则返回-1（或者，在适用的情况下，
返回Nothing或类似的空值）。

注释
可能有多个正确答案。在这种情况下，返回任意一个答案。
给定的索引将在给定数组中。
因此，给定的数组永远不会是空的。
Example

import codewars_test as test
from solution import least_larger

@test.it("example tests")
def test_case():
    test.assert_equals(least_larger( [4, 1, 3, 5, 6], 0), 3 )
    test.assert_equals(least_larger( [4, 1, 3, 5, 6], 4), -1 )
    test.assert_equals(least_larger( [1, 3, 5, 2, 4], 0), 3 )
'''

a,i = [4, 1, 3, 5, 6],0
a,i = [4, 1, 3, 5, 6], 4
#a,i = [1, 3, 5, 2, 4], 0
def least_larger(a, i):
    flag = [float('inf'),0]  #float('inf')
    for x,e in enumerate(a):
        if 0 < e - a[i] < flag[0]:
            flag = [e - a[i],x]
        #flag[1] = -1
    return flag[1] if flag[0] < float('inf') else -1
#[x if e > a[i] else -1 for x,e in enumerate(a)][::-1][0]

#1st solution
def least_larger(a, i):
    b = [x for x in a if x>a[i]]
    return a.index(min(b)) if b else -1
print(least_larger(a, i))