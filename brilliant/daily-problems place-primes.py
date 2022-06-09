'''
https://brilliant.org/daily-problems/place-primes/
'''

# solution A
# Place the Tiles
# Python

# set up variables
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
from itertools import permutations
p = list(permutations([2, 2, 3, 3, 5, 5, 7, 7]))
q = [(2, 2), (2, 3), (2, 4), (3, 2), (3, 3), (4, 2)]
# q is the number of tile total combinations
#   for Manju and Rosina

# go through each permutation of tiles
sollist = []
for a in range(0, len(p)):
    for b in range(0, len(q)):
        # make a list of Manju's, Rosina's,
        #  and Erin's tiles
        MTiles = []
        RTiles = []
        ETiles = []
        for c in range(0, q[b][0]):
            MTiles.append(p[a][c])
        for c in range(q[b][0], q[b][0] + q[b][1]):
            RTiles.append(p[a][c])
        for c in range(q[b][0] + q[b][1], 8):
            ETiles.append(p[a][c])
        # make sure the list is sorted to avoid repeats
        if sorted(MTiles) == MTiles and sorted(
            RTiles) == RTiles and sorted(
                ETiles) == ETiles:
            # find the sum of Manju's tiles
            MSum = 0
            for c in range(0, len(MTiles)):
                MSum += MTiles[c]
            # find the sum of Rosina's tiles
            RSum = 0
            for c in range(0, len(RTiles)):
                RSum += RTiles[c]
            # find the product of Rosina's tiles
            RProd = 1
            for c in range(0, len(RTiles)):
                RProd *= RTiles[c]
            # find the range of Erin's tiles
            ERange = max(ETiles) - min(ETiles)
            # if Rosina's sum is smaller than the
            #  current stored minimum and if
            #  everyone's tiles fit all the other
            #  criteria, then store the new minimum
            if (MTiles, RTiles, ETiles) not in sollist:
                if MSum in primes and ERange in primes:
                    if RProd % MSum == 0 and (
                        RProd % ERange) == 0:
                        sollist.append((MTiles, RTiles, ETiles))
                        print(MTiles, RTiles, ETiles)
# display the results
print("There are " + str(len(sollist)) + (
    " possible ways to solve the puzzle."))


# Solution B
# Python

# set up variables
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
from itertools import permutations
p = list(permutations([2, 2, 3, 3, 5, 5, 7, 7]))
q = [(2, 2), (2, 3), (2, 4), (3, 2), (3, 3), (4, 2)]
# q is the number of tile total combinations
#   for Manju and Rosina

# go through each permutation of tiles
RSumMin = 30
for a in range(0, len(p)):
    for b in range(0, len(q)):
        # make a list of Manju's, Rosina's,
        #  and Erin's tiles
        MTiles = []
        RTiles = []
        ETiles = []
        for c in range(0, q[b][0]):
            MTiles.append(p[a][c])
        for c in range(q[b][0], q[b][0] + q[b][1]):
            RTiles.append(p[a][c])
        for c in range(q[b][0] + q[b][1], 8):
            ETiles.append(p[a][c])
        # find the sum of Manju's tiles
        MSum = 0
        for c in range(0, len(MTiles)):
            MSum += MTiles[c]
        # find the sum of Rosina's tiles
        RSum = 0
        for c in range(0, len(RTiles)):
            RSum += RTiles[c]
        # find the product of Rosina's tiles
        RProd = 1
        for c in range(0, len(RTiles)):
            RProd *= RTiles[c]
        # find the range of Erin's tiles
        ERange = max(ETiles) - min(ETiles)
        # if Rosina's sum is smaller than the
        #  current stored minimum and if
        #  everyone's tiles fit all the other
        #  criteria, then store the new minimum
        if RSum < RSumMin:
            if MSum in primes and ERange in primes:
                if RProd % MSum == 0 and (
                    RProd % ERange) == 0:
                    RSumMin = RSum
# display the results
print("The minimum possible sum of Rosina's " + (
    "tiles is " + str(RSumMin)) + ".")