# https://brilliant.org/daily-problems/missing-length/
# triangle similiar
import math
res = []
h = 48
l = 100
for x in range(1,l):
    if x * (l-x) == h*h:
        res.append(x)
rate = math.sqrt((h**2 + res[1]**2)/res[1]**2)
print(l*rate)