'''
https://www.codewars.com/kata/51e0007c1f9378fa810002a9/train/python

Write a simple parser that will parse and run Deadfish.

Deadfish has 4 commands, each 1 character long:

i increments the value (initially 0)
d decrements the value
s squares the value
o outputs the value into the return array
Invalid characters should be ignored.

parse("iiisdoso")  ==>  [8, 64]
ALGORITHMSPARSINGSTRINGS

Test.assert_equals(parse("ooo"), [0,0,0])
Test.assert_equals(parse("ioioio"), [1,2,3])
Test.assert_equals(parse("idoiido"), [0,1])
Test.assert_equals(parse("isoisoiso"), [1,4,25])
Test.assert_equals(parse("codewars"), [0])
'''

def parse(data):
    s = 0
    ans = []
    op = {'i':"+1",'d':"-1",'s':"*"}
    for x in data:
        if x == 'i': s += 1
        elif x == 'd': s -= 1
        elif x == 's': s *= s
        elif x == 'o': ans.append(s)
        else:pass
    return ans
data = "ooo"
data = "isoisoiso"
data = "codewars"
print(parse(data))