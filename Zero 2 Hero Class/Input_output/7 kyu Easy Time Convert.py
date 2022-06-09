'''
https://www.codewars.com/kata/5a084a098ba9146690000969/train/python

test.assert_equals(time_convert(0), '00:00', 'Test at 0')
test.assert_equals(time_convert(-6), '00:00', 'Negative number')
test.assert_equals(time_convert(8), '00:08', '8 minutes')
test.assert_equals(time_convert(32), '00:32', '32 minutes')
test.assert_equals(time_convert(75), '01:15', 'over an hour')
test.assert_equals(time_convert(63), '01:03', 'over an hour')
test.assert_equals(time_convert(134), '02:14', 'over two hours')
test.assert_equals(time_convert(180), '03:00', 'three hours')
test.assert_equals(time_convert(970), '16:10', 'over 16 hours')
test.assert_equals(time_convert(565757), '9429:17', 'big numbers')
'''

def time_convert(num):
    return f"{num//60:02d}:{num%60:02d}"

num = 565757
print(time_convert(num))

#1st
def timeConvert(m):
    return '{:02d}:{:02d}'.format(*divmod(max(int(m), 0), 60))

