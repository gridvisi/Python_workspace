'''
https://brilliant.org/problems/to-become-a-millionaire/
'''
s = [10,2, 4, 5, 6, 9, 5, 4, 3, 8,11]

"""
solution of:
    https://brilliant.org/practice/linear-data-structures-level-4-challenges/?p=2
"""

def max_profit(price_data, max_number_of_transactions):
    res_data = dict()
    def inner(t_num, day_num):
        if t_num <= 0 or day_num <= 0:
            res = 0
        elif (t_num, day_num) in res_data:
            res = res_data[(t_num, day_num)]
        else:
            res = max(inner(t_num, day_num-1),
                      max([price_data[day_num]-price_data[tmp_day]+inner(t_num-1, tmp_day)
                           for tmp_day in range(day_num)]))
            res_data[(t_num, day_num)] = res
        return res
    return inner(max_number_of_transactions, len(price_data)-1)

assert max_profit([8, 7, 5, 4, 3, 2], 2) == 0
assert max_profit([2, 4, 5, 6, 9, 5, 4, 3, 8], 2) == 12
BIG_DATA = [96, 26, 73, 51, 54, 36, 7, 82, 66, 74, 92, 45, 98, 61, 80, 74, 44,
            50, 57, 21, 9, 90, 60, 10, 65, 37, 58, 76, 38, 93, 42, 60, 5, 77,
            61, 66, 17, 84, 92, 52, 34, 63, 21, 93, 55, 33, 48, 91, 36, 90, 26,
            17, 55, 43, 19, 41, 70, 68, 88, 96, 66, 32, 86, 43, 85, 72, 9, 70,
            47, 87, 85, 62, 94, 52, 51, 5, 20, 53, 84, 75, 18, 16, 60, 61, 81,
            89, 91, 49, 37, 27, 6, 19, 76, 20, 5, 77, 26, 62, 7, 17, 80, 28, 98,
            9, 94, 77, 44, 16, 80, 56, 73, 22, 97, 29, 35, 85, 6, 37, 93, 33,
            95, 21, 61, 55, 37, 93, 35, 71, 38, 58, 42, 49, 69, 86, 65, 86, 70,
            35, 90, 30, 81, 6, 81, 83, 89, 75, 6, 91, 59, 86, 13, 10, 63, 85,
            50, 62, 52, 17, 16, 8, 64, 31, 89, 3, 14, 21, 35, 61, 56, 11, 18,
            68, 11, 95, 95, 4, 67, 64, 42, 69, 70, 50, 22, 86, 71, 95, 26, 85,
            23, 44, 79, 93, 99, 50, 90, 26, 72, 65, 28, 72]
print(max_profit(BIG_DATA, 2))


def max_profit(price):
    out = price[1] - price[0]
    min_price = price[0]
    for i, e in enumerate(price[1:]):
        if e - min_price > out:
            out = e - min_price
            sell = e
        if e < min_price:
            min_price = e
    return out

def max_twice(s):
    mx = max(s)
    step = 0
    if s.index(mx) == len(s)-1:
        print(s[:-1])
        left,right = s[:s.index(max(s[:-1]))+1], s[s.index(max(s[-1])):]
    if s.index(mx) == 0:
        left,right = s[:s.index(max(s[1:]))+1], s[s.index(max(s[1:])):]
        print(left,right)
    left = max_profit(s[:s.index(max(s))+1])
    right = max_profit(s[s.index(max(s))+1:])
    return s,left+right
#print(max_twice(s))

'''
Python读取excel求股票最大收益
B座17楼 4月17日
'''
def max_profit(prices):
    out = prices[1] - prices[0]
    min_price = prices[0]

    for i, e in enumerate(prices[1:]):
        if e - min_price > out:
            out = e - min_price
            sell = e
        if e < min_price:
            min_price = e
    return round(out, 2), sell - round(out, 2), sell

