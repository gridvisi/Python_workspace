'''
https://brilliant.org/daily-problems/pigeonholed-numbers/


'''

from itertools import combinations

jar = {n: list(combinations(range(1, 9), n)) for n in range(2, 9)}
print(jar)
for cards in range(3, 9):
    for pull in jar[cards]:
        if not any([sum(n) == 9 and set(n) & set(pull) == set(n) for n in jar[2]]):
            break
    else:
        print("pair guaranteed at min", cards, "moves")
        break