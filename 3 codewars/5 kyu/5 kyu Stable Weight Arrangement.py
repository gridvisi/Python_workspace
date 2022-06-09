'''
https://www.codewars.com/kata/stable-weight-arrangement/train/python
这是一个简单的任务。获取唯一正整数的数组/元组，以及两个附加的正整数。下面是一个例子：
arr=（3,5,7,1,6,8,2,4）
n=3#跨度
q=13#重量阈值
尝试重新排列arr，使任意n个连续值之和不超过q。
'''
arr = (3,5,7,1,6,8,2,4)
n = 3 # span length
q = 13 # weight threshold
#solver(arr,n,q) ## one possible solution: (4,7,1,5,6,2,3,8)

def s(p, arr, n, q):
    l = len(p)
    if (l >= n and sum(p[l - n:]) > q) or (l < n and sum(p) > q):
        return []
    if arr == []:
        return p
    for a in arr:
        ar = list(arr)
        ar.remove(a)
        r = s(p + [a], ar, n, q)
        if r != []:
            return r
    return []

def solver(arr, n, q):
    return s([], list(arr), n, q)
print(solver(arr, n, q))

def bottom_up_seque(c):
    lent = len(c)
    table = [None] * (lent + 1)
    table[0] = 0
    table[1] = c[0]
    for i in range(2, lent + 1):
        table[i] = max(table[i - 1] + c[i - 1], c[i - 1])
    return table


def back_seque(table, c):
    select = []
    import numpy
    lent = len(table)
    max_sum = max(table)  # max_sum为table中的最大值
    max_i = numpy.argmax(table)  # max_i为table中最大元素的索引
    i = max_i
    while max_sum > 0:
        max_sum -= c[i - 1]
        select.append(c[i - 1])
        i -= 1
    return select


if __name__ == "__main__":
    c = [-2, 11, -4, 13, -5, 2]
    temp = bottom_up_seque(c)
    select = back_seque(temp, c)
    print("动态规划表：")
    print(temp)
    print(select[::-1])

A = [2, 3, 4, 1, -1, 7, -3, 7, -6]


def solver(arr,n,q):
    res = [arr[i:i+n] for i in range(len(arr)-n)]

    return sorted(res)
#[(3, 5, 7), (5, 7, 1), (7, 1, 6), (1, 6, 8), (6, 8, 2)]
print(solver(arr,n,q))


'''
import itertools
def solver(arr,n,q):
    re,res = [],[]
    for i in itertools.combinations(arr, n):
        if sum(i) <= q:
            re.append(i)
    print(re)
    for i in re:
        for j in re:
            if i[1:] == j[:2]:
                res.append((i,j))
    return res
'''

