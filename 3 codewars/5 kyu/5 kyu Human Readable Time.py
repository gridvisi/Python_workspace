'''
https://www.codewars.com/kata/human-readable-time/solutions/python

Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
Test.assert_equals(make_readable(0), "00:00:00")
Test.assert_equals(make_readable(5), "00:00:05")
Test.assert_equals(make_readable(60), "00:01:00")
Test.assert_equals(make_readable(86399), "23:59:59")
Test.assert_equals(make_readable(359999), "99:59:59")
ALGORITHMSDATES/TIMEMATHEMATICSNUMBERS
'''

def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)

def make_readable(seconds):
    hours, seconds = divmod(seconds, 60 ** 2)
    minutes, seconds = divmod(seconds, 60)
    return '{:02}:{:02}:{:02}'.format(hours, minutes, seconds)

def make_readable(seconds):
    return "{0:02d}:{1:02d}:{2:02d}".format(seconds / 3600, seconds / 60 % 60, seconds % 60)

def make_readable(seconds):
    h = 0
    m = 0
    s = 0
    output = []
    while seconds:
        s += 1
        if s == 60:
            s = 0
            m += 1
        if m == 60:
            m = 0
            h += 1
        seconds -= 1
    if int(h / 10) == 0:
        h = '0'+str(h)+':'
    else:
        h = str(h)+':'
    if int(m /10) == 0:
        m = '0' + str(m) + ':'
    else:
        m = str(m) + ':'
    if int(s /10) == 0:
        s = '0' + str(s)
    else:
        s = str(s)
    output = [h,m,s]
    output = ''.join(output)
    return output