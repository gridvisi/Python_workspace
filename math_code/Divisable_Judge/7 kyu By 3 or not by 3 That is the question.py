# 7 kyu  By 3, or not by 3? That is the question
'''
https://www.codewars.com/kata/59f7fc109f0e86d705000043/train/python
我在小学里学到的一个确定一个数字是否能被三除的技巧是，将数字中的所有整数相加，
然后用所得之和除以三。如果除以3没有余数，那么原来的数字也是可以被3整除的。

给出一串数字作为字符串，确定该字符串所代表的数字是否能被三除。
你可以期望所有测试案例的参数都是代表大于0的数值的字符串。

A trick I learned in elementary school to determine whether or
not a number was divisible by three is to add all of the integers
in the number together and to divide the resulting sum by three.
If there is no remainder from dividing the sum by three, then the
original number is divisible by three as well.

Given a series of digits as a string, determine if the number
represented by the string is divisible by three.

You can expect all test case arguments to be strings representing
values greater than 0.


例子Example:
"123"      -> true
"8409"     -> true
"100853"   -> false
"33333333" -> true
"7"        -> false
'''

def divisible_by_three(st):
    # your code here
    return sum([eval(i) for i in st])%3==0
'''
Test Results:
You"ve % in your code, please remove that and use the described method
You"ve eval in your code, please remove that and use the described method
Basic Test Cases
Test Passed
Test Passed
Test Passed
Test Passed
'''

#1st
def divisible_by_three(st):
    while len(st) != 1:
        st = str(sum(int(n) for n in st))
    return int(st) in [0, 3, 6, 9]


def divisible_by_three(digits: str) -> bool:
    number = int(digits)
    while number > 9:
        number = sum(map(int, str(number)))
    return str(number) in '0369'