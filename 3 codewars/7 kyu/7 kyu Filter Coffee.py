'''
You love coffee and want to know what beans you can afford to buy it.
The first argument to your search function will be a number which represents
your budget.

The second argument will be an array of coffee bean prices.
Your 'search' function should return the stores that sell coffee within your budget.
The search function should return a string of prices for the coffees beans you can afford.
 The prices in this string are to be sorted in ascending order.
'''
budget,prices = 14, [7, 3, 23, 9, 14, 20, 7]
def search(budget,prices):
    res = ''
    re = sorted([x for x in prices if x <= budget])
    for e in re:
        res += str(e)+','
    return res[:-1]

print(search(budget,prices))

def search(budget, prices):
    return ','.join(str(a) for a in sorted(prices) if a <= budget)

budget = int(input())
price = [int(n) for n in input().split()]
print(','.join(str(a) for a in sorted(prices) if a <= budget))