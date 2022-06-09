'''
https://stackoverflow.com/questions/40631553/python-3-decimal-rounding-half-down-with-round-half-up-context
'''


#https://stackoverflow.com/questions/49785753/how-to-properly-round-half-down-a-decimal-number?r=SearchResults
import sys, signal, json, time
import random
import decimal
from decimal import Decimal, ROUND_HALF_DOWN
num = 0.049852124
num = Decimal(num)
numCoins = Decimal(num.quantize(Decimal('0.001'), rounding=ROUND_HALF_DOWN))
numCoins = float(numCoins)
print('test_1:',numCoins)

import decimal

context = decimal.getcontext()
context.rounding = decimal.ROUND_HALF_UP
round(decimal.Decimal('2.5'))
2
decimal.Decimal('2.5').__round__()
2
decimal.Decimal('2.5').quantize(decimal.Decimal('1'), rounding=decimal.ROUND_HALF_UP)

#decimal('3')

decimal('2.5').__round__()
2
decimal('2.5').__round__(0)
#decimal('3')