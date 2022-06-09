'''
https://brilliant.org/problems/kaboobly-dooists-visit-the-canteen/
'''
price ={'A': 12, 'B': 7,
        'C': 10, 'D': 9,
        'E': 7, 'F': 13,
        'G': 11, 'H': 9,
        'I': 8, 'J': 13,
        'K': 10, 'L': 10,
        'M': 8, 'N': 11,
        'O': 11, 'P': 9,
        'Q': 7, 'R': 11,
        'S': 9, 'T': 12}

canteen = 'ABCDEFGHIJKLMNOPQRST'
print(price['A'],set(canteen))
bad_pairs = set()
for i in range(0,len(canteen),2):
    new = (canteen[i],canteen[i+1])
    bad_pairs.add(new)
print(bad_pairs)

def sum_price(items):
    total = 0
    for item in items:
        print('sum_item:',item,items,price[item])
        total += price[item]
    return total

def alphabetize(items):
    return ''.join(sorted(items))

def valid(items):
    for a, b in bad_pairs:
        if a in items and b in items:
            return False
    if sum_price(items) > 50:
        return False
    if items != alphabetize(items):
        return False
    return True

def neighbors(items):
    children = set()
    okay = set(canteen)-set(items)
    print('okay:',okay)
    for item in okay:
        if valid(items+item):
            print('valid(items+item):',valid(items+item))
            children.add(items+item)
    print('children:',children)
    return children

level = {0:set([''])}
cur_level = 1
while cur_level <= 5:
    level[cur_level] = set()
    print(level[cur_level])
    for items in level[cur_level-1]:
        print('itmes:',items)
        for new in neighbors(items):
            print(new)
            level[cur_level].add(new)
    del level[cur_level-1]
    cur_level += 1
print("Answer:", len(level[5]))