'''
https://brilliant.org/problems/breaking-rsa-gcd-of-multiple-keys/

Breaking RSA (GCD of multiple keys)
Computer Science Level 1
You have looked up several people's public keys, some of which
are below. Some of them are vulnerable, because they are divisible
by the same prime. What prime is that?

Key #1: 1196311
Key #2: 1250759
Key #3: 1362733
Key #4: 1462991
Key #5: 1509349
'''

import itertools

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

for x in list(itertools.combinations([1196311, 1250759, 1362733, 1462991, 1509349], 2)):
    temp = gcd(x[0], x[1])
    if temp != 1:
        print(temp)