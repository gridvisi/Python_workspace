def nth_smallest(arr, pos):
    return sorted(arr)[pos-1]
print(nth_smallest([3,1,2],2))