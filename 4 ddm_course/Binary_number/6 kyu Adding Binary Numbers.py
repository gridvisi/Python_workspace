'''
https://www.codewars.com/kata/55c11989e13716e35f000013/train/python

##Task: You have to write a function add which takes two binary numbers as strings and returns their sum as a string.

##Note:

You are not allowed to convert binary to decimal & vice versa.
The sum should contain No leading zeroes.
##Examples:

add('111','10'); => '1001'
add('1101','101'); => '10010'
add('1101','10111') => '100100'
FUNDAMENTALSBINARYBITS

Test.assert_equals(add('111','10'),'1001')
Test.assert_equals(add('1101','101'),'10010')
Test.assert_equals(add('1101','10111'),'100100')
Test.assert_equals(add('10111','001010101'),'1101100')
Test.assert_equals(add('00','0'),'0')

位运算符	说明
<<	按位左移，左移n位相当于乘以2的n次方
>>	按位右移 ，左移n位相当于除以2的n次方
&	按位与，二进制位数同且为1结果位为1
l	按位或 ，二进制位数或有1结果位为1
^	按位异或 ，二进制位数不同结果位为1
~	按位取反，二进制位0和1结果位互换
'''

print(1 ^ 0)
print(1 ^ 1)
print(0 ^ 0)
print(1 & 0)
print(1 & 1)

def add(a,b):
    if len(a) > len(b):
        b = (1+len(a)-len(b))*'0'+b
    elif len(a)< len(b):
        a = (1+len(b)-len(a))*'0'+a
    #minl = min(len(a),len(b))
    print(a,b)
    ans = [(int(x),int(y)) for x,y in zip(a,b)]
    for i,e in enumerate(ans,-1):
        pass
    return ans
a, b = '1101','10111'
print(add(a,b))

sl = [1,2,3,4]
for i,e in enumerate(sl,-1):
    print([i,e])