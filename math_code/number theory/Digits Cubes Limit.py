'''
https://brilliant.org/problems/digits-cubes-limit/
Digits Cubes Limit
Computer Science Level 2
f(n)f(n) gives the sum of the cubed digits of some positive integer n.n. For example, f(123)=1^3+2^3+3^3=36.f(123)=1
If we repeatedly apply this process on each previous result, the following two different behaviors may arise:
Arrive at a fixed point: For example, beginning with 3, we eventually arrive at 153, and f(153)=153.f(153)=153.
We say that 153 is a fixed point.
Arrive at a limit cycle: For example, beginning with 4, we eventually arrive at 133, and f(133) = 55 \implies f(55) = 250 \implies f(250)=133.
f(133)=55⟹f(55)=250⟹f(250)=133. We say that \{55,133,250\}{55,133,250} is a limit cycle.
Let the limit set be the set of all fixed points and limit cycles in the range of f(n).f(n).
Find the sum of all the numbers in the limit set (including the four in pink found above).
Note: A coding environment is provided below:
'''
# solution 1
found = []
for n in range(1, 2917):
    previous = []
    k = n
    while k not in previous:
        n = k
        k = sum([int(a)**3 for a in str(n)])
        previous.append(n)
    if k not in found:
        for i in range(previous.index(k), len(previous)):
            if previous[i] not in found:
                found.append(previous[i])
print(sum(found))

# solution 2
def f(n): # sum cubes of digits
    ss=0
    s=str(n)
    for i in range(len(s)):
        ss+=int(s[i])**3
    return ss

def g(n): # find cycles
    cycle=set([f(n)])
    n=f(n)
    while n not in cycle:
        cycle.add(n)
        n=f(n)
    cycle=set([n])
    n=f(n)
    while n not in cycle:
        cycle.add(n)
        n=f(n)
    return(cycle)

u=set()
for i in range(1,10000):
    u=u.union(g(i))
print(u)


# solution 3
def foo(x): #sum of cube of digits
    y=0;
    while(x>0):
        y+=(x%10)**3;
        x//=10;
    return(y);

Df=set(range(1,4*9**3))   # Df = domain of foo
Rf=set()
while(True):
    for i in Df:
        Rf.add(foo(i))    # Rf = range of foo
    if(len(Df)>len(Rf)): # if range != domain
        Df=Rf            # range = new domain, reiterate
        Rf=set()
    else:                   # if range == domain
        break              # limit set found

print(sum(Rf))