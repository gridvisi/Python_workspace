'''
https://www.codewars.com/kata/5809c661f15835266900010a/train/python

test.assert_equals(double_every_other([1,2,3,4,5]), [1,4,3,8,5])
test.assert_equals(double_every_other([1,19,6,2,12,-3]), [1,38,6,4,12,-6])
test.assert_equals(double_every_other([-1000,1653,210,0,1]), [-1000,3306,210,0,1])
'''

# index() is not fix link with the i , it linked value same with ahead of the position
def double_every_other(lst):
    return [2*i if lst.index(i)%2==1 else i for i in lst]

def double_every_other(lst):
    return [2*e if i%2 ==1 else e for i,e in enumerate(lst)]
