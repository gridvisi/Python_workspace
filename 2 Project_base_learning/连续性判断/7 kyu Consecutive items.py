'''
https://www.codewars.com/kata/5f6d533e1475f30001e47514/train/python

import codewars_test as test

@test.describe("Simple tests")
def test_group_1():
    @test.it("Test 1")
    def test_1():
        test.assert_equals(consecutive([1, 3, 5, 7], 3, 7), False)
    @test.it("Test 2")
    def test_2():
        test.assert_equals(consecutive([1, 3, 5, 7], 3, 1), True)
    @test.it("Test 3")
    def test_3():
        test.assert_equals(consecutive([1, 6, 9, -3, 4, -78, 0], -3, 4), True)
'''
arr, a, b = [1, 6, 9, -3, 4, -78, 0], -3, 4

def consecutive(arr, a, b):
    return abs(arr.index(a) - arr.index(b)) == 1

print(consecutive(arr, a, b))