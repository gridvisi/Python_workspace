def invite_more_women(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum > 0
print(invite_more_women([1,-1,1]))