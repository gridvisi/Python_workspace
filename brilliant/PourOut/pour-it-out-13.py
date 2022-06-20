'''
https://brilliant.org/daily-problems/pour-it-out-13/
'''
option = [1.5,3.25,5,6.75]

def pourMin(u,U): # u=small, U=larger
    i,j,s = 2,1,True
    ans = [float('INF')]
    minvol = u*i - U*j
    step = 0
    while minvol <= u+U:#minvol <= 两个杯子容量之和
        s = not(s)

        minvol = abs(u*i - U*j)
        i += s
        j += not(s)
        ans.append(minvol)

    return sorted(set(ans)),[i for i in set(ans) if i in option]
u,U = 9,11.25
print(pourMin(u,U))


# filter result of pourMin

def isVolum(x):
    return x <= u+U
#notVolum = lambda x:x!=0 and x<=u+U
#
from itertools import dropwhile
print('dropwhile:',list(dropwhile(isVolum,pourMin(u,U)[0])))

from itertools import takewhile
print('takewhile:',list(takewhile(isVolum,pourMin(u,U)[0])))

#from itertools import span
#print('takewhile:',list(span(isVolum,pourMin(u,U)[0])))


def notisVolum(x):
    return x > 0

def span(x):

    right = list(takewhile(isVolum,x))
    left = list(dropwhile(right, x))
    ans = left.extend(right)
    return left,right
x = pourMin(u,U)[0]
print('span:',span(x))

import math
ans = []
for n in pourMin(u,U)[0]:
    if n > 0 and n <= (u+U):
        #print(n,ans)
        ans.append(n)
print('for_loop',ans)
print(1 > 0.0)

'''

def drop_while(arr, pred):
    return list(dropwhile(pred, arr))

arr,pred = pourMin(u,U),notVolum
print(drop_while(arr,pred))
'''


#example
from itertools import dropwhile
import itertools

# initializing list
li = [2, 4, 5, 7, 8]

# using dropwhile() to start displaying after condition is false
print("The values after condition returns false : ", end="")
print(list(itertools.dropwhile(lambda x: x % 2 == 0, li)))

#example-2
# Python code to demonstrate the working of
# dropwhile()


# Function to be passed
# as an argument
def is_positive(n):
    return n > 0
value_list = [5, 6, -8, -4, 2]
result = list(itertools.dropwhile(is_positive, value_list))

print(result)