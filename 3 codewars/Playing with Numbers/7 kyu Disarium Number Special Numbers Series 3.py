'''
https://www.codewars.com/kata/5a53a17bfd56cb9c14000003/train/python
'''

def disarium_number(number):
    disarium = [int(e)**(i+1) for i,e in enumerate(str(number))]

    return "Disarium !!" if sum(disarium) == number else "Not !!"


def disarium_number(n):
    return "Disarium !!" if n == sum(int(d)**i for i, d in enumerate(str(n), 1)) else "Not !!"


from math import log


# trying to avoid string solution

def disarium_number(number):
    def f(x):
        y = log(x, 10) // 1 + 1
        return x ** y if x < 10 else (x % 10) ** y + f(x // 10)

    return "Disarium !!" if not number or f(number) == number else "Not !!"