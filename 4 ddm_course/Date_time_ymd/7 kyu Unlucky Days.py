'''
https://www.codewars.com/kata/56eb0be52caf798c630013c0/train/python

13号星期五或黑色星期五被认为是不吉利的日子。计算在给定的一年中，有多少个不吉利的日子。
找出给定年份中13号星期五的数量。

输入。年是一个整数。
输出：一年中黑色星期五的数量。一年中黑色星期五的数量作为一个整数。
例子：在一年中，黑色星期五的数量是整数。

test.describe("Example Tests")
test.assert_equals(unlucky_days(2015), 3)
test.assert_equals(unlucky_days(1986), 1)

'''
import datetime
import time
def unlucky_days(year):
    ans = []
    for month in range(1,13):
        date = datetime.date(year,month,13)
        weekday = datetime.datetime.isoweekday(date)
        if weekday == 5:
            ans.append(date)
    return len(ans)
year = 2015
print(unlucky_days(year))


#1st solution
from datetime import date

def unlucky_days(year):
    return sum(date(year, m, 13).weekday() == 4 for m in range(1, 13))