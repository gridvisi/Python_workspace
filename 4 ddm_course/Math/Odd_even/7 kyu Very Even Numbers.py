'''
https://www.codewars.com/kata/58c9322bedb4235468000019/train/python

input(88) => returns false -> 8 + 8 = 16 -> 1 + 6 = 7 => 7 is odd

input(222) => returns true

input(5) => returns false

input(841) => returns true -> 8 + 4 + 1 = 13 -> 1 + 3 => 4 is even
'''
#19th solution by ericlee
def is_very_even_number(n):
    if len(n) == 1:return eval(n)%2 == 0
    n = sum([eval(i) for i in str(n)])
    return is_very_even_number(n)


#1st solution
def is_very_even_number(n):
    while len(str(n)) > 1:
        n = sum(int(x) for x in str(n))
    return True if n % 2 == 0 else False

#2nd solution
def is_very_even_number(n):
    return n == 0 or (n - 1) % 9 % 2


def is_very_even_number(n):
    if n < 10:
        return n % 2 == 0
    return is_very_even_number(sum(int(d) for d in str(n)))

def is_very_even_number(n):
    while n >= 10:
        n = sum(map(int, str(n)))
    return n % 2 == 0



