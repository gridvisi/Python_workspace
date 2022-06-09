'''
https://www.codewars.com/kata/60cc93db4ab0ae0026761232/train/python
Task
A list S will be given. You need to generate a list T from it by following the given process:

Remove the first and last element from the list S and add them to the list T.
Reverse the list S
Repeat the process until list S gets emptied.
Example
S = [1,2,3,4,5,6]
T = []

S = [2,3,4,5] => [5,4,3,2]
T = [1,6]

S = [4,3] => [3,4]
T = [1,6,5,2]

S = []
T = [1,6,5,2,3,4]
return T
Note
size of S goes up to 10^6
Keep the efficiency of your code in mind
Don't mutate the input
'''

#25th by ericlee
def arrange(s):
    lft,rht = 0, len(s)-1
    step,l = 0,len(s)-1
    ans = []
    while step <= l//2:
        sl = s[lft + step],s[rht - step]
        if step%2 == 1:sl=sl[::-1]
        ans.extend(sl)
        step += 1

    if len(s)%2 == 1:
        return ans[:-1]
    else:return ans

s = [4, 3, 2]
#s = [2, 4, 3, 4]
s = [9, 7, -2, 8, 5, -3, 6, 5, 1]  #[9, 1, 5, 7, -2, 6, -3, 8, 5]
print(arrange(s))

#1st
from collections import deque

def arrange(s):
    q=deque(s)
    return [q.pop() if 0<i%4<3 else q.popleft() for i in range(len(s))]

#2nd
arrange=lambda s:[s[[i,-i,~i,i][i%4]//2]for i in range(len(s))]

#3rd
def order():
    p, n = 0, -1
    while True:
        yield p
        p += 1
        yield n
        n -= 1
        yield n
        n -= 1
        yield p
        p += 1

def arrange(s):
    return [s[i] for i, _ in zip(order(), s)]

#4th
def arrange(s):
    t = []
    left, right = 0, len(s)-1
    for i in range(len(s)):
        if ((i+1)//2) % 2 == 0:
            t.append(s[left])
            left += 1
        else:
            t.append(s[right])
            right -= 1
    return t

#5th
def arrange(s):
    t = []

    for i in range(len(s) // 2):
        if i % 2 == 0:
            t.extend([s[i], s[~i]])
        else:
            t.extend([s[~i], s[i]])

    if len(s) % 2 == 1:
        t.append(s[len(s) // 2])

    return t