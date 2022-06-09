'''
https://www.codewars.com/kata/59f2746e50c8c2b55d000085/train/python

You are given num (up to 15 digits, never less than 0).

If the length of num is even, return odd numbers as ints and even ones as strings,
based on their position in the given number. Strings alternate in type cases: starting
in lowercase to uppercase and so on based on position. If the length of num is odd,
all the rules are opposite. See sample tests.

给定num(最多15位数字，不能小于0)，如果num的长度是偶数，则根据给定数字中的位置，将奇数作为ints，
偶数作为字符串返回。

如果num的长度是偶数，则根据奇数在给定数字中的位置，将奇数作为ints返回，偶数作为字符串返回。字符串
的类型大小写交替进行：根据位置从小写开始到大写，以此类推。如果num的长度是奇数，所有的规则都是相反的。
参见示例测试。

注意：数字的位置是基于1的。

Note: Positions of numbers are 1-based.

import codewars_test as test
from solution import conv

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(conv(0), "0")
        test.assert_equals(conv(11), "11")
        test.assert_equals(conv(1101), "11zer1")
        test.assert_equals(conv(54563), "F4FIV6THREE")
        test.assert_equals(conv(47309534), "f73zero953fourFOUR")
        test.assert_equals(conv(34266262106), "T4266262ONEoneONE06")
        test.assert_equals(conv(15795379351687), "15795379351sixSIXsixSIXeightEIGHTeig7")
        test.assert_equals(conv(157953793516872), "OFISEVNINEFIVEfTHREEtSEVENseNINEnineTHREEthreFIVEfiveFIONEoneONEon68SEVENsevenSEVE2")

'''

def conv(num):
    pass