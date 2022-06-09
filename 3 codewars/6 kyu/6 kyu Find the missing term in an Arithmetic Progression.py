'''

https://www.codewars.com/kata/52de553ebb55d1fca3000371/train/python
一个算术进阶的定义是，在一个给定的数字系列的连续项之间有一个恒定的差异。我们为你提供了一个算术递进的连续元素。
然而，有一个问题：在给你的数字集合中，恰恰缺少了原始数列中的一个项。其余的数列与原来的AP是一样的。找出缺失的项。
你必须写一个函数，接收一个列表，列表大小将永远是至少3个数字。缺少的项永远不会是第一个或最后一个。
test.assert_equals(find_missing([1, 2, 3, 4, 6, 7, 8, 9]), 5)
test.assert_equals(find_missing([1, 3, 4, 5, 6, 7, 8, 9]), 2)
find_missing([1, 3, 5, 9, 11]) == 7
'''
def find_missing(sequence):
    equal = [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]
    step = [i if equal.count(i) > 1 else i for i in set(equal)]
    return step[0] + sequence[equal.index(step[1])]  #something wrong ???
sequence = [1, 3, 5, 9, 11]
print(find_missing(sequence))

def find_missing(sequence):
    seq = range(sequence[0],sequence[-1],(sequence[-1]-sequence[0])//len(sequence))
    equal = sum(seq)+sequence[-1] - sum(sequence)
    return equal
sequence = [1, 3, 5, 9, 11]
print(find_missing(sequence))

def find_missing(sequence):
    t = sequence
    return (t[0] + t[-1]) * (len(t) + 1) / 2 - sum(t)

def find_missing(sequence):
    interval = (sequence[-1] - sequence[0])/len(sequence)
    for previous, item in enumerate(sequence[1:]):
        if item - sequence[previous] != interval:
            return item - interval


def find_missing(s):
    return (len(s) + 1) * (s[0] + s[len(s) - 1]) / 2 - sum(s)