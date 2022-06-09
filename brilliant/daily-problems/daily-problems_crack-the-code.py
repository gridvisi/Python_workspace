'''
https://brilliant.org/daily-problems/crack-the-code/

There is a three-digit code where only the digits 1 through 5 are possible. Each of the numbers below has exactly one digit correct, and in none of the cases is the correct digit in the correct place.



123 has exactly one digit correct, in the wrong position.
532 has exactly one digit correct, in the wrong position.
342 has exactly one digit correct, in the wrong position.
235 has exactly one digit correct, in the wrong position.

FirstDigit= ?

SecondDigit= ?

ThirdDigit= ?
'''

from itertools import permutations

"""
    abc
    ---
    123
    532
    342
    235
take it by columns:
    'a'  cannot be 1, 5, 3 or 2
    'b'  cannot be 2, 3, or 4
    'c'  cannot be 3, 2, 5
"""

digits = [1, 2, 3, 4, 5]
for a, b, c in permutations(digits, 3):
    if a not in [1, 5, 3, 2] and b not in [2, 3, 4] and c not in [3, 2, 5]:
        print(a, b, c)


#2nd solution
allPossib = range(111, 556)
inputs = [123, 532, 342, 235]
sets   = {}

def comparing(inputs, possib):
    exactPos = sum(a==b for a, b in zip(inputs, possib))
    wrongPos = sum(min(inputs.count(a), possib.count(a)) for a in possib) - exactPos
    return (exactPos, wrongPos)

for i in inputs:
    sets[i] = set(possib for possib in allPossib if comparing(str(i), str(possib)) == (0, 1))

code = sets[inputs[0]]
for k, v in sets.items():
    code &= v

print(code)
