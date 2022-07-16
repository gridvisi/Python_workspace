'''
https://brilliant.org/practice/quicksort/?p=10
'''

def quickSort(arr):
    less = []
    pivotList = []
    more = []
    arr_length = len(arr)
    if arr_length <= 1:
        return arr
    else:
        #pivot = arr[0] # Change this line
        if len(arr) > 2:
            pivot = sorted([arr[0],arr[arr_length // 2],arr[-1]])[1]
        else:
            pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSort(less)
        more = quickSort(more)
        return less + pivotList + more

arr = [57,16,207,94,17,2,138,12,73,103,77]
print(quickSort(arr))