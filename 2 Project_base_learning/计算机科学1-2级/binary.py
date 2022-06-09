
print(bin(56))

x = 0b1001
y = '0b1001'
print(int(x))
#print(int(y))
max = 0b11111111
print(max)

import string
print(string.ascii_letters)
s = string.ascii_letters
word = string.ascii_letters + '.,!:'
print(word)
ls = [(ord(i)) for i in word]
#scope = max(ls),min(ls)
test = [i.upper() for i in word]
print(test)
#print(scope)
