'''
https://www.codewars.com/kata/52fb87703c1351ebd200081f/train/python

"1999" --> "20th"
"2011" --> "21st"
"2154" --> "22nd"
"2259" --> "23rd"
"1124" --> "12th"
"2000" --> "20th"
'''
#1st solution
def what_century(year):
    n = (int(year) - 1) // 100 + 1
    return str(n) + ("th" if n < 20 else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th"))
year = 2001
print(f"{year}", (int(year) - 1) // 100 + 1)

#2nd solution
def what_century(year):
    year = int(year)
    dict = {
        0:'th',
        1:'st',
        2:'nd',
        3:'rd',
        4:'th',
        5:'th',
        6:'th',
        7:'th',
        8:'th',
        9:'th'
    }
    postfix = ''
    century = year // 100 + (year % 100 > 0)
    if century % 100 // 10 == 1:
        postfix = 'th'
    else:
        postfix = dict[century % 10]
    return str(century) + postfix



centcn = ["第一，第二，第三，第四，第五，第六，第七，第八，第九，第十，第十一，第十二，第十三",
          "第十四，第十五，第十六，第十七，第十八，第十九，第二十，第二十一"]
centen = ['First', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth',
          'eleventh', 'twelfth', 'thirteenth', 'fourteenth', 'fifteenth', 'sixteenth', 'seventeenth',
          'eighteenth', 'nineteenth', 'twentieth','twenty-first']

centennum = [str(i) for i in range(1,21)]
print(centennum)
import math
import re
from num2words import num2words

def what_century(year):
    n = [i for i in range(10)]
    yString = {1: 'st', 2: 'nd', 3: 'rd', 4: 'th', 5: 'th', 6: 'th', 7: 'th', 8: 'th', 9: 'th', 10: 'th', 11: 'th', 12: 'th', 13: 'th', 14: 'th', 15: 'th', 16: 'th', 17: 'th', 18: 'th', 19: 'th', 20: 'th', 21: 'st', 22: 'nd', 23: 'rd', 24: 'th', 25: 'th', 26: 'th', 27: 'th', 28: 'th', 29: 'th', 30: 'th', 31: 'st', 32: 'nd', 33: 'rd', 34: 'th', 35: 'th', 36: 'th', 37: 'th', 38: 'th', 39: 'th', 40: 'th', 41: 'st', 42: 'nd', 43: 'rd', 44: 'th', 45: 'th', 46: 'th', 47: 'th', 48: 'th', 49: 'th', 50: 'th', 51: 'st', 52: 'nd', 53: 'rd', 54: 'th', 55: 'th', 56: 'th', 57: 'th', 58: 'th', 59: 'th', 60: 'th', 61: 'st', 62: 'nd', 63: 'rd', 64: 'th', 65: 'th', 66: 'th', 67: 'th', 68: 'th', 69: 'th', 70: 'th', 71: 'st', 72: 'nd', 73: 'rd', 74: 'th', 75: 'th', 76: 'th', 77: 'th', 78: 'th', 79: 'th', 80: 'th', 81: 'st', 82: 'nd', 83: 'rd', 84: 'th', 85: 'th', 86: 'th', 87: 'th', 88: 'th', 89: 'th', 90: 'th', 91: 'st', 92: 'nd', 93: 'rd', 94: 'th', 95: 'th', 96: 'th', 97: 'th', 98: 'th', 99: 'th', 100: 'th'}
    #nthString = dict([(num,num2words((num), ordinal=True)) for num in range(1,99)])
    cent = math.ceil(year/100)
    return f"{cent}{yString[cent][-2:]}"
year = 2000
print(what_century(year))
print([what_century(year) for year in (1124,1999,2000,2099,2501,2011,2259)])


def what_century(n):
    #num = [i for i in range(1,n)]
    nthString = dict([(num,num2words((num), ordinal=True)[-2:]) for num in range(1,n)])
    cent = math.ceil(year/100)
    return nthString
n = 101
print(what_century(n))
#print([what_century(year) for year in (1124,1999,2000,2099,2501,2011,2259)])


# Is there a python function to convert ordinal number to word
# https://stackoverflow.com/questions/56813864/is-there-a-python-function-to-convert-ordinal-number-to-word

import re
from num2words import num2words
ordinalAsNumber = "42nd"
number = re.search('\d+', ordinalAsNumber)
ordinalAsString = num2words(number[0], ordinal=True)
print( ordinalAsString ) # forty-second

'''
课后小任务
如何将2020年10月4日转换为字符串表达为
输入：2020年10月4日
输出：2020/10/4日
​
'''
ymd = '2020年10月4日'

def ymdAsnum(ymd):
    #ymd = [ymd.split(f"{i}") for i in ymd if not i.isdigit]
    ymd = [i if i.isdigit() else '/' for i in ymd ]
    return ''.join(ymd)
print(ymdAsnum(ymd))