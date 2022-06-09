'''
https://www.codewars.com/kata/5dd259444228280032b1ed2a/train/python

@test.describe('Fixed Tests')
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_tests():
        test.assert_equals(solve(6,3), (3,3))
        test.assert_equals(solve(8,2), (2,6))
        test.assert_equals(solve(10,3), -1)
        test.assert_equals(solve(12,4), (4,8))
        test.assert_equals(solve(12,5), -1)
'''
import math
def solve(s,g):
    for i in range(1,s+1):
        print(i)
        if math.gcd(i,s-i) == g:
            return [i,s-i]
    return -1
'''
Test Results:
 Fixed Tests
 Basic Test Cases (10 of 10 Assertions)
Completed in 0.20ms
 Random Tests
 Random Test Cases (7 of 7 Assertions)
 STDERR
Max Buffer Size Reached (1.5 MiB)
'''
s,g = 12,4
print(math.gcd(12,4))
print(solve(s,g))

def solve(s,g):
    for i in range(0,s+1,g):
        print(i)
        if math.gcd(i,s-i) == g:
            return [i,s-i]
    return -1

s,g = 12,4
print(math.gcd(12,4))
print(solve(s,g))

#1st solution
def solve(s,g):
    return -1 if s % g else (g, s - g)

#2nd solution
def solve(s,g):
    if s % g != 0:
        return -1
    else:
        b = s - g
        a = g
        return (a,b)