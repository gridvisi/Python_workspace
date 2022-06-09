'''
https://www.codewars.com/kata/52dbae61ca039685460001ae/train/python
'''
st = "a   **&  cZ" # =>  "10100000000000000000000001"
st = ''
st = "&%&%/$%$%$%$%GYtf67fg34678hgfdyd"
import string
def change(st):
    res = [''] * 26
    alph = string.ascii_letters[:27]
    re = [alph.index(i.lower()) if i.lower() in alph else '0' for i in st]
    for i,e in enumerate(res):
        if i in re: res[i] = '1'
        else:
            res[i] = '0'
    return ''.join(res)

def change(st):
    new = ""
    st = st.lower()
    for letter in "abcdefghijklmnopqrstuvwxyz":
        if letter in st:
            new += "1"
        else:
            new += "0"
    return new
print(change(st))

def change(s):
    s = set(s.lower())
    return "".join("1" if x in s else "0" for x in map(chr, range(97, 123)))

ABC = "abcdefghijklmnopqrstuvwxyz"
def change(s):
    s = set(s.lower())
    return "".join(str(int(char in s)) for char in ABC)

def change(st):
    return "".join(["1" if chr(i + 97) in st.lower() else "0" for i in range(26)])

from string import ascii_lowercase


def change(st):
    source = st.lower()
    return ''.join('1' if q in source else '0' for q in ascii_lowercase)