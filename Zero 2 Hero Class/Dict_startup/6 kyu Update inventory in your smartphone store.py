'''
https://www.codewars.com/kata/57a31ce7cf1fa5a1e1000227/train/python

current = [(25, 'HTC'), (1000, 'Nokia'), (50, 'Samsung'), (33, 'Sony'), (10, 'Apple')]
new = [(5, 'LG'), (10, 'Sony'), (4, 'Samsung'), (5, 'Apple')]
result = [(15, 'Apple'), (25, 'HTC'), (5, 'LG'), (1000, 'Nokia'), (54, 'Samsung'), (43, 'Sony')]

Test.assert_equals(update_inventory(current, new), result)
'''
#10 solve by ericlee
def update_inventory(cur_stock, new_stock):
    cur_stock = dict(item[::-1] for item in cur_stock)
    new_stock = dict(item[::-1] for item in new_stock)
    print(cur_stock,new_stock)
    #new_stock.update(cur_stock)
    for k,v in cur_stock.items():
        if k in new_stock:
            cur_stock[k] += new_stock[k]
    new_stock.update(cur_stock)
    return sorted([(v,k) for k,v in new_stock.items()])

current = [(25, 'HTC'), (1000, 'Nokia'), (50, 'Samsung'), (33, 'Sony'), (10, 'Apple')]
new = [(5, 'LG'), (10, 'Sony'), (4, 'Samsung'), (5, 'Apple')]
print(update_inventory(current, new))

#1st
from collections import defaultdict
def update_inventory(cur_stock, new_stock):
    answer = defaultdict(int)
    for stock, item in cur_stock + new_stock:
        answer[item] += stock
    return [(answer[item], item) for item in sorted(answer)]


#
from collections import Counter
def update_inventory(cur_stock, new_stock):
    stock = Counter({k: v for v, k in cur_stock}) + Counter({k: v for v, k in new_stock})
    return sorted(((v, k) for k, v in stock.items()), key=lambda x: (x[1]))

#

from collections import defaultdict


def update_inventory(cur_stock, new_stock):
    answer = defaultdict(int)
    for stock, item in cur_stock + new_stock:
        answer[item] += stock
    return [(answer[item], item) for item in sorted(answer)]


from collections import defaultdict
def update_inventory(cur_stock, new_stock):
    stock = defaultdict(int, [(k, v) for v, k in cur_stock])

    for v, k in new_stock:
        stock[k] += v

    return [(v, k) for k, v in sorted(stock.items())]



def update_inventory(cur_stock, new_stock):
    updated_stock = [];
    stock = [];
    brands = [];
    tmpBrands = [];

    # determine original brands available
    for i in cur_stock:
        brands.append(i[1])

    # determine all brands now available
    for j in new_stock:
        if j[1] not in brands:
            brands.append(j[1])

    # sort the brand list into alphabetical order
    brands.sort()
    tmpBrands = brands.copy()
    print(tmpBrands)

    # create list of summed intersecting stock
    for i in cur_stock:
        for j in new_stock:
            if i[1] == j[1]:
                stock.append((i[0] + j[0], i[1]))
                # remove brand from list
                tmpBrands.remove(i[1])

    # add mutually exclusive brand stock from original stock
    for i in cur_stock:
        if i[1] in tmpBrands:
            stock.append(i)
            tmpBrands.remove(i[1])

    # add mutually exclusive brand stock from new stock
    for j in new_stock:
        if j[1] in tmpBrands:
            stock.append(j)
            tmpBrands.remove(j[1])

    i = 0
    while len(stock):
        for j in brands:
            for k in stock:
                if j == k[1]:
                    updated_stock.append(k)
                    stock.remove(k)
                    break
        i += 1

    return updated_stock


from collections import defaultdict
def update_inventory(prv_stock, add_stock):
    new_stock = defaultdict(int, (item[::-1] for item in prv_stock))
    for qty, prod in add_stock:
        new_stock[prod] += qty
    return [item[::-1] for item in sorted(new_stock.items())]


from collections import Counter
# Counter already knows how to do that
def update_inventory(cur_stock, new_stock):
    C1 = Counter({v: k for k, v in cur_stock})
    C2 = Counter({v: k for k, v in new_stock})
    return [(v, k) for k, v in sorted((C1 + C2).items())]


from collections import Counter
def update_inventory(cur_stock, new_stock):
    c = Counter({key: value for value, key in cur_stock}) + Counter({key: value for value, key in new_stock})
    return [(c[key], key) for key in sorted(c)]


def update_inventory(cur_stock, new_stock):
    cur_stock_dict = {key: value for value, key in cur_stock}
    for value, key in new_stock:
        cur_stock_dict[key] = cur_stock_dict.get(key, 0) + value
    return [(cur_stock_dict[key], key) for key in sorted(cur_stock_dict)]

from collections import Counter

revertToDct = lambda lst: Counter(dict(x[::-1] for x in lst))

def update_inventory(*stocks):
    old, new = map(revertToDct, stocks)
    return [it[::-1] for it in sorted((old + new).items())]

def update_inventory(cur_stock, new_stock):
    d = {}
    for i, j in cur_stock + new_stock:
        d[j] = d.get(j, 0) + i
    return sorted([(j, i) for i, j in d.items()], key=lambda x: x[1])

from functools import reduce
from collections import Counter
def update_inventory(cur_stock, new_stock):
    return sorted([(v, k) for k, v in
                   reduce(lambda x, y: x + y, [Counter({k: v for v, k in x}) for x in [cur_stock, new_stock]]).items()],
                  key=lambda x: x[1])


def update_inventory(cur_stock, new_stock):
    cur_stock = dict(item[::-1] for item in cur_stock)
    new_stock = dict(item[::-1] for item in new_stock)
    for k, v in cur_stock.items():
        if k in new_stock:
            cur_stock[k] += new_stock[k]
    new_stock.update(cur_stock)
    return [(v, k) for k, v in sorted(new_stock.items())]


from collections import defaultdict
def update_inventory(curstock, newstock):
    curdict = defaultdict(int, [(brand, inv) for inv, brand in curstock])
    for v, k in newstock:
        curdict[k] += v
    sortedlist = [(v, k) for k, v in sorted(curdict.items())]
    return sortedlist

from operator import itemgetter
def update_inventory(curstock, newstock):
    curdict = {brand: inv for inv, brand in curstock}
    for v, k in newstock:
        if k in curdict:
            curdict[k] += v
        else:
            curdict[k] = v
    sortedlist = sorted([(v, k) for k, v in curdict.items()], key=itemgetter(1))
    return sortedlist


from collections import Counter
def update_inventory(cur_stock, new_stock):
    stock = Counter({k: v for v, k in cur_stock}) + Counter({k: v for v, k in new_stock})

    return sorted(((v, k) for k, v in stock.items()), key=lambda x: (x[1]))


def update_inventory(cur_stock, new_stock):
    to_dict = lambda L: {tup[1]: tup[0] for tup in L}
    from_dict = lambda d: [(v, k,) for k, v in d.items()]
    return sorted(from_dict(merge(to_dict(cur_stock), to_dict(new_stock))), key=lambda x: x[1])

def merge(*args):
    d = {}
    for arg in args:
        for key in arg:
            d[key] = d.get(key, 0) + arg[key]
    else:
        return d


from collections import Counter
def update_inventory(cur_stock: list, new_stock: list) -> list:
    current, new = Counter({val: key for key, val in cur_stock}), Counter({val: key for key, val in new_stock})
    return [(val, key) for key, val in sorted((current + new).items())]

def update_inventory(cur_stock, new_stock):
    phones = [i[1] for i in cur_stock + new_stock]
    cur_stock = {k: v for v, k in cur_stock}
    new_stock = {k: v for v, k in new_stock}
    ans = []
    for phone in sorted(list(set(phones))):
        ans.append((cur_stock.get(phone, 0) + new_stock.get(phone, 0), phone))
    return ans

#
def update_inventory(cur_stock, new_stock):
    cur_stock = {v: k for k, v in cur_stock}
    for v, k in new_stock:
        cur_stock[k] = cur_stock.get(k, 0) + v
    return sorted(((v, k) for k, v in cur_stock.items()), key=lambda x: x[1])