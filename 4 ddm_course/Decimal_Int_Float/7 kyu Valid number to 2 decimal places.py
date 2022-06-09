'''
https://www.codewars.com/kata/55f9064161541a9e01000001/train/python

检查一个数字是否是一个有效的数字，该数字已被赋予小数点后2位。传递给该函数的数字将以字符串形式给出。如果该数字满足以下标准，该函数应返回真，否则应返回假。

请检查有效数字的标准。前面有可选的+或-符号

小数点前的可选数字（数字是指从'0'到'9'的字符）。

一个小数点

小数点后正好是两个数字没有别的
Examples of valid and non-valid numbers

List of valid numbers: [ "0.00" "3.90" "1000.00" ".00" "-2.55" "+2.10" "-.55"]

List of non-valid numbers: ["hellow 11.99" "11.9" "11" "11." ".9"]
'''

import re

def valid_number(input_str):
    return re.match(r"""
        [+-]?   # optional +/- sign
        \d*     # optional digits
        \.      # decimal point
        \d\d    # two digits
        $       # end of string
        """, input_str, re.VERBOSE) is not None

import re
def valid_number(n):
    return bool(re.fullmatch(r'^[-+]?\d*\.\d{2}$', n))


def valid_number(n):
    if '.' not in n or len(n.split('.')[1])!=2 : return False
    try: eval(n)
    except: return False
    return True


def valid_number(n):
    if n[-3] == '.':
        if n.count('.') > 1:
            return False

        for i in n:
            if i.isalpha():
                return False
        return True
    else:
        return False