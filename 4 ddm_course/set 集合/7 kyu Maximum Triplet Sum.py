'''
https://www.codewars.com/kata/5aa1bcda373c2eb596000112/train/python

Notes :
Array/list size is at least 3 .

Array/list numbers could be a mixture of positives , negatives and zeros .

Repetition of numbers in the array/list could occur , So (duplications are not included when summing).

        test.assert_equals(max_tri_sum([3,2,6,8,2,3]),17)
        test.assert_equals(max_tri_sum([2,9,13,10,5,2,9,5]),32)
        test.assert_equals(max_tri_sum([2,1,8,0,6,4,8,6,2,4]),18)
        test.assert_equals(max_tri_sum([-3,-27,-4,-2,-27,-2]),-9)
        test.assert_equals(max_tri_sum([-14,-12,-7,-42,-809,-14,-12]),-33)
        test.assert_equals(max_tri_sum([-13,-50,57,13,67,-13,57,108,67]),232)
        test.assert_equals(max_tri_sum([-7,12,-7,29,-5,0,-7,0,0,29]),41)
        test.assert_equals(max_tri_sum([-2,0,2]),0)
        test.assert_equals(max_tri_sum([-2,-4,0,-9,2]),0)
        test.assert_equals(max_tri_sum([-5,-1,-9,0,2]),1)

'''

def max_tri_sum(numbers):
    return sum(sorted([i for i in set(numbers)])[-3:])

#1st
def max_tri_sum(numbers):
    return sum(sorted(set(numbers))[-3:])