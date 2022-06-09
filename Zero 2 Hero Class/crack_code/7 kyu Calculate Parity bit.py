'''
https://www.codewars.com/kata/5df261342964c80028345a0a/train/python

A parity bit, or check bit, is a bit added to a string of bits to ensure that the total
number of 1-bits in the string is even or odd. Parity bits are used as the simplest form
of error detecting code.

You have two parameters, one being the wanted parity (always 'even' or 'odd'), and the
other being the binary representation of the number you want to check.

Your task is to return an integer (0 or 1), whose the parity bit you need to add to the
binary representation so that the parity of the resulting string is as expected.

Example:

  Parity: 'even'
  Bin: '0101010'
  Result: 1
Because there is an odd number of 1-bits (3) you need to put another 1 to it to get an
even number of 1-bits.

For more information: https://en.wikipedia.org/wiki/Parity_bit
奇偶校验位，或检查位，是加在一串比特上的一个位，以确保字符串中的1-比特总数是偶数或奇数。奇偶校验位被用作
最简单的错误检测代码。

你有两个参数，一个是想要的奇偶校验位（总是'偶数'或'奇数'），另一个是你想要检查的数字的二进制表示。
你的任务是返回一个整数(0或1)，你需要将其奇偶校验位添加到二进制表示法中，这样产生的字符串的奇偶校验就符合预期。

例子:
  奇偶性: 'even'
  仓：'0101010'
  结果：1
因为有一个奇数的1-bits(3)，你需要再加一个1来得到偶数的1-bits。

更多信息：https://en.wikipedia.org/wiki/Parity_bit
FUNDAMENTALS
'''

def check_parity(parity, bin_str):
    if bin_str.count('1') % 2:
        if parity == "odd":return 0
        else:return 1
    else:
        if parity == "even":return 0
        else:return 1

# short
def check_parity(parity, bin_str):
    return 1 if (bin_str.count('1') % 2) + (parity == 'odd') == 2 else (bin_str.count('1') % 2) + (parity == 'odd')

#3rd solve by ericlee
def check_parity(parity, bin_str):
    return int(bin(bin_str.count('1') % 2 + (parity == 'odd'))[-1])

#1st
def check_parity(parity, bin_str):
    return [0, 1][bin_str.count("1") % 2 == (parity == "even")]

#2rd
def check_parity(parity, bin_str):
    return 1 if bin_str.count('1') % 2 == (parity == 'even') else 0