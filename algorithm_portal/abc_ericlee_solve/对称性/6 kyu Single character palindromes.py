'''
https://www.codewars.com/kata/5a2c22271f7f709eaa0005d3/train/python

solve("abba") = "OK". -- This is a palindrome
solve("abbaa") = "remove one". -- remove the 'a' at the extreme right.
solve("abbaab") = "not possible".

你将会得到一个字符串，你的任务是检查是否可以通过删除一个字符将该字符串转换为一个词缀。如果该字符串已经是一个词缀，
返回 "OK"。如果不是，而且我们可以通过删除一个字符将其转换为一个词缀，则返回 "删除一个"，否则返回 "不可能"。
字符的顺序不应改变。比如说

Test.it("Basic tests")
Test.assert_equals(solve("abba"),"OK")
Test.assert_equals(solve("abbaa"),"remove one")
Test.assert_equals(solve("abbaab"),"not possible")
Test.assert_equals(solve("madmam"),"remove one")
Test.assert_equals(solve("raydarm"),"not possible")
Test.assert_equals(solve("hannah"),"OK")
'''
print('abbaa'.replace('a',''))

# 22nd solution by ericlee
def solve(s):
    if s == s[::-1]:return "OK"
    for i in range(len(s)): #why not - 1???
        sPopi = [e for x,e in enumerate(s) if x != i]
        print(''.join(sPopi),''.join(sPopi)[::-1])

        if ''.join(sPopi) == ''.join(sPopi)[::-1]:
            return "remove one"
    return "not possible"
s = "abbaab"
s = "madmam"
s = "-aba-a"
print(solve(s))

# Be careful range(index) differ with c in s
def solve(s):
    if s == s[::-1]:return "OK"
    for i in s:
        sPopi = [x for x in s if x != i]
        print(''.join(sPopi),''.join(sPopi)[::-1])
        if ''.join(sPopi) == ''.join(sPopi)[::-1]:
            return "remove one"
    return "not possible"
s = "abbaab"
#print(solve(s))


#1st solution

def solve(s):
    isOK = lambda x: x == x[::-1]

    return ("OK" if isOK(s) else
            "remove one" if any(isOK(s[:i] + s[i + 1:]) for i in range(len(s))) else
            "not possible")


#2nd solution
def solve(s):
    if s == s[::-1]:
        return 'OK'
    for i in range(len(s)):
        if s[:i] + s[i+1:] == (s[:i] + s[i+1:])[::-1]:
            return 'remove one'
    return 'not possible'

#23th solution
def solve(s):
    if s[::-1] == s:
        return 'OK'

    for i in range(0, len(s)):
        pal = s[:i] + s[i + 1:]
        if pal[::-1] == pal:
            return 'remove one'
    return 'not possible'