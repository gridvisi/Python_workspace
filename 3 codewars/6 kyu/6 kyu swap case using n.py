'''
https://www.codewars.com/kata/5f3afc40b24f090028233490/train/python
swap('Hello world!', 11) == 'heLLO wORLd!'
# because bin(11) is 1011 so the first, third, fourth, fifth, seventh, eighth, and ninth alphabetical characters have cases swapped
'H e l l o  w o r l d !'
'1 0 1 1 1  0 1 1 1 0'
'^   ^ ^ ^    ^ ^ ^   '

swap('', 11345) == ''
swap('the lord of the rings', 0) == 'the lord of the rings'
'''
s,n = 'Hello world!', 11
print(s[-1])
print(s.find('world!'))


import string
print(string.ascii_letters)
#s = [i for i in s if i in string.ascii_letters]
#print(s)
def swap(s,n):
    i,st = 0,list(s)
    l = 1+len(s)//len(str(bin(n))[2:])+len(s)%len(str(bin(n))[2:])
    index = str(bin(n))[2:]*(1+len(s)//len(str(bin(n))[2:]))#[:l]
    print(list(index))
    print(list(s))
    i = j = 0
    while i < len(s):
        if st[i] in string.ascii_letters:
            if index[j] == '1':
                st[i] = st[i].swapcase()
            else:
                pass
            i += 1
            j += 1
        elif st[i] not in string.ascii_letters:
            i += 1
    return st,''.join(st)
#''.join([e.swapcase() if i in index else e for i,e in enumerate(s)])
s,n = 'the quick broWn fox leapt over the fence',9
s,n = 'Hello world!', 11  #'heLLO wORLd!'
print(swap(s,n))


from itertools import cycle
def swap(s,n):
    b = cycle(bin(n)[2:])
    return "".join(c.swapcase() if c.isalpha() and next(b) == '1' else c for c in s)


from itertools import cycle
def swap(s,n):
    doSwap = cycle(map(int,f"{n:b}"))
    return ''.join(c.swapcase() if c.isalpha() and next(doSwap) else c for c in s)

'''
def swap(s,n):
    re,l = '',0
    st = [i for i in s if i in string.ascii_letters]
    index = (str(bin(n))[2:] * (1+len(st)//len(str(bin(n))[2:])))[:len(st)]
    st = [e.swapcase() if index[int(i)] == '1' else e for i,e in enumerate(st)]
    for w in s.split():
        re += ''.join(st[l:l+len(w)])+' '
        l += len(w)
    if len(re[:-1]) == len(s):
        return re[:-1]
    else:
        return re[:-1]+s[-1]

'''