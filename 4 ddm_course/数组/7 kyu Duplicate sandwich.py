'''
https://www.codewars.com/kata/5f8a15c06dbd530016be0c19/train/python
Task
In this kata you will be given a list consisting of unique elements except for one thing that
appears twice.Your task is to output a list of everything inbetween both occurrences of this
element in the list.

Examples:
@test.describe("Duplicate sandwich")
def tests():
    @test.describe("Basic tests")
    def basic():
        test.assert_equals(duplicate_sandwich([0, 1, 2, 3, 4, 5, 6, 1, 7, 8]), [2, 3, 4, 5, 6])
        test.assert_equals(duplicate_sandwich(['None', 'Hello', 'Example', 'hello', 'None', 'Extra']), ['Hello', 'Example', 'hello'])
        test.assert_equals(duplicate_sandwich([0, 0]), [])
        test.assert_equals(duplicate_sandwich([True, False, True]), [False])
        test.assert_equals(duplicate_sandwich(['e', 'x', 'a', 'm', 'p', 'l', 'e']), ['x', 'a', 'm', 'p', 'l'])
'''
arr = ['e', 'x', 'a', 'm', 'p', 'l', 'e']
arr = ['None', 'Hello', 'Example', 'hello', 'None', 'Extra']
def duplicate_sandwich(arr):
    dup = []
    for i,e in enumerate(arr):
        if e not in dup:
            dup.append(e)
        else:
            #print(i,e)
            return arr[arr.index(e)+1:i]

#1ST
def duplicate_sandwich(arr):
    start, end = [i for i, x in enumerate(arr) if arr.count(x) > 1]
    return arr[start+1:end]
print(duplicate_sandwich(arr))

def duplicate_sandwich(arr):
    i,j = 0,len(arr)-1
    while i <= j:
        if arr[i] == arr[j]:
            return arr[i+1: j+1]
        i += 1
        j -= 1

