'''
https://www.codewars.com/kata/5a7893ef0025e9eb50000013/train/python

Test.describe("Basic tests")
Test.assert_equals(max_gap([13,10,2,9,5]),4)
Test.assert_equals(max_gap([13,3,5]),8)
Test.assert_equals(max_gap([24,299,131,14,26,25]),168)
Test.assert_equals(max_gap([-3,-27,-4,-2]),23)
Test.assert_equals(max_gap([-7,-42,-809,-14,-12]),767)
Test.assert_equals(max_gap([12,-5,-7,0,290]),278)
Test.assert_equals(max_gap([-54,37,0,64,-15,640,0]),576)
Test.assert_equals(max_gap([130,30,50]),80)
Test.assert_equals(max_gap([1,1,1]),0)
Test.assert_equals(max_gap([-1,-1,-1]),0)
print("<COMPLETEDIN::>")
'''

def max_gap(numbers):
    sl = sorted(numbers)
    print('s',[e - sl[i] for i,e in enumerate(sl[1:])])
    return max([e - sl[i] for i,e in enumerate(sl[1:])])

numbers = [13,10,2,9,5]
print(sorted(numbers))
print(max_gap(numbers))


def max_gap(numbers):
    lst = sorted(numbers)
    return max(b-a for a,b in zip(lst, lst[1:]))

import numpy
def max_gap(numbers):
    return max(numpy.diff(sorted(numbers)))