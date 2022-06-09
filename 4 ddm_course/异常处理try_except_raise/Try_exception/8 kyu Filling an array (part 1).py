'''
https://www.codewars.com/kata/571d42206414b103dc0006a1/train/python

@test.it("Basic Tests")
def basic_tests():
    test.assert_equals(arr(4), [0,1,2,3])
    test.assert_equals(arr(0), [])
    test.assert_equals(arr(), [])
'''
n = ''
def arr(n=0):
    try:
        if n:
            return [i for i in range(n)]
        else:return []
    except:
        n = 0
        return []
n = ''
print(arr(n))

#1st solution
def arr(n=0):
    return list(range(n))