'''
https://www.codewars.com/kata/546ba103f0cf8f7982000df4/train/python
Test.assert_equals(calculate('1', '1', 'add'), '10')
Test.assert_equals(calculate('1', '1', 'subtract'), '0')
Test.assert_equals(calculate('1', '1', 'multiply'), '1')
'''

n1,n2,o ='11', '111', 'subtract' # '10'
def calculate(n1, n2, o):
    if o == 'add':
        return bin(int(('0b'+n1),2)+int(('0b'+n2),2))[2:]
    elif o == 'subtract':
        if bin(int(('0b'+n1),2)-int(('0b'+n2),2))[0] == '-':
            return '-'+bin(int(('0b'+n1),2)-int(('0b'+n2),2))[3:]
        else:return bin(int(('0b'+n1),2)-int(('0b'+n2),2))[2:]
    elif o == 'multiply':
        print(int(n1)*int(n2),int(('0b'+n1),2),int(n2))
        return bin(int(('0b'+n1),2)*int(('0b'+n2),2))[2:]

from operator import mul,add,sub
operators = {'add':add, 'subtract':sub, 'multiply':mul }

def calculate(n1, n2, o):
    return '{:b}'.format(operators[o](int(n1,2), int(n2,2)))
print('sd',calculate(n1, n2, o))


from operator import *
def calculate(n1, n2, o):
    result = eval(o[:3])(int(n1, 2), int(n2, 2))
    return (bin(result)[2:], bin(result)[0] + bin(result)[3:])[result < 0]
print(calculate(n1, n2, o))
import operator
def calculate(n1, n2, o):
    calc = {
        'add':operator.add((int(n1, base=2)),(int(n2, base=2))),
        'subtract':operator.sub((int(n1, base=2)),(int(n2, base=2))),
        'multiply':operator.mul((int(n1, base=2)),(int(n2, base=2))) }
    return '{:b}'.format(calc[o])

from operator import add, sub, mul
# a = float(raw_input("Input the first number:"))
# b = float(raw_input("Input the second number:"))
operator = {'+': add, '-': sub, '*': mul}  #'/':div

def Input(a, o, b):
   return "%s%s%s=%s" % (a, o, b, operator.get(o)(a, b))

Input(25, "+", 56)
Input(86, "-", 68)
Input(50, "*", 60)
Input(99, "/", 25)
