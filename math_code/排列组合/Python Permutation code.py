
#https://stackoverflow.com/questions/3336862/python-permutation-code

def perm(lst, c = [], x = 0):
    i = -1
    g = len(lst) - 1
    if x == g:
        while i < g:
            i += 1
            if lst[i] in c:
                continue
            c.append(lst[i])
            print(c)
            del c[-1]
            i = g
    else:
        while i < g:
            if x == 0:
                del c[:]
            elif g == x:
                del c[-1]
            elif len(c) > x:
                del c[-1]
                continue
            i += 1
            if lst[i] in c:
                continue
            c.append(lst[i])
            x + 1
            perm(lst, c, x + 1)

lst = 'abcd'
lst = '1234'
print(perm(lst, c = [], x = 0))

'''
perm(range(2))
[0, 1]
[1, 0]

perm([1, 4, 5])
[1, 4, 5]
[1, 5, 4]
[4, 1, 5]
[4, 5, 1]
[5, 1, 4]
[5, 4, 1]
'''

import itertools
for i in itertools.permutations('abcd',4):
    print (''.join(i))

print(list(itertools.combinations(['a','b','c'],2)))
#[('a', 'b'), ('a', 'c'), ('b', 'c')]