'''
https://www.codewars.com/kata/56311e4fdd811616810000ce/train/python

test.describe("Example Tests")
l = List()

integers_list =  [1, 1, 2 ,3 ,1 ,2 ,3 ,4]
digits_list = [1, 3]
test.assert_equals(l.count_spec_digits(integers_list, digits_list),[(1, 3), (3, 2)])

integers_list = [-18, -31, 81, -19, 111, -888]
digits_list = [1, 8, 4]
test.assert_equals(l.count_spec_digits(integers_list, digits_list), [(1, 7), (8, 5), (4, 0)])

integers_list = [-77, -65, 56, -79, 6666, 222]
digits_list = [1, 8, 4]
test.assert_equals(l.count_spec_digits(integers_list, digits_list), [(1, 0), (8, 0), (4, 0)])

integers_list = []
digits_list = [1, 8, 4]
test.assert_equals(l.count_spec_digits(integers_list, digits_list), [(1, 0), (8, 0), (4, 0)])
'''

class List(object):
#    def __init__(self,integers_list,digits_list):
#        self.integers_list = integers_list
#        self.digits_list = digits_list

    def count_spec_digits(self, integers_list, digits_list):
        ans,str_int = [],''.join(list(map(str,integers_list)))

        return [(i,str_int.count(str(i))) for i in digits_list]

integers_list =  [1, 1, 2 ,3 ,1 ,2 ,3 ,4]
digits_list = [1, 3]

#l = List(self,integers_list,digits_list)
l = List()
print(l.count_spec_digits(integers_list,digits_list))


#1st
from collections import Counter

class List(object):
    @staticmethod
    def count_spec_digits(integers_list, digits_list):
        counts = Counter(''.join(str(abs(a)) for a in integers_list))
        return [(b, counts[str(b)]) for b in digits_list]