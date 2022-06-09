'''
https://www.codewars.com/kata/5aa39ba75084d7cf45000008/train/python

f0 = '0'
f1 = '01'
f2 = '010' = f1 + f0
f3 = '01001' = f2 + f1
You will be given a number and your task is to return the nth fibonacci string. For example:

solve(2) = '010'
solve(3) = '01001'

Test.it("Basic tests")
Test.assert_equals(solve(0),'0')
Test.assert_equals(solve(1),'01')
Test.assert_equals(solve(2),'010')
Test.assert_equals(solve(3),'01001')
Test.assert_equals(solve(5),'0100101001001')
'''

n = 5
def solve(n):
    a,b = '0','01'
    for i in range(n):
        a,b = b,b+a
    return a
print(solve(n))