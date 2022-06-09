'''
https://www.codewars.com/kata/59d9ff9f7905dfeed50000b0/train/python

Test.it("Basic tests")
Test.assert_equals(solve(["abode","ABc","xyzD"]),[4,3,1])
Test.assert_equals(solve(["abide","ABc","xyz"]),[4,3,0])
Test.assert_equals(solve(["IAMDEFANDJKL","thedefgh","xyzDEFghijabc"]),[6,5,7])
Test.assert_equals(solve(["encode","abc","xyzD","ABmD"]),[1, 3, 1, 3])
'''
import string
print("IAMDEFANDJKL".lower())
print("IAMDEFANDJKL".index('I'))
print(string.ascii_letters)
s = string.ascii_lowercase
print(s.index('a'))
print("thedefgh".find('e'))

def stringIndex(x):
    return string.ascii_uppercase.index(x.upper())
print(stringIndex('x'))

def solve(arrs):
    ans = []
    for arr in arrs:
        cunt = 0
        arr = arr.upper()
        #print(arr)
        for i,c in enumerate(arr):
            if c == string.ascii_uppercase[i]:
                cunt += 1
        ans.append(cunt)
    return ans
arr = ["abode","ABc","xyzD"]
#arr = ["abide","ABc","xyz"]
#arr = ["encode","abc","xyzD","ABmD"]
arr = ["IAMDEFANDJKL","thedefgh","xyzDEFghijabc"]  #[6,5,7]
#arr = "IAMDEFANDJKL"
#arr = ['ABC','EFG']
print(solve(arr))


#1st solution
def solve(arr):
    return [ sum(c == chr(97+i) for i,c in enumerate(w[:26].lower())) for w in arr ]

#2nd solution 
from operator import eq
from string import ascii_lowercase
def solve(strings):
    return [sum(map(eq, s.lower(), ascii_lowercase)) for s in strings]

'''
        s = s.upper()
        print(s)
        m = [s[stringIndex(x)]==x for x in s if stringIndex(x)<len(s)]
        k = [stringIndex(x) for x in s if stringIndex(x)<len(s)]
        n = sum([s[stringIndex(x)]==x for x in s if stringIndex(x)<len(s)])
        ans.append(n)
for e in arr:
    print(string.ascii_uppercase.index(e.upper()))
'''