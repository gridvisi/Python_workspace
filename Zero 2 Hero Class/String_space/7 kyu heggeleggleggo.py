'''
https://www.codewars.com/kata/55ea5304685da2fb40000018/train/python

Egg Talk.
Insert an "egg" after each consonant. If there are no consonants, there will be no eggs. Argument will consist of a string with only alphabetic characters and possibly some spaces.
eg:
hello => heggeleggleggo
eggs => egegggeggsegg
FUN KATA => FeggUNegg KeggATeggA
////
This Kata is designed for beginners to practice the basics of regular expressions.
With this in mind a little bit of commenting in your solution could be very useful.

Check Eloquent Javascript p176
鸡蛋说话。
在每个辅音后面加一个 "蛋"。如果没有辅音，就没有鸡蛋。参数将由一个只包含字母的字符串和可能的一些空格组成。
例如：Hello => heggelegg。
hello => heggeleggleggo(鸡蛋)
鸡蛋 => egegggeggsegg
FUN KATA => FeggUNegg KeggATeggA
////
这个卡塔是为初学者练习正则表达式的基础知识而设计的。考虑到这一点，在您的解决方案中添加一点注释可能非常有用。
检查Eloquent Javascript p176

import codewars_test as test
from solution import heggeleggleggo

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(heggeleggleggo("hello"), "heggeleggleggo")
        test.assert_equals(heggeleggleggo("code here"), "ceggodegge heggeregge")
        test.assert_equals(heggeleggleggo("FUN KATA"), "FeggUNegg KeggATeggA")
        test.assert_equals(heggeleggleggo("egg"), "egegggegg")
        test.assert_equals(heggeleggleggo("Hello world"), "Heggeleggleggo weggoreggleggdegg")
        test.assert_equals(heggeleggleggo("scrambled eggs"), "seggceggreggameggbeggleggedegg egegggeggsegg")
        test.assert_equals(heggeleggleggo("eggy bread"), "egegggeggyegg beggreggeadegg")
'''

#3rd solve by ericlee
def heggeleggleggo(word):
    return ''.join([e if e.lower() in 'aeiou ' else e + 'egg' for e in word])
word = "eggy bread"
print(heggeleggleggo(word))

#2nd
import re
def heggeleggleggo(word):
    return re.sub(r'(?i)([^aeiou\W])',r'\1egg',word)