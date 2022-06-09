'''
#About Caesar Cipher

Caesar Cipher is a simple encryption technique based on shifting each character by a
fixed number of positions in the alphabet.

For example, if the shift is 3, an encoded version of phrase "kata" will be:

k + 3 = n
a + 3 = d
t + 3 = w
a + 3 = d
In a case when "z" is reached, the algorithm wraps back to "a". Example: "zen", key 3

z + 3 = c
e + 3 = h
n + 3 = q

The key for this cipher can be any non-negative integer. However, because there are
26 letters in English alphabet, any key larger than 26 can be thought about as key = key % 26.

#What to do

Your task is to write a function that will encrypt a phrase using Caesar Cipher and a
given shift key and return it as a string.
However, the key should be increased by 1 with every word in a phrase. For example,
if the function is called with a phrase "divide et impera" and key 3, the encoding
should be as follows:

- Shift the word "divide" by the key of 3
- Shift the word "et" by the key of 3 + 1 = 4
- Shift the word "impera" by the key of 3 + 2 = 5
#Important things to note:

Guaranteed input will be of type string, lowercase characters and spaces only.
Key can be any non-negative integer.
To read more about Caesar Cipher, visit https://en.wikipedia.org/wiki/Caesar_cipher

ALGORITHMSCRYPTOGRAPHYSECURITY

import codewars_test as test
from solution import caesar_encode

@test.describe('Fixed Tests')
def fixed_tests():
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(caesar_encode("alea iacta est", 3), "dohd megxe jxy")
        test.assert_equals(caesar_encode("conquer et impera", 13), "pbadhre sh xbetgp")
        test.assert_equals(caesar_encode("fere libenter homines id quod volunt credunt", 7), "mlyl tqjmvbmz qxvrwnb sn bfzo haxgzf perqhag")
        test.assert_equals(caesar_encode("horum omnium fortissimi sunt belgae", 0), "horum pnojvn hqtvkuukok vxqw fipkei")
'''
#4th solve by ericlee

import string
def caesar_encode(phrase, shift):
    ans,bench = '',string.ascii_lowercase #+ ' '
    upper = []
    for e in phrase:
        if e in string.ascii_uppercase:
            upper.append(phrase.index(e))
        if e != " ":
            ans += bench[(bench.index(e.lower()) + shift)%26]
        else:
            ans += " "
            shift += 1
        # trap in " " which index 1 less or ahead of right_postion
    return ''.join([e.upper() if i in upper else e for i,e in enumerate(ans)])

#1st
def code(n):
    if(n > 122):
        return 96 + n - 122
    return n
def check_key(key):
    if key > 26:
        return key % 26
    return key


def caesar_encode(phrase, shift):
    result = ''
    shift = check_key(shift)
    for i in phrase:
        if(i == ' '):
            result += ' '
            shift += 1
            shift = check_key(shift)
        else:
            result += chr(code(ord(i) + shift))
    return result
phrase, shift = "alea iacta est", 3
phrase, shift = "Python", 3
print(caesar_encode(phrase,shift))

print(string.ascii_lowercase)
print(string.ascii_letters)

# 3、index()返回字符串中第一次指定字母的出现位置
print('hello'.index('l'))