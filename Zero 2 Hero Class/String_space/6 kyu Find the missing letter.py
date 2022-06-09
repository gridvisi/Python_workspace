'''
https://www.codewars.com/kata/find-the-missing-letter/python

#Find the missing letter

Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e' ['O','Q','R','S'] -> 'P'

["a","b","c","d","f"] -> "e"
["O","Q","R","S"] -> "P"
(Use the English alphabet with 26 letters!)

Have fun coding it and please don't forget to vote and rank this kata! :-)

I have also created other katas. Take a look if you enjoyed this kata!
test.assert_equals(find_missing_letter(['a','b','c','d','f']), 'e')
test.assert_equals(find_missing_letter(['O','Q','R','S']), 'P')

ALGORITHMSMATHEMATICSNUMBERS
'''

def find_missing_letter(chars):
    n = 0
    while ord(chars[n]) == ord(chars[n+1]) - 1:
        n += 1
    return chr(1+ord(chars[n]))

def find_missing_letter(input):
    alphabet = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    start = alphabet.index(input[0])
    for i in range(len(input)):
        if not input[i] == alphabet[start+i]:
            return alphabet[start+i]

def find_missing_letter(chars):
    st_nd,re = [],[]
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    alpha = ''.join([i.upper() for i in alpha]) + alpha
    print(alpha)
    for i,e in enumerate(alpha):
        if e in (chars[0], chars[-1]):
            st_nd.append(i)
    for e in alpha[st_nd[0]:st_nd[1]+1]:
        if e not in chars:
            return e