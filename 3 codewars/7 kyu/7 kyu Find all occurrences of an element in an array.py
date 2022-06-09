'''
https://www.codewars.com/kata/59a9919107157a45220000e1/train/python
'''

def find_all(array, n):
    it = iter(array)
    return [x for x in range(len(array)) if array[x] == n]

def find_all(array, n):
    return [index for index, item in enumerate(array) if item == n]
array,n = [10, 16, 20, 6, 14, 11, 20, 2, 17, 16, 14], 16
print(find_all(array, n))

def find_all(array, n):
    return [ i for i,v in enumerate(array) if v==n ]

