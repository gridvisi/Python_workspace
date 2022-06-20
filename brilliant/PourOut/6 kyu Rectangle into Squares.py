'''
https://www.codewars.com/kata/55466989aeecab5aac00003e/train/python

The drawing below gives an idea of how to cut a given "true" rectangle into squares ("true" rectangle meaning that the two dimensions are different).

alternative text

Can you translate this drawing into an algorithm?

You will be given two dimensions

a positive integer length
a positive integer width
You will return a collection or a string (depending on the language; Shell bash, PowerShell, Pascal and Fortran return a string) with the size of each of the squares.

Examples in general form:
(depending on the language)

  sqInRect(5, 3) should return [3, 2, 1, 1]
  sqInRect(3, 5) should return [3, 2, 1, 1]

'''


def sqInRect(lng, wdth):
    # your code
    ans = []
    lng, wdth = sorted([lng,wdth])[::-1]
    if lng == wdth:
        return None
    while True:
        ans.append(wdth)
        if lng - wdth > wdth:
            lng,wdth = lng-wdth,wdth

        elif lng > wdth:
            lng, wdth = wdth, lng-wdth

        elif lng <= wdth:
            #ans.append(wdth)
            return ans

lng, wdth = 5,3
#lng, wdth = 20, 14
lng, wdth = 37, 14
print(sqInRect(lng,wdth))


#2nd
def sqInRect(a, b):
    if a == b:
        return None
    res = []
    while b:
        b, a = sorted([a, b])
        res += [b]
        a, b = b, a - b
    return res

#3rd
# Recursive solution
def sqInRect(lng, wdth, recur = 0):
    if lng == wdth:
        return (None, [lng])[recur]            # If this is original function call, return None for equal sides (per kata requirement);
                                               # if this is recursion call, we reached the smallest square, so get out of recursion.
    lesser = min(lng, wdth)
    return [lesser] + sqInRect(lesser, abs(lng - wdth), recur = 1)

# recursion_2nd
def sqInRect(a, b, inner=False):
    if a < b:
        return sqInRect(b, a, True)
    elif a > b:
        return [b] + sqInRect(a-b, b, True)
    elif inner:
        return [a]

#recursion 3rd_solve
def sqInRect(a, b):
    if a < b:
        a, b = b, a

    if a == b:
        return None
    elif b == 0:
        return []
    else:
        return [b] * (a // b) + sqInRect(b, a % b)


#比较倒水的算法
option = [1.5,3.25,5,6.75]
def pourMin(u, U):   # u=small, U=larger
    i, j, s = 2, 1, True
    ans = [float('INF')]
    minvol = u*i - U*j

    while minvol <= u+U:
        '''minvol <= 两个杯子容量之和'''
        s = not s

        minvol = abs(u*i - U*j)
        i += s
        j += not(s)
        ans.append(minvol)

    return sorted(set(ans)),[i for i in set(ans) if i in option]