'''
https://www.codewars.com/kata/5a433c7a8f27f23bb00000dc/train/python
'''

def split_by_value(k, elements):
    left,right = [],[] #left=right=[] is not wrong!
    for i in elements:
        if i < k:
            left.append(i)
        else:
            right.append(i)

    return left+right

k,elements = 5, [1, 3, 5, 7, 6, 4, 2]

def split_by_value(k, elements):
    return sorted(elements, key=lambda x: x >= k)

print(split_by_value(k, elements))

