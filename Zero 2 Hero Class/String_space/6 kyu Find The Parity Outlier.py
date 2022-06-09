'''
https://www.codewars.com/kata/find-the-parity-outlier/solutions/python

You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.
Examples
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
ALGORITHMS
'''


def find_outlier(int):
    odds = [x for x in int if x % 2 != 0]
    evens = [x for x in int if x % 2 == 0]
    return odds[0] if len(odds) < len(evens) else evens[0]


def find_outlier(integers):
    parity = [n % 2 for n in integers]
    return integers[parity.index(1)] if sum(parity) == 1 else integers[parity.index(0)]

def find_outlier(integers):
    temp = []
    for i in integers:
        if i % 10 == 0 or i % 10 == 2 or i % 10 == 4 or i % 10 == 6 or i % 10 == 8:
            temp.append(1)
        else:
            temp.append(0)
    if temp.count(1) == 1:
        return integers[temp.index(1)]
    elif temp.count(0) == 1:
        return integers[temp.index(0)]