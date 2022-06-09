'''
https://www.codewars.com/kata/55eeddff3f64c954c2000059

Test.describe("Basic tests")
Test.assert_equals(sum_consecutives([1,4,4,4,0,4,3,3,1]),[1,12,0,4,6,1], "on list [1,4,4,0,4,3,3,1] you get ")
Test.assert_equals(sum_consecutives([1,1,7,7,3]),[2,14,3], "on list [1,1,7,7,3] you get ")
Test.assert_equals(sum_consecutives([-5,-5,7,7,12,0]),[-10,14,12,0], "on list [-5,-5,7,7,12,0] you get ")
Test.assert_equals(sum_consecutives([3,3,3,3,1]),[12, 1], "on list [3,3,3,3,1] you get " )
'''


def sum_consecutives(s):
    i,j,re = 0,1,[]
    while j < len(s):

        if s[i] == s[j]:
            j += 1

        else:
            re.append(sum(s[i:j]))
            i = j
    return re + [sum(s[i:j])]
s = [1,4,4,4,0,4,3,3,1]
s = [-5,-5,7,7,12,0]
#s = [3,3,3,3,1]
#s = [0, 1, 1, 2, 2]
# on list [0, 1, 1, 2, 2] you get : [0, 2, 2] should equal [0, 2, 4]

from itertools import groupby
def sum_consecutives(s):
    return [sum(group) for c, group in groupby(s)]
print(sum_consecutives(s))


def sum_consecutives(s):
    prev = None
    x = []
    for i in s:
        if i == prev:
            x[-1] += i
        else:
            x.append(i)
        prev = i
    return x

def sum_consecutives(s):
    res = []
    last = None
    for n in s:
        if n != last:
            res.append(n)
            last = n
        else:
            res[-1] += n
    return res
print(sum_consecutives(s))
