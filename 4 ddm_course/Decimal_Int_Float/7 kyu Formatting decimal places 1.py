'''
https://www.codewars.com/kata/5641c3f809bf31f008000042/train/python


test.it("works for some examples")
test.assert_equals(two_decimal_places(10.1289767789), 10.12, "didn't work for 10.1289767789")
test.assert_equals(two_decimal_places(-7488.83485834983), -7488.83, "didn't work for -7488.83485834983")
test.assert_equals(two_decimal_places(4.653725356), 4.65, "didn't work for 4.653725356")
'''


def two_decimal_places(number):
    return int(number * 100) / 100.0

import math
def two_decimal_places(number):
    #raise NotImplementedError("TODO: two_decimal_places")
    return float(str(number)[:len(str(int(number)))+3])

#math.floor(number*1000)/1000
# #number%1
# #abs(number)/1
# round(number,2) 四舍五入

number = -7488.83485834983
number = 32.8493
print(two_decimal_places(number))