'''
https://brilliant.org/daily-problems/bus-trip/


'''

from itertools import permutations
K, L, M, N, O = "Kamila", "Lily", "Miliam", "Naomi", "Odette"
for order in permutations((K, L, M, N, O)):
    if order.index(N) > order.index(L):
        continue
    if (order.index(L) < order.index(O)) ^ (order.index(O) < order.index(K)):
        continue
    if abs(order.index(K) - order.index(M)) != 3:
        continue
    print(" -> ".join(order))


#2nd
from itertools import permutations
for k, l, m, n, o in permutations([1, 2, 3, 4, 5]):
    if n < l and abs(k-m) == 3 and ((l<o<k) or (k<o<l)):
        l = [('k', k), ('l', l), ('m', m), ('n', n), ('o', o)]
        a = sorted(l, key=lambda item : item[1])
        print(''.join([j[0].upper() for j in a]))