'''
https://www.codewars.com/kata/57e2afb6e108c01da000026e/train/python
test.assert_equals(expression_out('1 + 3'),  'One Plus Three')
test.assert_equals(expression_out('2 - 10'), 'Two Minus Ten')
test.assert_equals(expression_out('6 ** 9'), 'Six To The Power Of Nine')
test.assert_equals(expression_out('5 = 5'),  'Five Equals Five')
test.assert_equals(expression_out('7 * 4'),  'Seven Times Four')
test.assert_equals(expression_out('2 / 2'),  'Two Divided By Two')
test.assert_equals(expression_out('8 != 5'), 'Eight Does Not Equal Five')
'''
print('cool think: ',int('7 '),type(int('7 ')),int('7 ')+3)

import re
from num2words import num2words

def expression_out(exp):
    #op = ['**','+','-*','/','=','!=']
    opword = {'+': ' Plus ',
          '-': ' Minus ',
          '*': ' Times ',
          '/': ' Divided By ',
          '**': ' To The Power Of ',
          '=': ' Equals ',
          '!=': ' Does Not Equal '}
    op = [k for k in opword]
    op = ['**','+','-*','/','=','!=']
    print(op)
    #key = [exp.rfind(i) for i in op]
    #key = [exp.replace(x,'') for x in op if x.isdigit]
    #key = [i for i in exp if i not in op]
    #key = [exp.index(i) for i in exp if i in op]
    #print('key:',key)
    for i in op:
        if i in exp:

            ansAsNum = [int(i) for i in exp.split(f"{i}")]
            #ansAsString = [i if i not in op else opword.get([i],None) for i in ansAsNum]
            print(ansAsNum,i)
            #number = re.search('\d+', ordinalAsNumber)
            ordinalAsStr = num2words(ansAsNum[0], ordinal=True) + opword[i] + num2words(ansAsNum[1], ordinal=True)
    return ordinalAsStr # ansAsNum,
exp = '6 ** 9'
print(expression_out(exp))


def num2word(x):
    num = [str(i) for i in range(1,22)]
    #numAstr = ['First', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth',
    #      'eleventh', 'twelfth', 'thirteenth', 'fourteenth', 'fifteenth', 'sixteenth', 'seventeenth',
    #     'eighteenth', 'nineteenth', 'twentieth','twenty-first']

    numAstr = [
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
            ]

    return dict(zip(num,numAstr))[str(x)]
x = 1
print(f"{x}",num2word(x))

# version upload to Codewars

def expression_out(exp):
    opword = {'+': ' Plus ',
          '-': ' Minus ',
          '*': ' Times ',
          '/': ' Divided By ',
          '**': ' To The Power Of ',
          '=': ' Equals ',
          '!=': ' Does Not Equal '}

    op = ['!=','**','+','-','*','/','=']
    ordinalAsStr = 0
    for i in op:
        if i in exp:
            ansAsNum = [i for i in exp.split(f"{' '}{i}{' '}")]
            print('ansAsNum:',exp.split(f"{' '}{i}{' '}"),ansAsNum,i)
            # ValueError: invalid literal for int() with base 10: ''
            ordinalAsStr = num2word(ansAsNum[0]) + opword[i] + num2word(ansAsNum[1])
            break
    return "That's not an operator!" if ordinalAsStr == 0 else ordinalAsStr

exp = '7 != 8'
exp = '2 - 10'
print('ans:',expression_out(exp))


#1st solution
OPERATORS = {'+': ' Plus ',
          '-': ' Minus ',
          '*': ' Times ',
          '/': ' Divided By ',
          '**': ' To The Power Of ',
          '=': ' Equals ',
          '!=': ' Does Not Equal '}

l = ['0','One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
def expression_out(exp):
    try:
        return l[int(exp.split()[0])] +" "+ OPERATORS[exp.split()[1]] + l[int(exp.split()[2])]
    except KeyError:
        return "That's not an operator!"

NUMBERS = 'Zero One Two Three Four Five Six Seven Eight Nine Ten'.split()

def expression_out(exp):
    x, op, y = exp.split()
    x, y = NUMBERS[int(x)], NUMBERS[int(y)]
    op = OPERATORS.get(op, "That's not an operator!")
    return '%s %s%s' % (x, op, y) if op[-1] != '!' else op

exp = '8 - 10'
x, op, y = exp.split()
print('x, op, y:',x, op, y)
print(NUMBERS[int(x)], NUMBERS[int(y)])
print(NUMBERS[int(x)], NUMBERS[int(y)])
num = 10
print(f"{NUMBERS[int(num)]}")

#3rd solution
NUMBERS = {
    '1': "One", '2': "Two", '3': "Three", '4': "Four", '5': "Five",
    '6': "Six", '7': "Seven", '8': "Eight", '9': "Nine", '10': "Ten"
}


def expression_out(exp: str) -> str:
    v1, op, v2 = exp.split()
    try:
        return f"{NUMBERS[v1]} {OPERATORS[op]}{NUMBERS[v2]}"
    except KeyError:
        return "That's not an operator!"

#4th solution
DIGITS = "zero one two three four five six seven eight nine ten".title().split()
def expression_out(exp):
    opr1, op, opr2 = exp.split()
    if op not in OPERATORS:
        return "That's not an operator!"
    return f"{DIGITS[int(opr1)]} {OPERATORS[op]}{DIGITS[int(opr2)]}"

#5th solution
import re
def expression_out(exp):
    dict = {
        '1': 'One',
        '2': 'Two',
        '3': 'Three',
        '4': 'Four',
        '5': 'Five',
        '6': 'Six',
        '7': 'Seven',
        '8': 'Eight',
        '9': 'Nine',
        '10': 'Ten',
        '+': 'Plus',
        '-': 'Minus',
        '*': 'Times',
        '/': 'Divided By',
        '**': 'To The Power Of',
        '=': 'Equals',
        '!=': 'Does Not Equal'
    }
    def rp(x):
        return dict[x.group(0)]
    return re.sub('([0-9\+\-\*/!=]+|)', rp, exp) if re.match('^[0-9]+ [\+\-\*/!=]+ [0-9]+$', exp) else 'That\'s not an operator!'

'''

def expression_out(exp):
    opword = {'+': ' Plus ',
          '-': ' Minus ',
          '*': ' Times ',
          '/': ' Divided By ',
          '**': ' To The Power Of ',
          '=': ' Equals ',
          '!=': ' Does Not Equal '}

    op = ['**','+','-*','/','=','!=']  
    for i in op:
        if i in exp:
            ansAsNum = exp.split(f"{i}")
            ordinalAsStr = num2words(ansAsNum[0], ordinal=True) + opword[i] + num2words(ansAsNum[1], ordinal=True)
    return ordinalAsStr 
    

def num2words(x):
    bit = {3:'hundred',4:'thousand',7:'million',
           10:'billion',13:'trillionth'}

    #nAsword = str(n) + ("th" if n < 20 else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return


def expression_out(exp):
    op = {'+': 'Plus ',
          '-': 'Minus ',
          '*': 'Times ',
          '/': 'Divided By ',
          '**': 'To The Power Of ',
          '=': 'Equals ',
          '!=': 'Does Not Equal '}

    return exp + exp

'''