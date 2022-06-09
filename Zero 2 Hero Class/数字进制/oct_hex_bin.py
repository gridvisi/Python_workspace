'''

有个数学笑话是万圣节等于圣诞节（Oct 31=Dec 25）
现在尝试用python“验证”这个笑话！​
八进制的31是否等于10进制的25

print(oct(8),oct(16),oct(32))
ouput:0o10 0o20 0o40

'''


print(oct(8),oct(16),oct(31))
print(oct(25))

#(11101011)_2=(?)_8
print(int('0b11101011',2))
print(oct(int('0b11101011',2)))

import string
def convert(n,x,ans):
    #n为待转换的十进制数，转换为x进制的数，取值为2-32
    ntox_dict = {2:'0b',8:'0o',16:'0x'}
    basefull = string.digits + string.ascii_lowercase
    #print(basefull)
    if (n>=0) and (n<x):
        ans = basefull[n]+ans
        return ntox_dict.get(x,f"{n} to {x}"+"进制是：") + ans
    else:
        ans = basefull[n % x] + ans
        return convert(n//x,x,ans)
n = 100 #十进制的100
x = 8   #转换为8进制
print(convert(n,x,ans=''))

n = 37  #十进制的37
x = 16  #转换为16进制
print(convert(n,x,ans=''))

n = 18  #十进制的18
x = 17  #转换为17进制
print(convert(n,x,ans=''))

#2
import string
def count_digit(number, digit, base=10, from_base=10):

    digs = string.digits + string.ascii_lowercase
    num = int(number, from_base)
    out = ''
    while num:
        out = digs[num % base] + out
        num = num // base
    if not out:
        out = '0'
    return out.count(digit)
number,digit,base,from_base = 10,8,8,10
#print(count_digit(number, digit, base=10, from_base=10))
