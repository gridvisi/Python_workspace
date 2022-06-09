'''
https://www.codewars.com/kata/568dc69683322417eb00002c/train/python

Given a string, return true if the first instance of "x" in the string is immediately followed by the string "xx".

tripleX("abraxxxas") → true
tripleX("xoxotrololololololoxxx") → false
tripleX("softX kitty, warm kitty, xxxxx") → true
tripleX("softx kitty, warm kitty, xxxxx") → false
Note :

capital X's do not count as an occurrence of "x".
if there are no "x"'s then return false
FUNDAMENTALSSTRINGSLOOPSCONTROL FLOWBASIC LANGUAGE FEATURESREGULAR EXPRESSIONSDECLARATIVE PROGRAMMINGADVANCED LANGUAGE FEATURES

import codewars_test as test
# TODO Write tests
import solution # or from solution import example

# test.assert_equals(actual, expected, [optional] message)
@test.describe("Example")
def test_group():
    @test.it("test case")
    def test_case():
        test.assert_equals(triple_x(""), False)
        test.assert_equals(triple_x("there's no XXX here"), False)
        test.assert_equals(triple_x("abraxxxas"),True);
        test.assert_equals(triple_x("xoxotrololololololoxxx"),False);
        test.assert_equals(triple_x("soft kitty, warm kitty, xxxxx"),True);
        test.assert_equals(triple_x("softx kitty, warm kitty, xxxxx"),False);
'''

def triple_x(s):
    cnt = ''
    i,j = 0, 1
    while i < j <= len(s)-1:

        if s[i] != s[j] or s[i] != s[i].lower() or s[i] != 'x':
            i += 1
            j += 1
        else:
            if s[i] == s[j] == 'x':
                cnt += 'x'
                start,end = i,j
                j += 1
            print(s[i:j+1], i,j,cnt,len(s[i:j+1]), s.index('x'))

            if s[i:j+1] == 'x'*len(s[i:j+1]):
                if s.index('x') == i:
                    return True
                else:
                    if j == len(s)-1:return False
                    else:
                        i = j
                        j += 1


s = "softx kitty, warm kitty, xxxxx"
#s = "xoxotrololololololoxxx"
#s = "abraxxxas"
s = "x xxthere's xx xno XXX herexxx"  # first time fail
print(triple_x(s))

def triple_x(s):
    try:
        return True if s.index("x")==s.index("xxx") else False
    except: return False

#2nd solution
def triple_x(s: str) -> bool:
    return 0 <= s.find("x") == s.find("xxx")

#3rd solution
import re

def triple_x(s):
    return re.match('[^x]*xxx', s) is not None

#4th solution
def triple_x(s):
    pos=s.find('x')
    return s[pos:pos+3]=='xxx'