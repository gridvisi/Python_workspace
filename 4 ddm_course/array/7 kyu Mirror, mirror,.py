'''
7 kyu
Mirror, mirror, on the wall...
https://www.codewars.com/kata/5f55ecd770692e001484af7d/train/python
mirror([]) == []
mirror([1]) == [1]
mirror([2, 1]) == [1, 2, 1]
mirror([1, 3, 2]) == [1, 2, 3, 2, 1]
mirror([-8, 42, 18, 0, -16]) == [-16, -8, 0, 18, 42, 18, 0, -8, -16]
'''

def mirror(data: list) -> list:
    ... # the solution goes here
    side = sorted(data)
    ans = [side,side[:-1][::-1]]
    return [i for arr in ans for i in arr]

#[x for arr in ans for x in arr]

#list(map(lambda x:''.join(str(x)), (side[:-1],side[-1],side[:-1][::-1])))
data = [-8, 42, 18, 0, -16]
print(mirror(data))

def mirror(data):
    return (s := sorted(data)) + s[-2::-1]

def mirror(data: list) -> list:
    arr = sorted(data)
    return arr + arr[-2::-1]