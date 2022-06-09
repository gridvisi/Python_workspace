'''
https://www.codewars.com/kata/58f174ed7e9b1f32b40000ec/train/python

ou're a buyer/seller and your buisness is at stake... You need to make profit...
Or at least, you need to lose the least amount of money! Knowing a list of prices
for buy/sell operations, you need to pick two of them.
Buy/sell market is evolving across time and the list represent this evolution.
First, you need to buy one item, then sell it later.
Find the best profit you can do.

Example:
Given an array of prices [3, 10, 8, 4], the best profit you could make would
be 7 because you buy at 3 first, then sell at 10.

Input:
A list of prices (integers), of length 2 or more.

Output:
The result of the best buy/sell operation, as an integer.
'''
from collections import *
from pythonds.basic import Stack
prices = [3, 10, 8, 4]

def max_profit(prices):
    d = Stack()
    maxP = 0
    for i in prices:
        d.push(i)

    return d.peek()
print(max_profit(prices))



def max_profit(prices):
    d = 0
    maxP = 0
    while d < len(prices)-1:
        if max(prices[d+1:]) - prices[d] > maxP:
            maxP = max(prices[d+1:]) - prices[d]
        d += 1
    return maxP
'''
Execution Timed Out
 STDERR  Execution Timed Out (12000 ms)
'''
def max_profit(prices):
    m = best = float('-inf')
    for v in reversed(prices):
        m, best = max(m, best-v), max(best,v)
    return m


def max_profit(prices):
    out = prices[1] - prices[0]
    min_price = prices[0]

    for i in prices[1:]:
        if i - min_price > out:
            out = i - min_price
        if i < min_price:
            min_price = i
    return out
'''

def max_profit(prices):
    s = sorted(prices)
    i,j = 0,len(prices)-1
    r,re = 0,[]
    #print(s[j] - s[i],i,j)
    while i != j:
        if prices.index(s[i]) < prices.index(s[j]):
            re.append(s[j] - s[i])
        else:
            re.append(s[i] - s[j])
            #print(re)
        i += int(bin(r)[-1])
        r += 1
        j -= int(bin(r)[-1])
        #print(i,j)
    return max(re)
'''