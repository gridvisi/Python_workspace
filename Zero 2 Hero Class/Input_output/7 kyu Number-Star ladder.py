'''
https://www.codewars.com/kata/5631213916d70a0979000066/train/python

Test.describe("pattern")

Test.it("works for some examples")
Test.assert_equals(pattern(3),"1\n1*2\n1**3")
Test.assert_equals(pattern(7),"1\n1*2\n1**3\n1***4\n1****5\n1*****6\n1******7")

pattern(10): should return the following:

1
1*2
1**3
1***4
1****5
1*****6
1******7
1*******8
1********9
1*********10
'''


def pattern(n):
    return '\n'.join([f"1{(i-1)*'*'}{i}" if i > 1 else str(i) for i in range(1,n+1)])

#Not smart with ''.join() instead of '\n'.join()
def pattern(n):
    return ''.join([f"1{(i-1)*'*'}{i}\n" if i > 1 else str(i)+'\n' for i in range(1,n+1)])
n = 4
print(pattern(n))
