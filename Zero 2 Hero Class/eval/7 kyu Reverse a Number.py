'''
https://www.codewars.com/kata/555bfd6f9f9f52680f0000c5/train/python

Test.assert_equals(reverse_number(123), 321)
Test.assert_equals(reverse_number(-123), -321, 'Negative Numbers should be preserved')
Test.assert_equals(reverse_number(1000), 1)
Test.assert_equals(reverse_number(4321234), 4321234)
Test.assert_equals(reverse_number(5), 5)
Test.assert_equals(reverse_number(0), 0)
Test.assert_equals(reverse_number(98989898), 89898989)
'''
n = 1000
print(str(n)[:0:-1],str(n)[::-1])

def reverse_number(n):
    if n == 0:return 0
    ans = 0
    while True:
        if n % 10 == 0:
            n = n//10
        else:
        #break
            ns = int(str(n)[::-1]) if n > 0 else -int(str(n)[:0:-1])
            print(ns)
            return ns
n = -1000
n = 1300
n = 0
n = 5
print(reverse_number(n))

#1st
def reverseNumber(n):
    if n < 0: return -reverseNumber(-n)
    return int(str(n)[::-1])

#2nd
def reverseNumber(n):
    return int(str(abs(n))[::-1]) * (-1 if n < 0 else 1)

#3rd
def reverseNumber(n):
    if n >= 0:
        return int(str(n)[::-1])
    else:
        return int(str(n).strip('-')[::-1])*-1

#4th
def reverse_number(n):
    return int(str(abs(n))[::-1]) * (-1)**(n<0)
print(int('0001'))