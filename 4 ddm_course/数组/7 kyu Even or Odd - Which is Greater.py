'''
https://www.codewars.com/kata/57f7b8271e3d9283300000b4/train/python

Given a string of digits confirm whether the sum of all the individual even digits are
greater than the sum of all the indiviudal odd digits. Always a string of numbers will
be given.

If the sum of even numbers is greater than the odd numbers return: "Even is greater
than Odd"

If the sum of odd numbers is greater than the sum of even numbers return: "Odd is greater
than Even"

If the total of both even and odd numbers are identical return: "Even and Odd are the same"


'''

def even_or_odd(s):
    odds = [int(i) for i in s if eval(i)%2]
    evens = [int(i) for i in s if not eval(i)%2]
    if sum(odds) > sum(evens):return 'Odd is greater than Even'
    elif sum(odds) < sum(evens):return 'Even is greater than Odd'
    else: return 'Even and Odd are the same'

#1st solution
def even_or_odd(s):
    n=sum(x * (-1 if x % 2 else 1) for x in map(int,s))
    return 'Even is greater than Odd' if n > 0 else \
           'Odd is greater than Even' if n < 0 else \
           'Even and Odd are the same'