'''

https://www.codewars.com/kata/59f7fc109f0e86d705000043/train/python

@test.describe('Basic Test Cases')
def basic_tests():
    test.assert_equals(divisible_by_three('123'), True, "Should return true if the sum of the given digits is divisible by 3.")
    test.assert_equals(divisible_by_three('19254'), True, "Should return true if the sum of the given digits is divisible by 3.")
    test.assert_equals(divisible_by_three('88'), False, "Should return false if the sum of the given digits is not divisible by 3.")
    test.assert_equals(divisible_by_three('1'), False, "Should return false if the sum of the given digits is not divisible by 3.")
'''

def divisible_by_three(st):
    return sum([eval(i) for i in st])%3 == 0

def divisible_by_three(s):
    return int(s) % 3 == 0

divisible_by_three=lambda st:int(st)%3==0