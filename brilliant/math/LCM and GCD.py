'''
https://brilliant.org/daily-problems/sick-dog/

Today's Challenge
Sarai takes her dog Seamus to the veterinarian and is given two different medications:

When they get home at 12:00,12:00, Sarai gives Seamus a dose of both medications.
After that, she needs to give Seamus a dose of one medication every eight hours,
and the other every ten hours.

What time will it be ((on a 1212-hour clock)) the next time Sarai gives Seamus both
medications at the same time?

今天的挑战
Sarai带着她的狗Seamus去看兽医，并得到两种不同的药物。
当他们在12: 00回家时，Sarai给Seamus服用两种药物。之后，她需要每隔8小时给Seamus服用一种药物，
另一种药物每隔10小时服用一次。下次Sarai同时给Seamus服用两种药物的时间是（（12小时钟））？
'''
import time

print([i for i in range(12,100) if i % 8 == 0 and i % 10 == 0])

#import sympy
#print(sympy.lcm(10, 8) % 12)


# find prime factors
from collections import Counter
from collections import defaultdict
def factorize(n):
    factor = 2
    factors = []
    while factor <= n//factor:
        while n % factor == 0:
            factors.append(factor)
            n //= factor
        factor += 1
    if n > 1:
        factors.append(n)
    return factors

# factorize all numbers and count equal factors
factorizedList = []
for i in [10, 8]:  # or as many other numbers as you like but each >= 1
    factorizedList.append(Counter(factorize(i)))

# find max powers of equal factors
result = defaultdict(int)
for f in factorizedList:
    for k, v in f.items():
        result[k] = max(result[k], v)

# product of max-powers-factors
lcm = 1
for k, v in result.items():
    lcm *= pow(k, v)

print(lcm)