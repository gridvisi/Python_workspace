'''
https://www.codewars.com/kata/56f699cd9400f5b7d8000b55/solutions/python

Test.describe("Basic tests")
Test.assert_equals(fix_the_meerkat(["tail", "body", "head"]), ["head", "body", "tail"])
Test.assert_equals(fix_the_meerkat(["tails", "body", "heads"]), ["heads", "body", "tails"])
Test.assert_equals(fix_the_meerkat(["bottom", "middle", "top"]), ["top", "middle", "bottom"])
Test.assert_equals(fix_the_meerkat(["lower legs", "torso", "upper legs"]), ["upper legs", "torso", "lower legs"])
Test.assert_equals(fix_the_meerkat(["ground", "rainbow", "sky"]), ["sky", "rainbow", "ground"])
'''

def fix_the_meerkat(arr):
    return arr[::-1]

def fix_the_meerkat(arr):
    temp = arr[0]
    arr[0] = arr[2]
    arr[2]= temp
    return arr

def fix_the_meerkat(arr):
    #your code here
    newarr = [ arr[2], arr[1], arr[0]]
    return newarr