'''
https://www.codewars.com/kata/583989556754d6f4c700018e/train/python

Print all numbers up to 3rd parameter which are multiple of both 1st and 2nd parameter.

Python, Javascript, Java, Ruby versions: return results in a list/array

NOTICE:

Do NOT worry about checking zeros or negative values.
To find out if 3rd parameter (the upper limit) is inclusive or not, check the tests,
it differs in each translation

s1, s2, s3 = 2,4,40
print(s1, s2, s3)
test.assert_equals(multiples(s1,s2,s3), [4, 8, 12, 16, 20, 24, 28, 32, 36])

s1, s2, s3 = 3,4,40
print(s1, s2, s3)
test.assert_equals(multiples(s1,s2,s3), [12, 24, 36])

s1, s2, s3 = 7,4,80
print(s1, s2, s3)
test.assert_equals(multiples(s1,s2,s3), [28, 56])

s1, s2, s3 = 7,4,20
print(s1, s2, s3)
test.assert_equals(multiples(s1,s2,s3), [])
'''

# Python version: return multiples of 2 numbers in a list

#15th solve by ericlee
def multiples(s1,s2,s3):
    return [i for i in range(0,s3,min(s1,s2)) if i%s2 == 0 and i%s1 == 0 and i != 0]
s1,s2,s3 = 7,4,80
print(multiples(s1,s2,s3))

#1st
def multiples(s1,s2,s3):
    return [x for x in range(s1, s3) if x % s1 == 0 and x % s2 == 0]

#2nd
from fractions import gcd
def multiples(s1,s2,s3):
    lcm = s1 * s2 // gcd(s1, s2)
    return range(lcm, s3, lcm)