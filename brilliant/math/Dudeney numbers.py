'''
https://brilliant.org/problems/dudeney-numbers/

Dudeney numbers
Computer Science Level 3
A Dudeney number is a positive integer that is a perfect cube such that the sum of its decimal digits is equal to the cube root of the number. There are exactly six such integers, i.e. 1,\, 512,\, 4913,\, 5832,\, 17576,1,512,4913,5832,17576, and 19683:19683:

\left\{ \begin{array}{llll} 1 = {\color{#3D99F6}1}^3 && {\color{#3D99F6}1} = 1\\ 512 = {\color{#3D99F6}8}^3 && {\color{#3D99F6}8} = 5 + 1 + 2\\ 4913 = {\color{#3D99F6}17}^3 && {\color{#3D99F6}17} = 4 + 9 + 1 + 3\\ 5832 = {\color{#3D99F6}18}^3 && {\color{#3D99F6}18} = 5 + 8 + 3 + 2\\ 17576 = {\color{#3D99F6}26}^3 && {\color{#3D99F6}26} = 1 + 7 + 5 + 7 + 6\\ 19683 = {\color{#3D99F6}27}^3 && {\color{#3D99F6}27} = 1 + 9 + 6 + 8 + 3. \end{array} \right.
⎩
1=1
3

512=8
3

4913=17
3

5832=18
3

17576=26
3

19683=27
3
 ​

1=1
8=5+1+2
17=4+9+1+3
18=5+8+3+2
26=1+7+5+7+6
27=1+9+6+8+3.

We can extend the definition to include not only perfect cubes but any perfect power.
A kk-Dudeney number will therefore be any positive integer such that the sum of its
decimal digits is equal to the k^\text{th}k th  root of the number.
'''

def cube_perfect(n):
    ans = []
    for i in range(n):
        if sum([int(x) for x in str(i)])**3 == i:
            ans.append(i)
    return ans
n = 100000
print(cube_perfect(n))

'''
https://brilliant.org/problems/find-the-smallest-10-digit-number-that-is-a/

1026753849
'''
import math
digit = [str(i) for i in range(10)]

start = math.sqrt(1234567890)
start = math.sqrt(1000000000)
end = math.sqrt(9876543210)
print(int(start),int(end))

ans = []
for i in range(int(start),int(end)+1):
    #print(list(str(i**2)))
    #if set(list(str(i**2))) == set(digit):
    if len(set(str(i*i))) == 10:
        ans.append((i,i**2))
print('answer',ans[0])

'''
    if all(str(i) in str(i**2) for i in digit):
        print(i,i**2)
'''

from math import sqrt
# only consider the values from 1,000,000,000 to 10,000,000,000
Start = int(sqrt(1e9)) + 1
End = int(sqrt(1e10))
for n in range(Start, End):
    if len(set(str(n * n))) == 10:
        print(n * n)
        break