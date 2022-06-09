'''
https://brilliant.org/daily-problems/what-is-love/
'''

digit = [i for i in range(10)]
ans = []
for i in digit[1:]:
    for j in digit:
        if str(5*i + 5*j+3)[:2] == str(j)+str(i):
            ans.append([i,j])

print(ans)

for love in range(2000, 9999):
    l, o, v, e = list(map(int, str(love)))  # or  [love//10**n % 10 for n in range(3, -1, -1)]
    s, o_, l_, v_, e_ = list(map(int, str(5 * love)))
    if len(set([s, o_, l_, v_, e_])) == 5 and [s, o_, l_, v_, e_] == [s, o, l, v, e] :
        print("LOVE", "=", love)


from itertools import permutations

for S, O, L, V, E in permutations("0123456789", 5):
    LOVE = int(L + O + V + E)
    SOLVE = int(S + O + L + V + E)
    if 5 * LOVE == SOLVE:
        print(f"5 x {LOVE} = {SOLVE}")
