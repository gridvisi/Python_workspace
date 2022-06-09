'''
https://www.codewars.com/kata/5966ec8e62d030d8530000a7/train/python
For Example if D=1 and N=10 then the answer would be 45
([0,1,2,3,4,5,6,7,8,9]) If D=2 and N = 3 the answer is 18
which would be the sum of every number in the following:

[
[(0,0), (0,1), (0,2)],
[(1,0), (1,1), (1,2)],
[(2,0), (2,1), (2,2)]
]
'''

def super_sum(D, N):
    s = 0
    for i in range(D+1):
        arr,sub = [i+j for j in range(N)],sum([i+j for j in range(N)])
        print(arr)
        s += sub
    return s,arr
D,N = 3,3
print(super_sum(D, N))