def sum_mix(arr):
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    return sum(arr)
print(sum_mix(['1', '5', '8', 8, 9, 9, 2, '3']))