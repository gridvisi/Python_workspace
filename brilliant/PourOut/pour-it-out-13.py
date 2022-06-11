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
        print(i, j, minvol, ans)
    return sorted(set(ans))[:-2],[i for i in set(ans) if i in option]
u,U = 9,11.25
print(pourMin(u,U))


# filter result of pourMin

def notVolum():
    if x != 0 and x <= u + U:
        return x

#
from itertools import dropwhile

def drop_while(arr, pred):
    return list(dropwhile(pred, arr))

arr = pourMin(u,U),notVolum()
print(drop_while(arr,pred))