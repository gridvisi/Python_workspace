'''
https://www.codewars.com/kata/5ce969ab07d4b7002dcaa7a1/train/python

In this Kata, you will be given a string and your task will be to return the length of the longest prefix that is also a suffix. A prefix is the start of a string while the suffix is the end of a string. For instance, the prefixes of the string "abcd" are ["a","ab","abc"]. The suffixes are ["bcd", "cd", "d"]. You should not overlap the prefix and suffix.

for example:
solve("abcd") = 0, because no prefix == suffix.
solve("abcda") = 1, because the longest prefix which == suffix is "a".
solve("abcdabc") = 3. Longest prefix which == suffix is "abc".
solve("aaaa") = 2. Longest prefix which == suffix is "aa". You should not overlap the prefix and suffix
solve("aa") = 1. You should not overlap the prefix and suffix.
solve("a") = 0. You should not overlap the prefix and suffix.

Test.it("Basic tests")
Test.assert_equals(solve("abcd"),0)
Test.assert_equals(solve("abcda"),1)
Test.assert_equals(solve("abcdabc"),3)
Test.assert_equals(solve("abcabc"),3)
Test.assert_equals(solve("abcabca"),1)
Test.assert_equals(solve("aaaaa"),2)
Test.assert_equals(solve("aaaa"),2)
Test.assert_equals(solve("aaa"),1)
Test.assert_equals(solve("aa"),1)
Test.assert_equals(solve("a"),0)
'''
#13rd solution by ericlee
def solve(st):
    i = 0
    while i < len(st)//2:
        pref,suff = st[:i+1],st[(len(st)-1-i):]
        print(pref,suff)
        if pref == suff:
            cunt = len(pref)
        i += 1
    return cunt
st = "abcabca"
st = "abcdabc"
st = 'abcda'
print(solve(st))

#1st solution
def solve(st):
    return next((n for n in range(len(st)//2, 0, -1) if st[:n] == st[-n:]), 0)

#2nd solution
def solve(s):
    for i in range(len(s) // 2, 0, -1):
        if s[:i] == s[-i:]:
            return i
    return 0