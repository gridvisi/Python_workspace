'''
https://www.codewars.com/kata/55fab1ffda3e2e44f00000c6/train/python
蟑螂是速度最快的昆虫之一。写一个函数，把它的速度以公里/小时为单位，以厘米/秒为单位返回，四舍五入到整数（=浮动）。

例如蟑螂的速度(1. 08) ==30
注意！输入的是实数（实际类型取决于语言），并且是>=0。输入是一个实数（实际类型取决于语言），并且是>=0。
结果应该是一个整数。

The cockroach is one of the fastest insects. Write a function which takes its speed
in km per hour and returns it in cm per second, rounded down to the integer (= floored).

For example:

cockroach_speed(1.08) == 30
Note! The input is a Real number (actual type is language dependent) and is >= 0.
The result should be an Integer.
'''
import math
def cockroach_speed(s): #公里/小时为单位，以厘米/秒为单位返回

    return math.floor(s * 10**5 / 3600)

#1st
def cockroach_speed(s):
    return s // 0.036

#2nd
def cockroach_speed(s):
    cm_per_km = 100000
    sec_per_hour = 3600
    return int(s * cm_per_km / sec_per_hour)

#3rd
def cockroach_speed(s):
    return (s * 100000) // (60 * 60)