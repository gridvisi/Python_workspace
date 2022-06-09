'''
https://www.codewars.com/kata/56453a12fcee9a6c4700009c/train/python

test.it("No margin")
test.assert_equals(close_compare(4, 5), -1)
test.assert_equals(close_compare(5, 5), 0)
test.assert_equals(close_compare(6, 5), 1)

test.it("With margin of 3")
test.assert_equals(close_compare(2, 5, 3), 0)
test.assert_equals(close_compare(5, 5, 3), 0)
test.assert_equals(close_compare(8, 5, 3), 0)
test.assert_equals(close_compare(8.1, 5, 3), 1)
test.assert_equals(close_compare(1.99, 5, 3), -1)

Please note the following:

When a is close to b, return 0.
Otherwise...

When a is less than b, return -1.

When a is greater than b, return 1.

If margin is not given, treat it as zero.
'''

def close_compare(a, b, margin=0):
    if a - b <= margin:
        return 0
    else:
        if a < b: return -1
        elif a>b: return 1

#1st
def close_compare(a, b, margin = 0):
    return 0 if abs(a - b) <= margin else -1 if b > a else 1

#2nd
def close_compare(a, b, margin=0):
    if a == b or abs(a - b) <= margin:
        return 0
    if a < b:
        return -1
    if a > b:
        return 1

#课外任务
# 编写一个函数gap_age(a,b)
# a,b 是两人的岁数，返回两个人年龄相差几岁？
# abs函数是？

def gap_age(a,b): #a,b is positive number
    return a-b if a>=b else b-a
print(gap_age(19,23))