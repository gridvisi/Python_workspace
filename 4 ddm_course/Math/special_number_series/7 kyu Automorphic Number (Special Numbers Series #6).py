'''
https://www.codewars.com/kata/5a58d889880385c2f40000aa/train/python

Test.describe("Basic tests")
Test.assert_equals(automorphic(1),"Automorphic")
Test.assert_equals(automorphic(3),"Not!!")
Test.assert_equals(automorphic(6),"Automorphic")
Test.assert_equals(automorphic(9),"Not!!")
Test.assert_equals(automorphic(25),"Automorphic")
Test.assert_equals(automorphic(53),"Not!!")
Test.assert_equals(automorphic(76),"Automorphic")
Test.assert_equals(automorphic(95),"Not!!")
Test.assert_equals(automorphic(625),"Automorphic")
Test.assert_equals(automorphic(225),"Not!!")
print("<COMPLETEDIN::>")
'''

def automorphic(n):
    ans = eval(str(n)[-1]) ** 2
    return "Automorphic" if str(ans)[-1] == str(n)[-1] else "Not!!"
n = 16
print(automorphic(n))

def automorphic(n):
    return "Automorphic" if str(n*n).endswith(str(n)) else "Not!!"
#past solution
def automorphic(n):
    x = n
    if str(n*n)[-len(str(n)):] == str(n):return "Automorphic"
    else:return "Not!!"