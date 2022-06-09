'''
https://www.codewars.com/kata/number-of-measurements-to-spot-the-counterfeit-coin/train/python
'''
def how_many_measurements(n,step = 0):
    if n == 1: return 0
    if n == 2: return step+1
    if n == 3: return step+1
    if n > 3:
        if n % 3 == 0:
            step += 1
            return how_many_measurements(n // 3, step)
        elif n % 3 != 0:
            step += 1
        return how_many_measurements(n//3+1,step)
n = 100000
print(how_many_measurements(n,step = 0))

from math import ceil, log
def how_many_measurements(n):
    return ceil(log(n, 3))

def how_many_measurements(n):
  if n>1:
      return 1 + how_many_measurements(n/3)
  return 0

import math
def how_many_measurements(n):
    return math.ceil(math.log(n, 3))

def how_many_measurements(n):
    # Split coins in three equal sized groups,
    # one measurement will tell which of the groups contains
    # the fake coin, when less than 3 coins is in a group, one
    # measurement is required to determine which coin is fake
    if n == 1:
      return 0
    elif n <= 3:
        return 1
    n_coins_in_sub_group = n / 3
    return how_many_measurements(n_coins_in_sub_group) + 1