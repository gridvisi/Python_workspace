'''
https://www.codewars.com/kata/find-the-parity-outlier/train/python
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
'''
integers = [160, 3, 1719, 19, 11, 13, -21]
def find_outlier(integers):
    arr_odd,arr_even = [],[]
    for i,x in enumerate(integers):
        if x%2 == 1:
            arr_odd.append(x)

        elif x%2 == 0:
            arr_even.append(x)
    if len(arr_even) > len(arr_odd):
        return arr_odd[0]
    else:return arr_even[0]

def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]

def find_outlier(integers):
    parity = [n % 2 for n in integers]
    return integers[parity.index(1)] if sum(parity) == 1 else integers[parity.index(0)]

def find_outlier(integers):
    even = filter(lambda x: x % 2 == 0, integers)
    return even[0] if len(even) == 1 else list(set(integers) - set(even))[0]
print(find_outlier(integers))