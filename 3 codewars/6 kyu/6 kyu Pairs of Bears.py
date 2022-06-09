'''
https://www.codewars.com/kata/pairs-of-bears/train/python

'''
x,s = 3, '88Bifk8hB8BB8BBBB888chl8BhBfd'  #["8BB8B8B88B",True])
for i in range(len(s) - 2):
    if s[i:i+2] == '8B':
        print(s[i:i+2])
    #print(s[i:i+2],type(s[i:i+2]))

def bears(x,s):
    res,cn,ls = '',0,list(s)
    for i in range(len(s) - 1):
        if ls[i:i + 2] == ['8','B'] or ls[i:i + 2] == ['B','8']:
            res += s[i:i + 2]
            ls[i + 1] = '0'
            cn += 1
    if cn >= x: re_bool = True
    else:re_bool = False
    return [res,re_bool]

s = 'FFFffFfFffffFfFFfffFfFFfFFf'

import re
def bears(n, s):
    a = re.findall(r"B8|8B", s)
    return ["".join(a), len(a) >= n]

line = 'FFFffFfFffffFfFFfffFfFFfFFf'
# line是函数的输入参数
import re
n = 90
def reorgan(n, s):
    print(n)
    a = re.findall(r"Ff|fF", s)
    print(a,len("".join(a)))
    return ["".join(a), len("".join(a)) >= n,len("".join(a)),n]
print('overwrite',reorgan(n,line),n)
print(10 > 24)


import re
def  reorgan(line):
    a = re.findall(r"Ff|fF", s)
    return "".join(a)
print(reorgan(line))

'''
    cn = 0
    m = (len(s) - len(''.join(s.split('8B'))))//2
    for i in s.split('8B'):
        if i.split('B8') != 0:
            cn += 1
    res = m*
    return , s.split('8B')
'''