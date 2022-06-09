'''
https://www.codewars.com/kata/strongn-strong-number-special-numbers-series-number-2/train/python
Definition Strong number is the number that the sum of the factorial of its digits is equal to number itself.
For example : 145 , since
1! + 4! + 5! = 1 + 24 + 120 = 145
So, 145 is a Strong number.
Task Given a number, Find if it is Strong or not .
'''
number = 2
def strong_num(number):
    s = 0
    nls = list(str(number))
    for i in nls:
        t = 1
        for j in range(1,int(i)+1):
            t *= j
        s += t
    if s == number:
        return 'STRONG!!!!'
    return 'Not Strong !!'
print(strong_num(number))