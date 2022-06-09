def positive_sum(arr):
    output = []
    for i in range(len(arr)):
        if arr[i] >= 0:
            output.append(arr[i])
    return sum(output)
print(positive_sum([1,-2,3,4,5]))