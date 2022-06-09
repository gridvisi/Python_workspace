'''
https://www.codewars.com/kata/5ce969ab07d4b7002dcaa7a1/train/python

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


def solve(st):
    ans = 0
    for i in range(1, len(st) // 2 + 1):
        if st[0:i] == st[len(st) - i:]:
            ans = i
        continue
    return ans

#1st
def solve(st):
    return next((n for n in range(len(st)//2, 0, -1) if st[:n] == st[-n:]), 0)