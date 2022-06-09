'''
https://www.codewars.com/kata/590ac6b9be4dff49b0000042/train/python


'''
import fractions

for v in [0.1, 0.5, 1.5, 2.0]:
    print('{} = {}'.format(v, fractions.Fraction(v)),2)

print(0.0001398888888888889 * 3600)


def convert(degrees):
    s = degrees * 3600
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)



import math
def convert(degrees):
    # your code here
    degree = math.floor(degrees)
    m = (degrees - degree)*3600//60
    s = round(degrees * 3600 - degree*3600 - m*60%60)
    return [degree,m,s]


def convert(degrees):
    s = degrees * 3600

    if round(s % 60) == 0 and int(s / 60 % 60) == 0:
        return [int(s / 3600)]

    elif round(s % 60) == 0:
        return [int(s / 3600), int(s / 60 % 60)]

    return [int(s / 3600), int(s / 60 % 60), round(s % 60)]

degrees = 0.0001398888888888889
degrees = 91.33333333333333
print(convert(degrees))

#1st
def convert(degrees):
    result = [int(degrees), int(degrees * 60 % 60), round(degrees * 3600 % 60)]
    return result if result[2] else result[:2] if result[1] else result[:1]

def convert(d):
    s=round(d*3600)
    m,s=divmod(s,60)
    d,m=divmod(m,60)
    if s: return [d,m,s]
    if m: return [d,m]
    return [d]

#一个地球年，大约365.24219天


def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)

def make_readable(seconds):
    hours, seconds = divmod(seconds, 60 ** 2)
    minutes, seconds = divmod(seconds, 60)
    return '{:02}:{:02}:{:02}'.format(hours, minutes, seconds)
