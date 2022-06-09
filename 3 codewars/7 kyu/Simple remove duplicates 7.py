def solve(arr):
    output = []
    for i in range(len(arr)-1,-1,-1):
        if arr[i] not in output:
            output.append(arr[i])
    return output[::-1]
print(solve([1,1,4,5,1,2,1]))