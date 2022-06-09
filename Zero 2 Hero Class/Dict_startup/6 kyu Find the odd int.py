'''
https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python

test.assert_equals(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)
test.assert_equals(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]), -1);
test.assert_equals(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]), 5);
test.assert_equals(find_it([10]), 10);
test.assert_equals(find_it([1,1,1,1,1,1,10,1,1,1,1]), 10);
test.assert_equals(find_it([5,4,3,2,1,5,4,3,2,10,10]), 1);
'''

from collections import Counter
def find_it(seq):
    freq = Counter(seq).items()
    print(freq)
    return [k for k,v in freq if v%2==1][0]

seq = [5,4,3,2,1,5,4,3,2,10,10]
print(find_it(seq))