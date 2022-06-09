'''
https://www.codewars.com/kata/595b3f0ad26b2d817400002a/train/python
Write a function that accepts two inputs: message and code and returns hidden message decrypted from message using the code.
The code is a nonnegative integer and it decrypts in binary the message.

Grille("abcdef", 5)  => "df"

message : abcdef
code    : 000101
----------------
result  : df
'''

print(bin(10))
print(bin(77098)) #binary

print('2 pow:',2**0 + 2**1 + 2**2 + 2**3)
print(2**1 + 2**4)

name = {'ada':['female','92','97','93'],'eric':'male'}
# 数据结构
# 算法

def grille(message, code):
    c = bin(code)[2:]
    flag = len(message)*[0]
    print(c)
    print(len(c),len(flag),len(list(zip(c,flag))),list(zip(c,flag)),flag)
    #
    if len(flag) > len(c):
        c = (len(flag)-len(c))*'0' + c
    elif len(flag) < len(c):
        c = (len(c)-len(flag))*'0' + c
    indx = [(int(x) + y) for x, y in zip(c, flag)]
    #print(indx,len(indx))
    return ''.join([message[i] for i,e in enumerate(indx) if e == 1])

message, code = "tcddoadepwweasresd", 77098
message, code = "abcde", 32
message, code = "ab", 255
message, code = "abcd", 1
message, code = "ab", 256
print(grille(message, code))

#1
def grille(msg, code):
    return ''.join(msg[-1-i] for i,c in enumerate(bin(code)[::-1]) if c == '1' and i < len(msg))[::-1]

#2
def grille(message, code):
    binary = bin(code)[2:][-len(message):].zfill(len(message))
    return ''.join(char for char, code in zip(message, binary) if code == '1')

#3
def grille(m, c):
    return "".join(i[0] for i in zip(m[::-1],bin(c)[2:][::-1]) if i[1]=="1")[::-1]

