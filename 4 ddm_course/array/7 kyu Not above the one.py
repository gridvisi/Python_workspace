'''
https://www.codewars.com/kata/5b5097324a317afc740000fe/train/python
Task
Implement a function which finds the numbers less than 2, and the indices of numbers greater
than 1 in the given sequence, and returns them as a pair of sequences.

Return a nested array or a tuple depending on the language:
The first sequence being only the 1s and 0s from the original sequence.
The second sequence being the indexes of the elements greater than 1 in the original sequence.
@test.describe('Example Tests')
def example_tests():
    test.assert_equals(binary_cleaner([0,1,2,1,0,2,1,1,1,0,4,5,6,2,1,1,0]), ( [ 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0 ], [ 2, 5, 10, 11, 12, 13 ] ))
    test.assert_equals(binary_cleaner([0,1,1,2,0]), ( [ 0, 1, 1, 0 ], [ 3 ] ))
    test.assert_equals(binary_cleaner([2,2,0]), ( [ 0 ], [ 0, 1 ] ))
    test.assert_equals(binary_cleaner([0,1,2,1,0,2,1,1]), ( [ 0, 1, 1, 0, 1, 1 ], [ 2, 5 ] ))
    test.assert_equals(binary_cleaner([1]), ( [ 1 ], [] ))
'''
# AttributeError: 'list' object has no attribute 'find'


def binary_cleaner(seq):
    zero_one = [0,1]
    return tuple([[i for i in seq if i in zero_one]] + [[i for i,e in enumerate(seq) if e not in zero_one]])

def binary_cleaner(seq):
    zero_one = [0,1]
    return tuple(i if i in zero_one else seq.index(i) for i in seq)

#1st solution
def binary_cleaner(seq):
    res = ([], [])
    for i,x in enumerate(seq):
        if x < 2: res[0].append(x)
        else: res[1].append(i)
    return res

