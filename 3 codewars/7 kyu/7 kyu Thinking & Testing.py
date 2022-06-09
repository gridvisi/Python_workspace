'''
https://www.codewars.com/kata/thinking-and-testing-incomplete-string/train/python
'''
'''
#Incomplete string
test.assert_equals(testit("a"), "a", "")
test.assert_equals(testit("b"), "b", "")
test.it("return s.substr(0,1) ?")
test.assert_equals(testit("aa"), "a", "")
test.assert_equals(testit("ab"), "a", "")
test.assert_equals(testit("bc"), "b", "")
test.it("return s.substr(0,s.length/2) ?")
test.assert_equals(testit("aaaa"), "aa", "")
test.assert_equals(testit("aaaaaa"), "aaa", "")
'''
def testit(s):
# return s?
# return s.substr(0,1) ?
# return s.substr(0,s.length/2) ?

    return s.substr(0,s.length/2)
s = "aaaaaa"
print(s.substr(0,1))
print(testit(s))