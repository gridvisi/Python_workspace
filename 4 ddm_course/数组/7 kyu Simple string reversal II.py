'''
https://www.codewars.com/kata/5a8d1c82373c2e099d0000ac/train/python

Test.it("Basic tests")
Test.assert_equals(solve("codewars",1,5),"cawedors")
Test.assert_equals(solve("codingIsFun",2,100),"conuFsIgnid")
solve("codewars",1,5) = "cawedors" -- elements at index 1 to 5 inclusive are "odewa". So we reverse them.
solve("cODEWArs", 1,5) = "cAWEDOrs" -- to help visualize.
'''

def solve(st,a,b):
    rev = list(st)[a:b+1][::-1]
    return ''.join(list(st)[:a] + rev + list(st)[b+1:])
st,a,b = "codewars",1,5
print(solve(st,a,b))

def solve(s,a,b):
    return s[:a]+s[a:b+1][::-1]+s[b+1:]