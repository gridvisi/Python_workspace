'''
https://www.codewars.com/kata/58223370aef9fc03fd000071/train/python
Given a number, return a string with dash'-'marks before and after each odd integer,
but do not begin or end the string with a dash mark.

给定一个数字，返回一个字符串，在每个奇数整数前后都有破折号，但不要以破折号开始或结束。
test.describe('Basic')
test.assert_equals(dashatize(274),"2-7-4", "Should return 2-7-4")
test.assert_equals(dashatize(5311),"5-3-1-1", "Should return 5-3-1-1")
test.assert_equals(dashatize(86320),"86-3-20", "Should return 86-3-20")
test.assert_equals(dashatize(974302),"9-7-4-3-02", "Should return 9-7-4-3-02")
test.describe('Weird')
test.assert_equals(dashatize(None),"None", "Should return None");
test.assert_equals(dashatize(0),"0", "Should return 0");
test.assert_equals(dashatize(-1),"1", "Should return 1");
test.assert_equals(dashatize(-28369),"28-3-6-9", "Should return 28-3-6-9");
'''

def dashatize(num):
    if num == None:
        return "None"
    num = abs(num)
    return ''.join([f"-{i}-" if eval(i) % 2 == 1 else i for i in str(num)]).strip('-').replace("--", '-')

num = 974302
print(dashatize(num))