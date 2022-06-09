'''
https://www.codewars.com/kata/5a262cfb8f27f217f700000b/train/python
'''
a,b = "abcd","xyz" #"abcdxyz"
a,b = 'hello','halo'
a,b = "xyabb","xzca"
def solve(a,b):
    front = set(a+b) - set(b)
    tail = set(a+b) - set(a)
    comm = set(a).intersection(set(b))
    re = [i for i in a+b if i in front or i in tail]
    return ''.join(re)
print(solve(a,b))