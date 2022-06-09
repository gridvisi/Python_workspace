'''
https://www.codewars.com/kata/526c7363236867513f0005ca/train/python
n this kata you should simply determine, whether a given year is a leap year or not.
In case you don't know the rules, here they are:

years divisible by 4 are leap years
but years divisible by 100 are not leap years
but years divisible by 400 are leap years
Additional Notes:

Only valid years (positive integers) will be tested, so you don't have to validate them
Examples can be found in the test fixture.

test.describe('Leap years (should equal True)')
test.assert_equals(isLeapYear(1984), True, 'Year 1984 was a leap year!')
test.assert_equals(isLeapYear(2000), True, 'Year 2000 was a leap year!')

test.describe('Normal years (should equal False)')
test.assert_equals(isLeapYear(1234), False, 'Year 1234 was NOT a leap year!')
test.assert_equals(isLeapYear(1100), False, 'Year 1100 was NOT a leap year!')
'''

def isLeapYear(year):
    return year%100 != 0 and year%4 == 0 or year%400 == 0

#1st
def isLeapYear(year):
    return (year % 100 != 0 and year % 4 == 0) or year % 400 == 0

def isLeapYear(year):
    return year % 4 is 0 and year % 100 is not 0 or year % 400 == 0