'''
Given a positive integer n, return first n dgits of Thue-Morse sequence, as a string (see examples).

Thue-Morse sequence is a binary sequence with 0 as the first
element. The rest of the sequece is obtained by adding the
Boolean (binary) complement of a group obtained so far.

For example:

0
01
0110
01101001
and so on...

给定一个正整数n，返回Thue-Morse序列的前n个dgits，作为一个字符串（见例子）。

Thue-Morse序列是一个二进制序列，0是第一个元素。序列的其余部分是通过添加
到目前为止获得的一个组的布尔（二进制）补数而获得的。

比如说

0
01
0110
01101001
以此类推...

先以10进制说明补数的定义：32的补数是100-32，320的补数是1000-320。
所以，一个数的补数就是和这个数相加得到最小的比它高一位的数，这样二进制
数的补数也就清楚了。10011的补数就是100000-10011=11100。

   二进制数的补数的计算方法是：（1）如果原数最后一位为1，则从右往左看，
   这个1不变。其它位数将1变成0，将0变成1。（2）如果原数最后一位为0，
   依然是从右往左看，第一个1出现之前所有的0都不变，第一次出现的1也不变，
   从这个1之后往左所有的位将1变成0，将0变成1。

   注意，二进制补数和计算机的二进制补码并不是同一件事。计算机中二进制数
   都是以补码的形式存储，由于数值有正负之分，因此第一位为符号位。
   设计补码的目的是：（
   1）使符号位能够参与运算；（
   2）将减法转化为加法运算。
   打个比方，如果带有符号位的正数和负数直接进行加法运算，
   得到的数值就一定是比这个负数数值还要小的负数，这显然是不合常理的。
   以一个例子说明：假设计算机处理的位数为8位。
   3 + （-15）= 00000011 + 10001111 = 10010010，十进制为-18，
   就相当于3+15然后去负号。但如果转化为补码，
   3 + （-15）= 00000011 + 11110001 = 11110100，这个数恰好为
   -12（10001100）的补码。而这样运算相当于原码的的3+（-85）。
   刚才已经验证，3+（-85）= -（3+85）=-88，取补码后就是-12。

   当然，补码和本文之前所说的补数也有共通之处，计算机存储的负数的补码就
   和这个数的补数是相等的（第一位不算，因为它使符号位）。当然，正数的补码
   和原数一致。

'''

# Twelfth
import math
def thue_morse(n):
    #p = math.ceil(math.log(n,2))
    start = '01'
    i = 1
    #for _ in range(0,p,2*i):
    while len(start) <= n:
        start += ''.join(['1' if i=='0' else '0' for i in start])
    return start[:n]
n = 2
print(thue_morse(n))
# ValueError: invalid literal for int() with base 10: 'T'
# ValueError: int()的无效字句，基数为10：'T'

#2nd
def thue_morse(n):
    out = "0"
    while len(out) < n:
        out += out.replace('1', '2').replace('0', '1').replace('2', '0')

    return out[:n]

#3rd
def thue_morse(n):
    k = t = 0
    while t.bit_length() < n:
        t = t << 2 ** k | ~t & (1 << 2 ** k) - 1
        k += 1
    return bin(t).replace('b', '')[:n]

#4th
from math import log

def thue_morse(n, s = "0"):
    for _ in range(int(log(n,2))+1): s += s.translate(str.maketrans("01","10"))
    return s[:n]

#5th
def thue_morse(n):
    s = "0"
    while len(s)<n:
        s += "".join([str(int(i)^1) for i in s])
    return s[:n]

