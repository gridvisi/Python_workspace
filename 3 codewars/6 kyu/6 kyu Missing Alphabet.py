'''
https://www.codewars.com/kata/missing-alphabet/train/python
Example:
input: "holly"
missing letters: "a,b,c,d,e,f,g,i,j,k,m,n,p,q,r,s,t,u,v,w,x,z"
output: "hIJKMNPQRSTUVWXZoPQRSTUVWXZlMNPQRSTUVWXZlyZ"
'''
st = 'abc'
it = iter(st)
print(list(it))

name = " Albert Einstein"
str = "If All the bees die on earth, we would die due to not enough food sustain the living"
def name_in_str(str, name):
    it = iter(str.lower())
    it = list(str.lower())
    return all(c in it for c in name.lower())
print(name_in_str(str, name))
import string
def insert_missing_letters(st):
    re = ''
    alpha = [i for i in string.ascii_uppercase[:26]]
    for i in st:
        s = ''.join(alpha).find(i.upper())
        sl = [i for i in alpha[s+1:] if i not in st.upper()]
        re += i + ''.join(sl)
    return re
st = 'holly'
# hIJKMNPQRSTUVWXZoPQRSTUVWXZlMNPQRSTUVWXZlyZ
# hIJKMNPQRSTUVWXZoPQRSTUVWXZlMNPQRSTUVWXZlMNPQRSTUVWXZyZ
print(insert_missing_letters(st))

'''
    alpha = [i for i in string.ascii_uppercase[:26]]
    for i,e in enumerate(alpha):
        if e in st.upper():
            alpha[i] = alpha[i].lower()
    print(alpha)
'''