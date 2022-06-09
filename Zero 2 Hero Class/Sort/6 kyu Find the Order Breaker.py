'''
https://www.codewars.com/kata/5fc2a4b9bb2de30012c49609/train/python

In this kata, you have an integer array which was ordered by ascending except one number.

For Example: [1,2,3,4,17,5,6,7,8]
For Example: [19,27,33,34,112,578,116,170,800]
You need to figure out the first breaker. Breaker is the item, when removed from sequence, sequence becomes ordered by ascending.

For Example: [1,2,3,4,17,5,6,7,8] => 17 is the only breaker.

For Example: [19,27,33,34,112,578,116,170,800] => 578 is the only breaker.

For Example: [105, 110, 111, 112, 114, 113, 115] => 114 and 113 are breakers. 114 is the first breaker.
    When removed 114, sequence becomes ordered by ascending => [105, 110, 111, 112, 113, 115]
    When removed 113, sequence becomes ordered by ascending => [105, 110, 111, 112, 114, 115]

For Example: [1, 0, 2] => 1 and 0 are the breakers. 1 is the first breaker.
    When removed 1, sequence becomes ordered by ascending => [0, 2]
    When removed 0, sequence becomes ordered by ascending => [1, 2]

For Example: [1, 2, 0, 3, 4] => 0 is the only breaker.
    When removed 0, sequence becomes ordered by ascending. => [1, 2, 3, 4]
TASK:
Write a function that returns the first breaker.

Notes:

Input array does not contain any duplicate element.
'''

def order_breaker(n):
    for i in range(len(n)-1):
        sl = [e for i,e in enumerate(n) if i != n[i]]
        if sorted(sl) == sl:
            return n[i]

def order_breaker(n):
    for i in range(len(n)):
        if n[:i]+n[i+1:] == sorted(n[:i]+n[i+1:]):
            return n[i]
print(float('inf'))
inp = [1,2,3,4,17,5,6,7,8]
#inp = [1, 2, 0, 3, 4]
# sum([y for x,y in list(zip(inp[:-1],inp[1:])) if x-y > 0 ])
print(order_breaker(inp))
'''
def order_breaker(n):
    for i in range(1,len(n)):
        if len(n)<=2 and n[i-1] > n[i]:return n[i-1]
        elif n[i-1] < n[i] > n[i+1]:return n[i]
        
        elif n[i-1] > n[i] < n[i+1]:
            return n[i-1]

def order_breaker(n):
    for i in range(1,len(n)-1):
        if n[i-1] < n[i] > n[i+1] or n[i-1] > n[i] < n[i+1]:
            return n[i]

def order_breaker(n):
    for i in range(len(n)):
        if n[i] != sorted(n)[i]:
            return n[i]
            
[1, 2, 0, 3, 4]
2 should equal 0

def order_breaker(n):
    if len(n) <= 3: return n[0]
    return [n[i] for i in n[1:-2] if n[i-1] < n[i] > n[i+1] or n[i-1] > n[i] < n[i+1]]
    
def order_breaker(n):
    m = sorted(n)
    for i in n:
        if not n.index(i) == m.index(i):
            return i
'''


#1st
INF = float('inf')

def order_breaker(lst):
    return next(b for a,b,c in zip([-INF]+lst, lst, lst[1:]+[INF])
                  if a<=c and (a>b or b>c) )

#2nd
def order_breaker(a):
    for i, x in enumerate(a):
        if x > a[i+1]:
            return a[i+(i and a[i-1] > a[i+1])]

#3rd
def order_breaker(inp):
    for i, num in enumerate(inp):
        x = inp[0:i] + inp[i+1:]
        if x == sorted(x):
            return num

#4th
def order_breaker(a):
    if a[0] > a[1]:
        return a[0]
    return next(
        x if w < y else y
        for w, x, y in zip(a, a[1:], a[2:])
        if x >= y
    )