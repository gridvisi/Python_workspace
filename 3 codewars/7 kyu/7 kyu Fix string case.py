'''

In this Kata, you will be given a string that may have mixed uppercase and lowercase letters and your task is to convert that string to either lowercase only or uppercase only based on:

make as few changes as possible.
if the string contains equal number of uppercase and lowercase letters, convert the string to lowercase.
For example:

solve("coDe") = "code". Lowercase characters > uppercase. Change only the "D" to lowercase.
solve("CODe") = "CODE". Uppercase characters > lowecase. Change only the "e" to uppercase.
solve("coDE") = "code". Upper == lowercase. Change all to lowercase.
More examples in test cases. Good luck!

Please also try:
Simple time difference
Simple remove duplicates

Test.it("Basic tests")
Test.assert_equals(solve("code"),"code")
Test.assert_equals(solve("CODe"),"CODE")
Test.assert_equals(solve("COde"),"code")
Test.assert_equals(solve("Code"),"code")

FUNDAMENTALS
'''
def solve(s):
    return s.upper() if sum(map(str.isupper, s)) * 2 > len(s) else s.lower()


def solve(s):
    upper = 0
    lower = 0
    for char in s:
        if char.islower():
            lower += 1
        else:
            upper += 1
    if upper == lower or lower > upper:
        return s.lower()
    else:
        return s.upper()

def solve(s):  #mcree
    s = list(s)
    big = 0
    small = 0
    for i in s:
        if ord(i) > 64 and ord(i) < 91:
            big += 1
        if ord(i) > 96 and ord(i) < 123:
            small += 1
    if big > small:
        return ''.join(s).upper()
    elif small > big or small == big:
        return ''.join(s).lower()