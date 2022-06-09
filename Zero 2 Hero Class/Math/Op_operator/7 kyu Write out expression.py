'''
https://www.codewars.com/kata/57e2afb6e108c01da000026e/train/python

Math hasn't always been your best subject, and these programming symbols always trip you up!

I mean, does ** mean *"Times, Times"* or *"To the power of"*?

Luckily, you can create a function to write out the expressions for you!

The operators you'll need to use are:

{ '+':   'Plus ',
  '-':   'Minus ',
  '*':   'Times ',
  '/':   'Divided By ',
  '**':  'To The Power Of ',
  '=':   'Equals ',
  '!=':  'Does Not Equal ' }
These values will be stored in the preloaded dictionary OPERATORS just as shown above.

But keep in mind: INVALID operators will also be tested, to which you should return "That's not an operator!"

And all of the numbers will be 1 to10! Isn't that nice!

Here's a few examples to clarify:

expression_out("4 ** 9") == "Four To The Power Of Nine"
expression_out("10 - 5") == "Ten Minus Five"
expression_out("2 = 2")  == "Two Equals Two"
Good luck!

FUNDAMENTALSBASIC LANGUAGE FEATURES

test.assert_equals(expression_out('1 + 3'),  'One Plus Three')
test.assert_equals(expression_out('2 - 10'), 'Two Minus Ten')
test.assert_equals(expression_out('6 ** 9'), 'Six To The Power Of Nine')
test.assert_equals(expression_out('5 = 5'),  'Five Equals Five')
test.assert_equals(expression_out('7 * 4'),  'Seven Times Four')
test.assert_equals(expression_out('2 / 2'),  'Two Divided By Two')
test.assert_equals(expression_out('8 != 5'), 'Eight Does Not Equal Five')
'''
import num2word
print(num2word.word(13242134))

num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', \
            19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', \
            50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', \
            90: 'Ninety', 0: 'Zero'}



def expression_out(exp):
    num2word = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
                 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten'}

    op = { '+':   ' Plus ',
            '-':   ' Minus ',
            '*':   ' Times ',
            '/':   ' Divided By ',
            '**':  ' To The Power Of ',
            '=':   ' Equals ',
            '!=':  ' Does Not Equal ' }
    x = exp.split(" ")
    if x[1] in op:return num2word[int(x[0])] + op.get(x[1]) + num2word[int(x[2])]
    return "That's not an operator!"

exp = '8 != 5'  #'Eight Does Not Equal Five'
print(expression_out(exp))

#1st
import operator
l = ['0','One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
def expression_out(exp):
    try:
        return l[int(exp.split()[0])] +" "+ OPERATORS[exp.split()[1]] + l[int(exp.split()[2])]
    except KeyError:
        return "That's not an operator!"

#3
sign = {'0':'Zero', '1':'One', '2':'Two', '3':'Three', '4':'Four', '5':'Five', '6':'Six', '7':'Seven', '8':'Eight', '9':'Nine', '10':'Ten',
    '+':   'Plus',
    '-':   'Minus',
    '*':   'Times',
    '/':   'Divided By',
    '**':  'To The Power Of',
    '=':   'Equals',
    '!=':  'Does Not Equal'}

def expression_out(exp):
    exp = exp.split()
    try:
        assert not exp[1].isdigit()
        return ' '.join(sign[i] for i in exp)
    except:
        return "That's not an operator!"


#7th
import operator
def expression_out(exp):
    NUMS = {
        '1': 'One',
        '2': 'Two',
        '3': 'Three',
        '4': 'Four',
        '5': 'Five',
        '6': 'Six',
        '7': 'Seven',
        '8': 'Eight',
        '9': 'Nine',
        '10': 'Ten'
    }

    (n1, op, n2) = exp.split()
    return f'{NUMS[n1]} {OPERATORS[op]}{NUMS[n2]}' if op in OPERATORS else "That's not an operator!"

units = ['','one','two','three','four','five','six','seven','eight','nine']
teens = ['','eleven','twelve','thirteen','fourteen','fifteen','sixteen', \
             'seventeen','eighteen','nineteen']
tens = ['','ten','twenty','thirty','forty','fifty','sixty','seventy', \
            'eighty','ninety']
thousands = ['','thousand','million','billion','trillion','quadrillion', \
                 'quintillion','sextillion','septillion','octillion', \
                 'nonillion','decillion','undecillion','duodecillion', \
                 'tredecillion','quattuordecillion','sexdecillion', \
                 'septendecillion','octodecillion','novemdecillion', \
                 'vigintillion']

import math
number = int(input("Enter number to print: "))
number_list = ["zero","one","two","three","four","five","six","seven","eight","nine"]
if number <= 9:
    print(number_list[number].capitalize())

