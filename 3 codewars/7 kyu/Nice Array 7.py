'''
def is_nice(arr):
    sum = 0
    for i in range(0,len(arr)):
        if arr.count(arr[i]-1) or arr.count(arr[i]+1):
            sum += 1
    if sum == 0:
        return False
    elif sum == len(arr):
        return True
    else:
        return False
'''
def is_nice(arr):
    s = 1
    for i in arr:
        if not ((i - 1 or i + 1) in arr):
            s = 0
    if not s:
        return False
    elif s:
        return True
    else:
        return False
print(is_nice([3,4,5,7]))

'''
#best code
def is_nice(arr):
    s = set(arr)
    return bool(arr) and all( n+1 in s or n-1 in s for n in s)
'''