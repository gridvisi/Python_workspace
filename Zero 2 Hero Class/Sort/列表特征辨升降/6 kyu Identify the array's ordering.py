'''
https://www.codewars.com/kata/57f669477c9a2b1b9700022d/train/python

test.describe("Basic Tests")
test.assert_equals(order_type([1, "b", ["p"], 2]),"Constant")
test.assert_equals(order_type([123, 1234, 12345, 123456]),"Increasing")
test.assert_equals(order_type(["a", "abc", "abcde", "ab"]),"Unsorted")
test.assert_equals(order_type([[1, 2, 3, 4], [5, 6, 7], [8, 9]]),"Decreasing")
test.assert_equals(order_type([1, 2, 3, 4, 56]),"Increasing")
test.assert_equals(order_type([["ab","cdef", "g"],["hi","jk","lmnopq"],["rst", "uv", "wx"],["yz"]]),"Decreasing")
test.assert_equals(order_type([[1, 23, 456, 78910], ["abcdef", "ghijklmno", "pqrstuvwxy"], [[1, 23, 456, 78910, ["abcdef", "ghijklmno", "pqrstuvwxy"]], 1234]]),"Decreasing")
test.assert_equals(order_type([]),"Constant")
test.assert_equals(order_type(["pippi", "pippi", "batuffulo", "pippi"]),"Unsorted")
test.assert_equals(order_type(["pippi"]),"Constant")

编写一个函数，将一个数组作为参数（包含多个字符串和/或正数和/或数组），并根据输入数组中元素的长度排序，返回四个可能的字符串值之一。

你的函数应该返回...

"增加" - 如果元素的长度从左到右增加（尽管有可能一些相邻的元素的长度也是相等的）。
"减少" - 如果元素的长度从左到右减少（尽管有些相邻元素的长度也可能相等）。
"未排序" - 如果元素的长度从左到右波动
"恒定"--如果所有元素的长度都相同。
数字和字符串应该根据用于书写它们的字符或数字的数量来评估。
'''

#11th solve by kevinlion
def order_type(arr):
    l = [len(str(i)) if isinstance(i,int) else len(i) for i in arr]
    if len(set(l)) in (0,1):return 'Constant'
    elif sorted(l) == l:
        return 'Increasing'
    elif sorted(l) == l[::-1]:
        return 'Decreasing'
    else:return 'Unsorted'

arr = [1, "b", ["p"], 2]
print(order_type(arr))

#1st
def order_type(arr):
    if not arr : return 'Constant'
    arr = list( map(len, [str(elt) if type(elt)==int else elt for elt in arr] ))
    cmp =sorted(arr)
    if arr == [arr[0]]*len(arr) : s='Constant'
    elif arr == cmp :             s='Increasing'
    elif arr == cmp[::-1] :       s='Decreasing'
    else :                        s='Unsorted'
    return s


#2nd
def order_type(arr):
    xs = [len(x) if hasattr(x, '__len__') else len(str(x)) for x in arr]
    ys = sorted(xs)
    return (
        'Constant' if not xs or ys[0] == ys[-1] else
        'Increasing' if xs == ys else
        'Decreasing' if xs[::-1] == ys else
        'Unsorted'
    )