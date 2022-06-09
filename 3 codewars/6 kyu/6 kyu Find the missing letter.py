'''
https://www.codewars.com/kata/find-the-missing-letter/train/python
'''
chars = ['a','b','c','d','f']
chars = ['O','Q','R','S']
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

def find_missing_letter(c):
    return next(chr(ord(c[i])+1) for i in range(len(c)-1) if ord(c[i])+1 != ord(c[i+1]))

print(find_missing_letter(chars))

'''
def find_missing_letter(chars):
    st_nd = []
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for i,e in enumerate(alpha):
        if e in (chars[0].lower(),chars[-1].lower()):
            st_nd.append(i)
    return st_nd
    
   for i,e in enumerate(l.lower() for l in chars):
        if e.lower() not in (l for l in alpha[st_nd[0]:st_nd[1]+1]):
            print(alpha[st_nd[0]:st_nd[1]+1])
            pass
            return e
            
    re = map(lambda x:x if x not in chars [x for x in alpha[st_nd[0]:st_nd[1]+1]]))
'''
