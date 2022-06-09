'''
https://www.codewars.com/kata/5f885fa9f130ea00207c7dc8/train/python
Note:

String can have leading/trailing spaces, you should not count them;
Strings contain only unique characters from a to z;
Order of characters in array doesn't matter;

Good luck!
'a b  c' => ['b']
'a bcs           d k' => ['d']
'    a b  sc     p     t   k'  => ['p']
'a  b  c  de'  => ['b', 'c']
'     a  b  c de        '  => ['b']
'abc' => ['a', 'b', 'c']
'''
strng = 'a bcs           d k'
strng = 'abc d   ef  g   h i j      '
strng = '  abc  d  z    f gk s '

import re
s = strng
sl = list(strng.strip())
s = re.findall(r".\s*", s.strip())
print('s:',s,sl)

import string
def loneliest(strng):
    #indx = [i for i,e in enumerate(strng) if e != ' ']#Your code here
    blank = {}
    strng = strng.strip()
    left, right = 0, 0
    #blank = [strng[:i].count(' ')+strng[i:i+1].count(' ') for i,e in enumerate(strng) if i+1 < len(strng)-1]
    for e in strng:
        #right = 0
        if e in string.ascii_lowercase:
            blank[e] = 0
            #right = 0

            print(e)
            prev = e
            blank[prev] = 0
            #print(left,right,blank)
            left = right
            right = 0

        elif e == ' ':
            right += 1
            #print(prev,left,right)

        blank[prev] = left + right
        maxkey = max([v for k,v in blank.items()])
    return [k for k,v in blank.items() if v == maxkey]
#[max([[k,v] for k,v in blank.items()],key=lambda x:x[1])[0]]            #sorted(blank.items(),key=blank.value())

strng = 'a  b  c  de  '
strng = 'abc d   ef  g   h i j      '
print(loneliest(strng))

# 3rd solution eric solution
def loneliest(strng):
    strng = strng.strip()
    blank = {}
    left, right = 0, 0

    for e in strng:

        if e in string.ascii_lowercase:
            blank[e] = 0
            prev = e

            left = right
            right = 0

        elif e == ' ':
            right += 1
            print(prev,left,right)

        blank[prev] = left + right

    return blank
#[max([[k,v] for k,v in blank.items()],key=lambda x:x[1])[0]]

#1st solution
import re

def loneliest(s):
    s = re.findall(r".\s*", s.strip())
    res = [s[0]]
    for i in range(1, len(s)):
        res.append(s[i-1][1:]+s[i])
    m = len(max(res, key=len))
    return [i.strip() for i in res if len(i) == m]

2# solution


def loneliest(strng):
    spaces = 0
    character = ''
    result = {}
    for c in strng.strip():
        if c == ' ':
            spaces += 1
        else:
            if character: result[character] += spaces
            character = c
            result[character] = spaces
            spaces = 0

    max_spaces = max(result.values())
    return list(filter(lambda c: result[c] == max_spaces, result.keys()))

