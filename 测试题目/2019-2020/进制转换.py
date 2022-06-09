import os, sys

# global definition
# base = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F]
base = [str(x) for x in range(10)] + [chr(x) for x in range(ord('A'), ord('A') + 6)]


# bin2dec
# 二进制 to 十进制: int(str,n=10)
def bin2dec(string_num):
    return str(int(string_num, 2))


# hex2dec
# 十六进制 to 十进制
def hex2dec(string_num):
    return str(int(string_num.upper(), 16))


# dec2bin
# 十进制 to 二进制: bin()
def dec2bin(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num, rem = divmod(num, 2)
        mid.append(base[rem])

    return ''.join([str(x) for x in mid[::-1]])


# dec2hex
# 十进制 to 八进制: oct()
# 十进制 to 十六进制: hex()
def dec2hex(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num, rem = divmod(num, 16)
        mid.append(base[rem])

    return ''.join([str(x) for x in mid[::-1]])


# hex2tobin
# 十六进制 to 二进制: bin(int(str,16))
def hex2bin(string_num):
    return dec2bin(hex2dec(string_num.upper()))


# bin2hex
# 二进制 to 十六进制: hex(int(str,2))
def bin2hex(string_num):
    return dec2hex(bin2dec(string_num))

print(hex2dec("0xa5"))
print(hex2dec("a5"))

x = 234567888888888888888888
#str_24 = str('{:.0f}'.format(item.get("二十四月内各月还款状况".decode("utf8"))))
str_24 = str('{:.0f}'.format(x))
print(str_24)

# 3.2 * 10 ** -12 = 3.2e-12

#import numpy as np
#np.set_printoptions(suppress=True)

#print（"%e" % x） #可以将number输出为科学计数法

print("foo ' bar")
#print('foo ' bar')
print("""foo ' bar""")

'''
Write an expression for a string literal consisting of the following ASCII characters:
Horizontal Tab character
Newline (ASCII Linefeed) character
The character with hexadecimal value a0
'''

print(ascii(0xa0))