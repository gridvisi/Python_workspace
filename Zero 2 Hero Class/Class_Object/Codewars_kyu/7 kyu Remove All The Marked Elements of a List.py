'''
https://www.codewars.com/kata/563089b9b7be03472d00002b/train/python

test.describe("Example Tests")
l = List()

integer_list =  [1, 1, 2 ,3 ,1 ,2 ,3 ,4]
values_list = [1, 3]
test.assert_equals(l.remove_(integer_list, values_list), [2, 2, 4])

integer_list = [1, 1, 2 ,3 ,1 ,2 ,3 ,4, 4, 3 ,5, 6, 7, 2, 8]
values_list  = [1, 3, 4, 2]
test.assert_equals(l.remove_(integer_list, values_list), [5, 6 ,7 ,8])

integer_list = [8, 2, 7, 2, 3, 4, 6, 5, 4, 4, 1, 2 , 3]
values_list  = [2, 4, 3]
test.assert_equals(l.remove_(integer_list, values_list), [8, 7, 6, 5, 1])
'''


class List:
    def remove_(self, integer_list, values_list):
        return [i for i in integer_list if i not in values_list]


integer_list = [8, 2, 7, 2, 3, 4, 6, 5, 4, 4, 1, 2 , 3]
values_list  = [2, 4, 3]   #[8, 7, 6, 5, 1]
xl = List
print(xl.remove_(1,integer_list,values_list))

#1st
class List(object):
    def remove_(self, integer_list, values_list):
        blacklist = set(values_list)
        return [val for val in integer_list if val not in blacklist]

print(xl.remove_(1,integer_list,values_list))
print(List.remove_(1,integer_list,values_list))

#2nd
class List(object):
    @staticmethod
    def remove_(xs, ys):
        return [x for x in xs if x not in ys]
print(xl.remove_(1,integer_list,values_list))