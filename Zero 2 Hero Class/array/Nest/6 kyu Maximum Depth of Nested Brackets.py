'''
https://www.codewars.com/kata/60e4dfc1dc28e70049e2cb9d/train/python
'''

# 保证嵌套最深的元素？
def strings_in_max_depth(s):
    if s.count('(')==0:return [s]
    out = []
    max_lr,gap = 0,[]
    l,r,cl,cr = 0,0,0,0

    for i,e in enumerate(s):
        if cr and cl and l < r:
            if cl - cr > max_lr:
                max_lr = cl - cr

                #out.append(s[l + 1:r])
                #cr = -1
                #cl = -1

        if e == '(':
            cl += 1
            l = i

        elif e == ')':
            cr += 1
            r = i
            gap.append([(cl-cr),s[l+1:r]])
    out = sorted(gap,key=lambda x:x[0])  #,max(gap,key=lambda x:x[0])[0]
    #key = out[-1][0]
    return [i[1] for i in gap if i[0] == out[-1][0]]
s = "((AAX(A(x)B)(U(x)P)F(Z)(((y))))(HH))"
#s = "((AAX(AB)(UP)F(Z))(HH))"
#s = "AA(XX((YY))(U))"
#s = "FB(TAIHJK(NZZCGDZXKF(SYMBLACQ)SBJMRFM)PRTRX(JCLYCOXIMOKGGIE)MWIOIJDCLXDSQFHK)WLVYSMNNHIGKR(MOIZLOT(RWMAVXSJQROHJ(GZURPPOQJVMYCE(VCPXSHXQ)LETIEWE(CBC)AAHEEO)NZHIGXBSJATXV)BSBYCMKFFAFZIK(KECNRQ)PIIQZGIDMLNQRQS)VGXXBYD"
# ['VCPXSHXQ', 'CBC']
print(strings_in_max_depth(s))

#1st
def strings_in_max_depth(s):
    start, deepest, lvl, out = 0, 0, 0, [s]

    for i, c in enumerate(s):
        if c == ')':
            if lvl == deepest: out.append(s[start:i])
            lvl -= 1
        elif c == '(':
            lvl += 1
            start = i + 1

        if lvl > deepest:
            out, deepest = [], lvl

    return out


#2
import re

def strings_in_max_depth(s):
    words = []
    depth = 0
    for c in re.split("([()])", s):
        if c == "(":
            depth += 1
        elif c == ")":
            depth -= 1
        elif depth == len(words):
            words.append([c])
        elif depth == len(words) - 1:
            words[-1].append(c)
    return words[-1]

#3
#nice kata!
from collections import defaultdict
def strings_in_max_depth(s):
    depth, d, words, l = 0, defaultdict(list),'', [];
    for i in s:
        if i.isalpha():words+=i
        elif i =="(":
            if words:l.append(words)
            words=''
            depth+=1
        elif i==")":
            l.append(words)
            if l:d[depth].append(l.pop())
            words=''
            depth-=1
    return max(d.items(),key=lambda i:i[0])[1] if d else [words] or ['']

from re import split
from collections import defaultdict
def strings_in_max_depth(s):
    r,c = defaultdict(list),0
    for i in split(r'([()])',s):
        if i=='(': c+=1
        elif i==')': c-=1
        else: r[c].append(i)
    return max(r.items(),key=lambda x:x[0], default=[0,''])[1]

#4
def strings_in_max_depth(s):
    m, n, r = 0, 0, ""
    for c in s:
        if m == n:
            r += c
        if c == '(':
            if m == n:
                r, m = "", m+1
            n += 1
        elif c == ')':
            n -= 1
    return r[:-1].split(')') if r and r[-1] == ')' else [r]

#Try 不能保证嵌套最深的元素？
def strings_in_max_depth(s):
    out = ''
    l,r,cl,cr = 0,0,0,0
    for i,e in enumerate(s):
        if cr and cl and l < r:
            out += s[l + 1:r]
            cr = 0
            cl = 0

        if e == '(':
            cl += 1
            l = i
        elif e == ')':
            cr += 1
            r = i

    return out
s = "((AAX(AB)(UP)F(Z))(HH))"
s = "AA(XX((YY))(U))"
print(strings_in_max_depth(s))


# half done due to recur return in first list
def strings_in_max_depth(s):
    ans = []
    for i in s:
        if isinstance(i,list):
            return strings_in_max_depth(i)
        elif isinstance(i,int):
            ans.append(i)

    return ans,i

s = "((AAX(AB)(UP)F(Z))(HH))"
s = [1,[2,3],[4,5],[6,[7,8],9]]
print(strings_in_max_depth(s))

# replace "()" with "[]"
s = "((AAX(AB)(UP)F(Z))(HH))"
sl = ''
for i in s:
    if i == '(':
        sl += '['
    elif i == ')':
        sl += ']'
    sl += i
print(sl)

#2
sl = ''
for i in list(s):
    if i == '(':
        i = '['
    elif i == ')':
        i = ']'
    sl += i
print(sl)