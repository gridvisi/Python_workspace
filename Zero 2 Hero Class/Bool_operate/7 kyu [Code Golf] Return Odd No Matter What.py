'''
https://www.codewars.com/kata/5f882dcc272e7a00287743f5/train/python
import codewars_test as test

@test.describe("Example")
def test_group():
    @test.it("test case")
    def test_1():
        test.assert_equals(always_odd(1), 1)
        test.assert_equals(always_odd(2), 1)
        test.assert_equals(always_odd(5), 5)
        test.assert_equals(always_odd(8), 7)
        test.assert_equals(always_odd(-3), -3)
        test.assert_equals(always_odd(-14), -15)

'''

def always_odd(n):
    return n - int(abs(n)%2==0)

'''
Test Results:
Code test
Code length test
Log
Your code length is: 51
Limit: 36
Value is not what was expected
Completed in 0.01ms
Completed in 0.02ms
Example
test case (6 of 6 Assertions)
Completed in 0.04ms
'''

always_odd=lambda n:n-(n%2==0)

always_odd=lambda n:n-1|1

always_odd=lambda n:n+abs(n%2)-1