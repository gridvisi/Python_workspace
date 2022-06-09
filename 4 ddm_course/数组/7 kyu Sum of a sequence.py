'''

https://www.codewars.com/kata/586f6741c66d18c22800010a/train/python

FUNDAMENTALSNUMBERSRECURSIONALGORITHMSCOMPUTABILITY THEORYTHEORETICAL
COMPUTER SCIENCELOOPSCONTROL FLOWBASIC LANGUAGE FEATURES

Test.describe("Basic tests")
Test.assert_equals(sequence_sum(2, 6, 2), 12)
Test.assert_equals(sequence_sum(1, 5, 1), 15)
Test.assert_equals(sequence_sum(1, 5, 3), 5)
Test.assert_equals(sequence_sum(0, 15, 3), 45)
Test.assert_equals(sequence_sum(16, 15, 3), 0)
Test.assert_equals(sequence_sum(2, 24, 22), 26)
Test.assert_equals(sequence_sum(2, 2, 2), 2)
Test.assert_equals(sequence_sum(2, 2, 1), 2)
Test.assert_equals(sequence_sum(1, 15, 3), 35)
Test.assert_equals(sequence_sum(15, 1, 3), 0)
'''

def sequence_sum(begin_number, end_number, step):
    return sum(range(begin_number,end_number,step))

begin_number, end_number, step = 1, 15, 3
begin_number, end_number, step = 16, 15, 3
print(sequence_sum(begin_number, end_number, step))