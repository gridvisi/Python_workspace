# https://brilliant.org/daily-problems/grid-fill-18/

test = [[2,3,4],[3,4,5]]
#print([x for y in test for x in y])

import random
from itertools import combinations
from itertools import permutations
grid = [1,2,3,4] * 3
print(len(list(permutations(grid))))

fourvect = [[1,1,2,2],[1,1,1,3]]

print(list(permutations(grid)))

for side in list(permutations(grid)):
    #print(side)
    if all([sum(side[i:i+4])==9 for i in range(0,13,4)]):
        if sorted([side[i] for i in range(0,13,4)]) in fourvect:
            print('side:',side)

print('grid')

'''

#s = random.choices(grid) #only pick one
#s = random.sample(grid,4) # not suit to slove since repeat element exceed precondition
s = [i for i in list(combinations(grid,4)) if sum(i)==9]
#print(list(s),len(s))
fourvect = [[1,1,2,2],[1,1,1,3]]

for i in s:
    one = [i for i in s if i[0]==1]
    two = [i for i in s if i[0]==2]
    three = [i for i in s if i[0]==3]
    for first in combinations(one,3):
        #print(list(first))
        fir = [x for y in first for x in y]
        for second in two:
            sec = [i for i in second]
            seq = fir + sec
            print(seq)
            if seq.count(1) == seq.count(2) == seq.count(3) == seq.count(4) == 3:
                print('result', seq)


print(len(one),one)
print(len(two),two)
print(len(three),three)
'''

