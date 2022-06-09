'''
https://www.codewars.com/kata/5a24254fe1ce0ec2eb000078/train/python

Test.it("Basic tests")
Test.assert_equals(solve("((1)23(45))(aB)",0),10)
Test.assert_equals(solve("((1)23(45))(aB)",1),3)
Test.assert_equals(solve("((1)23(45))(aB)",2),-1)
Test.assert_equals(solve("((1)23(45))(aB)",6),9)
Test.assert_equals(solve("((1)23(45))(aB)",11),14)
Test.assert_equals(solve("(g(At)IO(f)(tM(qk)YF(n)Nr(E)))",11),28)
Test.assert_equals(solve("(g(At)IO(f)(tM(qk)YF(n)Nr(E)))",0),29)
Test.assert_equals(solve("(>_(va)`?(h)C(as)(x(hD)P|(fg)))",19),22)
'''
# Parentheses 括号
def solve(st, idx):
    if st[idx] not in "()":return -1
    flag = 0
    for i,p in enumerate(st[idx:]):
        if p == '(':
            flag += 1
        elif p == ')':
            flag -= 1
        if flag == 0:
            return i + idx
    if flag > 0:
        return -1
st, idx = "((1)23(45))(aB)",0 # 10
st, idx = "((1)23(45))(aB)",6
print(st[0:])
print(solve(st, idx))
