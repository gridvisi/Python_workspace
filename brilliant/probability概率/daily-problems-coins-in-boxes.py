'''
https://brilliant.org/daily-problems/coins-in-boxes/
'''
s = ''
from random import choice, randrange

G, S = "gold", "silver"
BOXES = ((G, G, G), (G, G, S), (G, S, S), (S, S, S))

N_TRIAL = 10000
n_total = 0
n = 0

for i in range(N_TRIAL):
    box = list(choice(BOXES))
    print(box)
    coin = box.pop(randrange(3)) #随机选一个挑出来
    print(box,coin)
    if coin == S:
        n_total += 1
        if choice(box) == S:
            n += 1

print(n / n_total)