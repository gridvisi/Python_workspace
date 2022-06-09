# https://brilliant.org/daily-problems/difference-of-powers/

p = 0
for i in range(0, 10):
    p += 2**i
    print(f"{p:>11b}")
print(f"{p+1:b}")