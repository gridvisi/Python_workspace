#https://brilliant.org/problems/digits-cubes-limit/?ref_id=1509807
'''
a = {[1,2,3],[1,2,3]}
print(set(a))
a = {{1,2,3},{1,2,3}}
print(set(a))

a = {1,2,3,1,2,3}
print(set(a))

a = [1,2,3,1,2,3]
print(set(a))

a = {(1,2,3),(1,2,3)}
print(set(a))

a = [{1,2,3},{1,2,3}]
print(set(a))

'''

import math
import time
def cube(x):
    bench = []
    while x not in bench:
        bench.append(x)
        x = sum([pow(int(i),3) for i in str(x)])
    return set(i for i in bench[bench.index(x):])
x = 5
print(cube(x))

n,total,re = 1,0,set()
result = {}
re = set()
while n < 10000:
    result[n]=cube(n)
    re.update(cube(n))
    n += 1
st = time.time()
print(set(re),sum(re))
nd = time.time()
print('time use:',nd - st)

n,total,re = 1,0,set()
while cube(n).difference(re):
    re.update(cube(n))
    n += 1
print(re,sum(re))

n,total,re = 1,0,set()
while not cube(n).issubset(re):
    re.update(cube(n))
    print(re,cube(n))
    n += 1
print('::',re,sum(re),n)


# Recrution infinite to finite repeat point
def cube(x):
    total = sum([pow(int(i), 3) for i in str(x)])
    print(x,total)
    if x == total:
        return x
    return cube(total),total
x = 4
#print(cube(x))

'''
L1 = [1, 2, 3, 3]
>>> L2 = [1, 2, 3, 4]
>>> set(L1).difference(L2)
set([ ])
>>> set(L2).difference(L1)
set([4])
'''

# brilliant post
def f(x):
    sum = 0
    while(x!=0):
        sum += (x%10)**3
        x //= 10
    return sum

limit_set = set()
# The highest digit possible is 9. 9999 decreases to 2916, so we can say with certainity that
# the largest fixed point is at most 4 digits, and further that it is at most 2916 since any 4-digit number
# greater than that will decrease. Also, of course, any value must be at least 0.
for i in range(2917):
    path = set()
    next = i
    while not (next in path):
        path.add(next)
        next = f(next)
    # at this line, next is part of the limit set, since it was seen twice on the path.
    # Add the cycle to the limit set (it's a set, so we can add it several times)
    cycle_pos = f(next)
    limit_set.add(next) # this line needed to add fixed points
    while(cycle_pos !=next):
        limit_set.add(next)
        cycle_pos = f(cycle_pos) 
sum = 0
for i in limit_set:
    sum+=i
print(sum)