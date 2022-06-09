'''
We want an array, but not just any old array, an array with contents!
Write a function that produces an array with the numbers 0 to N-1 in it.
For example, the following code will result in an array containing the numbers 0 to 4:

arr(5) // => [0,1,2,3,4]

@test.it("Basic Tests")
def basic_tests():
    test.assert_equals(arr(4), [0,1,2,3])
    test.assert_equals(arr(0), [])
    test.assert_equals(arr(), [])
'''

def arr(n=0):
    return list(range(n))

def arr(n=0):
    return [i for i in range(n)]

def arr(n=0):
    return [*range(n)]

def arr(n=int()): return list(range(int(),n))



