'''
https://brilliant.org/daily-problems/wrong-seats/
'''

from itertools import product
from collections import Counter

# all combinations of possible distances
# count all distances in each combination and collect max value
# print min of all max
print(min([max(Counter(p).values()) for p in (product([1, 2, 3, 4, 5], repeat=6))]))

print([(Counter(p).keys(),Counter(p).values(),p) for p in list(product([1, 2, 3, 4, 5], repeat=6))])


#Solution 2nd
from itertools import permutations

def isNotInOrder(lst):
    for i in range(6):
        if lst[i] == i:
            return False
    return True

def countCorrectPosition(lst):
    count = 0
    for i in range(6):
        if lst[i] == i:
            count += 1
    return count

def rotateClockwise(lst):
    temp = lst[0]
    for i in range(len(lst)-1):
        lst[i] = lst[i+1]
    lst[len(lst)-1] = temp

# Get all configurations such that no one is in the correct position
configurations = filter(isNotInOrder, permutations(range(6)))

# Contains the smallest maximum number of correct positions
minOfMax = 6

for config in configurations:
    config = list(config)
    maxCorrectPos = 0
    for _ in range(5):
        rotateClockwise(config)
        numCorrectPos = countCorrectPosition(config)
        maxCorrectPos = max(maxCorrectPos, numCorrectPos)
    rotateClockwise(config)
    minOfMax = min(minOfMax, maxCorrectPos)

# Print the smallest maximum
print("Smallest number of correct positions: %d" % (minOfMax))