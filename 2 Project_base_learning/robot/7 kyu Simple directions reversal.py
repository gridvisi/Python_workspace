'''
https://www.codewars.com/kata/5b94d7eb1d5ed297680000ca/train/python
Test.it("Basic tests")
Test.assert_equals(solve(['Begin on 3rd Blvd', 'Right on First Road', 'Left on 9th Dr']), ['Begin on 9th Dr', 'Right on First Road', 'Left on 3rd Blvd'])
Test.assert_equals(solve(["Begin on Road A","Right on Road B","Right on Road C","Left on Road D"]),['Begin on Road D', 'Right on Road C', 'Left on Road B', 'Left on Road A'])
Test.assert_equals(solve(["Begin on Road A"]),['Begin on Road A'])
'''
import string
def solve(arr):
    res = []
    for s in arr[::-1]:
        if s.startswith('Begin'):
            s = s.replace('Begin', 'End')
            res.append(s)
            print(s)
        elif s.startswith('Right'):
            s = s.replace('Right', 'Left')
            res.append(s)
        elif s.startswith('Left'):
            s = s.replace('Left','Right')
            res.append(s)
    return res
arr = ["Begin on Road A","Right on Road B","Right on Road C","Left on Road D"] #['Begin on Road D', 'Right on Road C', 'Left on Road B', 'Left on Road A']
print(solve(arr))