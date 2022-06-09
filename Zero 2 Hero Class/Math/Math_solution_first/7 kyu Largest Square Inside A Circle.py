'''
https://www.codewars.com/kata/5887a6fe0cfe64850800161c/train/python

Determine the area of the largest square that can fit inside a circle with radius r.

ALGORITHMSGEOMETRYALGEBRAMATHEMATICS

Test.describe("area_largest_square:")
Test.assert_equals(area_largest_square(5), 50)
Test.assert_equals(area_largest_square(7), 98)
Test.assert_equals(area_largest_square(15), 450)
'''

def area_largest_square(r):
    return 2 * r ** 2