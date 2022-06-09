
from functools import reduce
x = 4
n = 5
def recur_cubes(n ,x):
    cache = []
    if n == 1:
        x = tri_cubes(x)
        return x
    else:
        x = recur_cubes( n -1 ,x)
        cache.append(x)
        print(cache)
        return recur_cubes(n - 1 ,x)

def tri_cubes(x):
    ls = map(lambda x :int(x )**3, list(str(x)))
    xls = reduce(lambda x ,y: x+ y, ls)
    # return tri_cubes(xls)
    return xls
print(recur_cubes(n, x))

#No 1.  solution
def foo(x): #sum of cube of digits
    y=0
    while(x>0):
        y+=(x%10)**3
        x//=10
    return(y)

Df=set(range(1,4*9**3)) # Df = domain of foo
Rf=set()
while(True):
    for i in Df:
        Rf.add(foo(i)) # Rf = range of foo
        if(len(Df)>len(Rf)): # if range != domain
            Df=Rf # range = new domain, reiterate
            Rf=set()
        else: # if range == domain
            break # limit set found
print('solution 1st',Rf)

#No 2 solution
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