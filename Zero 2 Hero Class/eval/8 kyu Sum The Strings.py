'''
https://www.codewars.com/kata/5966e33c4e686b508700002d/train/python

Create a function that takes 2 positive integers in form of a string as an input, and outputs the sum (also as a string):

  sum_str("4", "5")    # should output "9"
  sum_str("34", "5")   # should output "39"
If either input is an empty string, consider it as zero.

FUNDAMENTALS
import codewars_test as test
from solution import sum_str

@test.describe("Fixed Tests")
def basic_tests():

    @test.it("Sample Tests")
    def sample_tests():
        test.assert_equals(sum_str("4","5"), "9")
        test.assert_equals(sum_str("34","5"), "39")

    @test.it("Tests with empty strings")
    def empty_string():
        test.assert_equals(sum_str("9",""), "9", "x + empty = x")
        test.assert_equals(sum_str("","9"), "9", "empty + x = x")
        test.assert_equals(sum_str("","") , "0", "empty + empty = 0")
'''

def sum_str(a, b):
    if not (a or b): return '0'
    return str(eval(a) + eval(b)) if a and b else str(eval(a+b))
a, b = "","9"
a, b = "9",""
print(sum_str(a, b))

#1st
def sum_str(a, b):
    return str(int(a or 0) + int(b or 0))

'''
进一步，寻找一个数附近的平方数：例如3，3最接近的平方数是4，因为4是2的平方而且没有比4更接近的了，3-1=2，4-3=1
'''


'''
进一步，寻找一定范围内，有多少个数恰好是2的整数幂，​如：0-10之间有2，4，8满足，即有3个​！
'''
a = 100
b = 1000
print(bin(a),bin(b))

