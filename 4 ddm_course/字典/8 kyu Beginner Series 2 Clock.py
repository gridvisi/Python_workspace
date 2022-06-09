'''
https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a/train/python

Clock shows 'h' hours, 'm' minutes and 's' seconds after midnight.
Your task is to make 'Past' function which returns time converted to milliseconds.

Example:
past(0, 1, 1) == 61000
Input constraints: 0 <= h <= 23, 0 <= m <= 59, 0 <= s <= 59

FUNDAMENTALS
'''
h, m, s = 0, 1, 1
def past(h, m, s):
    ms = {'h':h*60*60*1000,'m':m*60*1000,'s':s*1000}
    return ms['h'] + ms['m'] + ms['s']
print(past(h,m,s))

#1st solution
def past(h, m, s):
    return (3600*h + 60*m + s) * 1000

#2nd solution
def past(h, m, s):
    return (s + (m + h * 60) * 60) * 1000