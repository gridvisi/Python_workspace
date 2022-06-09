'''
https://www.codewars.com/kata/56b5dc75d362eac53d000bc8/train/python

@test.describe('Example Tests')
def example_tests():
    test.assert_equals(calculate_string(";$%§fsdfsd235??df/sdfgf5gh.000kk0000"), "47")
    test.assert_equals(calculate_string("sdfsd23454sdf*2342"), "54929268")
    test.assert_equals(calculate_string("fsdfsd235???34.4554s4234df-sdfgf2g3h4j442"), "-210908")
    test.assert_equals(calculate_string("fsdfsd234.4554s4234df+sf234442"), "234676")
    test.assert_equals(calculate_string("a1a2b3c.c0c/a1a0b.cc00c"), '12')
'''
#20th solution
def calculate_string(st):
    op = '+-*/.'
    cal_st = [i for i in st if i.isnumeric() or i in op]
    for operator in cal_st:
        if operator in op[-1]:
            idx = cal_st.index(operator)
    ans = eval(''.join(cal_st))
    return f"{int(ans+0.5)}" if ans > 0 else f"{int(ans-0.5)}"


st = ";$%§fsdfsd235??df/sdfgf5gh.000kk0000"
st = "fsdfsd235???34.4554s4234df-sdfgf2g3h4j442"
print(calculate_string(st))

'''
使用 int() 将小数转换为整数，小数取整会采用比较暴力的截断方式，
即向下取整。
（注：5.5向上取整为6，向下取整为5）
正常情况下 int(5.5) 结果为5
如果想要让其按照人类的思维“四舍五入”
5.4 “四舍五入”结果为：5，int(5.4+0.5) == 5
5.6 “四舍五入”结果为：6，int(5.6+0.5) == 6
'''

#1st solutioin
import re

def calculate_string(st):
    st = re.sub(r'[^-+*/\d.]', '', st)
    result = eval(st)
    return str(int(round(result)))

#2nd solution
def calculate_string(st: str) -> str:
    return f"{eval(''.join(s for s in st if s in '0123456789.+-/*')):.0f}"


import re
def calculate_string(st):
    return str(round(eval(re.sub(r'[^0-9\-\+\*\/\.]',"",st))))


def calculate_string(s):
    return str(round(eval("".join(c for c in s if c.isdigit() or c in ".+-*/"))))