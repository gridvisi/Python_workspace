'''
https://www.codewars.com/kata/55c933c115a8c426ac000082/train/python

Switch/Case - Bug Fixing #6
Oh no! Timmy's evalObject function doesn't work. He uses Switch/Cases to evaluate the
given properties of an object, can you fix timmy's function?

BUGSCASE/SWITCH STATEMENTSCONDITIONAL STATEMENTSCONTROL FLOWBASIC LANGUAGE
FEATURESFUNDAMENTALS

Test.assert_equals(eval_object({'a':1,'b':1,'operation':'+'}), 2, 'Return the evaluated string as a number!')
Test.assert_equals(eval_object({'a':1,'b':1,'operation':'-'}), 0, 'Return the evaluated string as a number!')
Test.assert_equals(eval_object({'a':1,'b':1,'operation':'/'}), 1, 'Return the evaluated string as a number!')
Test.assert_equals(eval_object({'a':1,'b':1,'operation':'*'}), 1, 'Return the evaluated string as a number!')
Test.assert_equals(eval_object({'a':1,'b':1,'operation':'%'}), 0, 'Return the evaluated string as a number!')
Test.assert_equals(eval_object({'a':1,'b':1,'operation':'**'}), 1, 'Return the evaluated string as a number!')
'''
#10th solve by ericlee
v = {'a':1,'b':1,'operation':'+'}
def eval_object(v):
    rule = {"+": v['a'] + v['b'],
     "-": v['a'] - v['b'],
     "/": v['a'] / v['b'],
     "*": v['a'] * v['b'],
     "%": v['a'] % v['b'],
     "**": v['a'] ** v['b'], }  #.get('operation', 1)
    return rule[v["operation"]]
print(eval_object(v))

#1st
def eval_object(v):
    return {"+": v['a']+v['b'],
            "-": v['a']-v['b'],
            "/": v['a']/v['b'],
            "*": v['a']*v['b'],
            "%": v['a']%v['b'],
           "**": v['a']**v['b'], }.get(v['operation'])

#2nd
def eval_object(v):
    return eval("{a}{operation}{b}".format(**v))

#3rd
import operator

OP_FUNCS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.div,
    '%': operator.mod,
    '**': operator.pow,
}

def eval_object(o):
    f = OP_FUNCS.get(o['operation'])
    return f(o['a'], o['b']) if f else 0

#4th
def eval_object(v):

    return {"+": v['a']+v['b'],
        "-": v['a']-v['b'],
        "/": v['a']/v['b'],
        "*": v['a']*v['b'],
        "%": v['a']%v['b'],
        "**": v['a']**v['b'], }.get(eval('operation',v))

#5th
def eval_object(v):
    return {
        "+" : v['a'] +  v['b'],
        "-" : v['a'] -  v['b'],
        "/" : v['a'] /  v['b'],
        "*" : v['a'] *  v['b'],
        "%" : v['a'] %  v['b'],
        "**": v['a'] ** v['b'],
    }.get(v['operation'])

#6th
from operator import add, sub, truediv, mul, mod, pow
ops = {'+':add, '-':sub, '/':truediv, '*':mul, '%':mod, '**':pow}
one = lambda a,b: 1

def eval_object(v):
    return ops.get(v['operation'], one)(v['a'], v['b'])

#7th
from typing import Dict, Union

def eval_object(v: Dict[str, Union[str, int]]) -> int:
    """ Make a math operation based on `v` object. """
    return {
        "+": v["a"] + v["b"],
        "-": v["a"] - v["b"],
        "/": v["a"] / v["b"],
        "*": v["a"] * v["b"],
        "%": v["a"] % v["b"],
        "**": v["a"] ** v["b"]
    }.get(v["operation"], 1)