'''
https://www.codewars.com/kata/574b1916a3ebd6e4fa0012e7/train/python

test.assert_equals(is_opposite("ab","AB") , True);
test.assert_equals(is_opposite("aB","Ab") , True);
test.assert_equals(is_opposite("aBcd","AbCD") , True);
test.assert_equals(is_opposite("AB","Ab") , False);
test.assert_equals(is_opposite("","") , False);
'''
a,b = '',''
print(list(a),list(b),list(a)==list(b))

a,b = 'aB','Ab'
print(list(a),list(b),list(a) or list(b),a or b)

def is_opposite(s1,s2):
    if s1==s2=='':return False
    return all(x != y for x,y in zip(list(s1),list(s2)))
s1,s2 = "",""
print(is_opposite(s1,s2))

#1st
def is_opposite(s1, s2):
    return False if not(s1 or s2) else s1.swapcase() == s2

def is_opposite(s1,s2):
    return s1!="" and s1.swapcase() == s2