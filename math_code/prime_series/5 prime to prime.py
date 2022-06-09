__author__ = 'Administrator'
import math

def primes(n): # simple Sieve of Eratosthenes
   odds = range(3, n+1, 2)
   sieve = set(sum([range(q*q, n+1, q+q) for q in odds],[]))
   return [2] + [p for p in odds if p not in sieve]


def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = range(r)
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

n = 4
r = 3
primes_ = primes(20)
print ('List of primes being examined: %s' % primes_)
combos = nCr(n,r)

max_count = 0
max_ = []

for i in combinations(primes_, n):
    count = 0
    for j in combinations(i, r):
        if sum(j) in primes(400):
           count += 1
        if count > max_count:
            max_count = count

print ('Maximum number of triples out of %d possible combinations with a prime sum = %d'\
     %(combos, max_count))

for i in combinations(primes_, n):

    count = 0
    for j in combinations(i, r):
        if sum(j) in primes(400):
           count += 1
        if count == max_count:
            max_.append(i)

print ('Combos of %d numbers with the sum of %d/%d triples being prime: %s' \
    % (n, max_count, combos, max_))