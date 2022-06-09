'''
https://www.codewars.com/kata/564d0490e96393fc5c000029/train/python

The function takes cents value (int) and needs to return the minimum number of coins combination of the same value.

The function should return an array where
coins[0] = pennies ==> $00.01
coins[1] = nickels ==> $00.05
coins[2] = dimes ==> $00.10
coins[3] = quarters ==> $00.25

So for example:
coinCombo(6) --> [1, 1, 0, 0]

import codewars_test as test

@test.describe('Coin Combo')
def fixed_tests():
    @test.it('takes 1 and returns, 1 Penny.')
    def basic_test1():
        test.assert_equals(coin_combo(1),[1, 0, 0, 0])

    @test.it('takes 6 and returns, 1 Penny, 1 Nickle.')
    def basic_test2():
        test.assert_equals(coin_combo(6),[1, 1, 0, 0])

    @test.it('takes 11 and returns, 1 Dime, 1 Penny.')
    def basic_test3():
        test.assert_equals(coin_combo(11),[1, 0, 1, 0])
'''

#17 by ericlee
def coin_combo(cents):
    unit = [1,5,10,25]
    coin = dict(zip(unit,[0,0,0,0]))
    for v in unit[::-1]:
        if cents // v:
            coin[v] += cents // v
            cents = cents % v
    return [i for i in coin.values()]
cents = 6
print(coin_combo(cents))

#1st solution
def coin_combo(cents):
    return [cents%5, ((cents%25)%10)//5, (cents%25)//10, cents//25]

#2nd solution
def coin_combo(cents):
    coins = [1, 5, 10, 25]
    for i in range(3,-1,-1):
        coins[i], cents = divmod(cents, coins[i])
    return coins


def coin_combo(cents):
    q, cents = divmod(cents, 25)
    d, cents = divmod(cents, 10)
    n, p = divmod(cents, 5)
    return [p, n, d, q]

coins = [25, 10, 5, 1]

def coin_combo(cents):
    result = []
    for coin in coins:
        qty, cents = divmod(cents, coin)
        result.append(qty)
    return result[::-1]