'''
https://www.codewars.com/kata/530017aac7c0f49926000084/train/python

@test.describe('Example Tests')
def example_tests():
    objs = [{'a':1, 'b':2, 'c': 3}, {'a':4, 'b':5, 'c': 6}, {'a':7, 'b':8, 'c': 9}, {'a':10, 'b':11}]

    test.assert_equals(pluck(objs, 'a'), [1,4,7,10])
    test.assert_equals(pluck(objs, 'b'), [2,5,8,11])
    test.assert_equals(pluck(objs, 'c'), [3,6,9,None])
'''

def pluck(objs, name):
    return [d[name] if name in d.keys() else None for d in objs ]
objs, name = [{'a':1, 'b':3}, {'a':2}], 'b'

# 1st solution
def pluck(objs, name):
    return [item.get(name) for item in objs]

def pluck(objs, name):
    return [x.get(name, None) for x in objs]

def pluck(objs, name):
    return [d.get(name,None) for d in objs]
print(pluck(objs, name))