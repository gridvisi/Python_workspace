'''
https://brilliant.org/daily-problems/pour-it-out-13/
'''
option = [1.5,3.25,5,6.75]

def pourMin(u,U): # u=small, U=larger
    i,j,s = 2,1,True
    ans = [float('INF')]
    minvol = u*i - U*j
    step = 0
    while step < 20:#minvol <= min(ans):
        s = not(s)

        minvol = abs(u*i - U*j)
        i += s
        j += not(s)
        ans.append(minvol)
        print(i, j, minvol, ans)
        step += 1
    return minvol,[i for i in set(ans) if i in option]
u,U = 9,11.25
print(pourMin(u,U))


