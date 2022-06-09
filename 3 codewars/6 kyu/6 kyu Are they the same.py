'''
https://www.codewars.com/kata/are-they-the-same/train/python
'''
array1 = [121, 144, 19, 161, 19, 144, 19, 11]
array2 = [132, 14641, 20736, 361, 25921, 361, 20736, 361]

array1 = [121, 144, 19, 161, 19, 144, 19, 11]
array2 = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
import math
def comp(array1, array2):
    if len(array1) == 0 or len(array2) == 0:return False
    re = [i*i for i in array1 if i*i in array2]
    res = [i for i in array2 if i not in re]
    print(res)
    return len(res)== 0 #all(math.sqrt(c) == int(math.sqrt(c)) for c in re)
print(comp(array1, array2))