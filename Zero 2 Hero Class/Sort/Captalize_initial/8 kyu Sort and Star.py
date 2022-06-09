'''
https://www.codewars.com/kata/57cfdf34902f6ba3d300001e/train/python
'''

array = ["Lets", "all", "go", "on", "holiday", "somewhere", "very", "cold"]
def two_sort(array):
    return '***'.join(list(min(array)))
print(two_sort(array))