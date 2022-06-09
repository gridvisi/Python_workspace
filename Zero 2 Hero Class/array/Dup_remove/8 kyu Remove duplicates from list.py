# https://www.codewars.com/kata/57a5b0dfcf1fa526bb000118/train/python
'''
Define a function that removes duplicates from an array of numbers
and returns it as a result.

The order of the sequence has to stay the same.
import codewars_test as test
from solution import distinct

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(distinct([1]), [1])
        test.assert_equals(distinct([1, 2]), [1, 2])
        test.assert_equals(distinct([1, 1, 2]), [1, 2])
        test.assert_equals(distinct([1, 1, 1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        test.assert_equals(distinct([1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 7, 7]), [1, 2, 3, 4, 5, 6, 7])
'''

def distinct(seq):
    ans = []
    for i in seq:
        if i not in ans:
            ans.append(i)
    return ans

def distinct(seq):
    return sorted(set(seq), key = seq.index)