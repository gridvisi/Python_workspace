'''
https://www.codewars.com/kata/57b2020eb69bfcbf64000375/train/python

In this kata you will have to change every letter in a given string to the next letter in
the alphabet.
You will write a function nextLetter (Javascript) / next_letter (Python, Ruby) to do this.
The function will take a single parameter s (string).

Examples:

"Hello" --> "Ifmmp"

"What is your name?" --> "Xibu jt zpvs obnf?"

"zoo" --> "app"

"zzZAaa" --> "aaABbb"
Note: spaces and special characters should remain the same.
Capital letters should transfer in the same way but remain capitilized.

Test.assert_equals(next_letter("Hello"), "Ifmmp")
Test.assert_equals(next_letter("What is your name?"), "Xibu jt zpvs obnf?")
Test.assert_equals(next_letter("zOo"), "aPp")
'''
print(ascii('z'),ascii('Z'))
print(ord('a'),ord('A'),ord('z'),ord('Z'))

import string
def shiftaz(x):
    if x=='z':return 'a'
    if x == 'Z':return 'A'
    if x not in string.ascii_letters:return x
    else:
        return chr(ord(x) + 1)

def next_letter(s):
    return ''.join([shiftaz(e) for e in s ])
s = "What is your name?"
print(next_letter(s))


def next_letter(s):
    alpha = string.ascii_letters
    ans = ''
    for e in s:
        if e == 'z':ans += 'a'
        elif e == 'Z':ans += 'Z'
        elif e in alpha and e not in 'zZ' :
            ans += alpha[alpha.index(e) + 1]
        else:
            ans += e
    return ans
s = "What is your name?"
print(next_letter(s))


#1st
def next_letter(string):
    return "".join(chr(ord(c)+(-25 if c in 'zZ' else 1)) if c.isalpha() else c for c in string)