'''
https://www.codewars.com/kata/5fad2310ff1ef6003291a951/train/python

# One of the possible solutions: W = [-10, -1, -1, 1, 1, 1]
# 1*(-10) + 2*(-1) + 3*(-1) + 4*1 + 5*1 + 6*1
weigh_the_list([1, 2, 3, 4, 5, 6])

# One of the possible solutions: W = [4, 1]
# -13*4 + 52*1 = 0
weigh_the_list([-13, 52])

# One of the possible solutions: W = [1, 1]
# -1*1 + 1*1 = 0
weigh_the_list([-1, 1])
'''
a = [1, 2, 3, 4, 5, 6]


#1st
def weigh_the_list(a):
    return [w for i in range(0, len(a), 2) for w in [a[i + 1], -a[i]]]
a = [2, 7, 3, 11, 5, 23, 47, 3]
a = [1, 2, 3, 4, 5, 6]
print(weigh_the_list(a))


#2nd
def weigh_the_list(a):
    array1, array2 = a[:(len(a) // 2)], a[(len(a) // 2):]
    return ([-x for x in array2] + array1)
a = [2, 7, 3, 11, 5, 23, 47, 3]
print(weigh_the_list(a))

def weigh_the_list(a):
    numEntries = len(a)
    Weights = []
    # Make sure that their sum is zero pairwise
    # For example, make sure that first and second elements summed are zero, then third and forth, etc
    for i in range(int(numEntries/2)):
        A = a[2*i]
        B = a[2*i+1]
        Weights.append(B)
        Weights.append(-A)
    return Weights
a = [2, 7, 3, 11, 5, 23, 47, 3]
a = [1, 2, 3, 4, 5, 6]
print(weigh_the_list(a))



from collections import Counter
def weigh_the_list(a):
    a_sort = sorted(a)
    arr = Counter(a)
    mid = [a[i] for i in range(len(a)) if sum(a[0:i]) < sum(a)//2]
    gap = sum(a) - sum(mid) * 2
    print(gap,mid)
    for n in a_sort:
        if gap % n == 0:
            arr[n] += gap//n
            return arr,[e if i < len(mid) else -e for i,e in enumerate(arr.values())]
        else:
            arr[n] = - gap//n
            gap = gap % n
            if gap == 0:
                return arr,[e if i < len(mid) else -e for i, e in enumerate(arr.values())]

