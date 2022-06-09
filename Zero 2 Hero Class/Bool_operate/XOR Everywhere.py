'''
https://brilliant.org/problems/xor-everywhere/
'''

def mysterious(a,b,c):
    a = a ^ b ^ c
    b = a ^ b ^ c
    c = a ^ b ^ c
    a = a ^ b ^ c
    return pow(a,b) + c
#b**c + a
a,b,c = 0,0,0
print(mysterious(a,b,c))