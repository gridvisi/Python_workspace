# https://www.codewars.com/kata/55749101ae1cf7673800003e/train/python

def pattern(n):
    ans = ''
    for i in range(2,n+1,2):
        ans += i*str(i)+'\n'
    return ans[:-1]
n = 8
print(pattern(n))

#1st
def pattern(n):
    return '\n'.join([str(i) * i for i in range(2, n + 1, 2)])