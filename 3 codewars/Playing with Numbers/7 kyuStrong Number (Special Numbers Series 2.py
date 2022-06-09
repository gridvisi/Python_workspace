'''
https://www.codewars.com/kata/5a4d303f880385399b000001/train/python
'''

def factor(n):
    s = 1
    for i in range(1,n+1):
        s *= i
    return s

def strong_num(number):
    total = 0
    for i in str(number):
        total += factor(int(i))
    return "STRONG!!!!" if total == number else "Not Strong !!"


#1st
import math

def strong_num(number):
    return "STRONG!!!!" if sum(math.factorial(int(i)) for i in str(number)) == number else "Not Strong !!"


from math import factorial
def strong_num(number):
  return ("Not Strong !!", "STRONG!!!!")[sum(factorial(int(i)) for i in str(number)) == number]



def strong_num(number):
    result = []
    for i in str(number):
        fact = 1
        for j in range(1, int(i) + 1):
            fact = fact * j
        result.append(fact)
    return "STRONG!!!!" if sum(result) == number else "Not Strong !!"


from numpy import prod
def strong_num(n):
    return ["Not Strong !!", "STRONG!!!!"][ sum(prod(range(1,i+1)) for i in map(int, str(n)))==n]