'''
https://www.codewars.com/kata/58311faba317216aad000168/train/python

test.describe('Basic Tests')
test.assert_equals(print_nums(), '')
test.assert_equals(print_nums(2), '2')
test.assert_equals(print_nums(1, 12, 34), '01\n12\n34')
test.assert_equals(print_nums(1009, 2), '1009\n0002')

'''
#14th solve by eric
def print_nums(*args):
    if not args:return ''
    elem = [str(i) for i in args]
    start,maxl = args[0],len(max(elem,key=len))
    return '\n'.join([f"{i}".rjust(maxl,'0') for i in elem]),maxl

#关键在 join的括号里是否用\n替代空格

print(print_nums(1, 12, 34))
args = 1009,2
print(f"{args}:",print_nums(*args))

#1st
def print_nums(*arr):
    if not arr: return ''
    ln = len(str(max(arr)))  # cool!
    return '\n'.join(str(c).zfill(ln) for c in arr)


#6th
def print_nums(*nums):
    l = len(str(max(nums, default=0)))  #default is key?
    return "\n".join(f"{n:0{l}d}" for n in nums)  #cool





c = 12345678
print(f'c is {c:015,d}')      # 高位补零，宽度15位，十进制整数，使用,作为千分分割位

'''
>>> a = 1234
>>> f'a is {a:^#10X}'      # 居中，宽度10位，十六进制整数（大写字母），显示0X前缀
'a is   0X4D2   '
 
>>> b = 1234.5678
>>> f'b is {b:<+10.2f}'    # 左对齐，宽度10位，显示正号（+），定点数格式，2位小数
'b is +1234.57  '
 
>>> c = 12345678
>>> f'c is {c:015,d}'      # 高位补零，宽度15位，十进制整数，使用,作为千分分割位
'c is 000,012,345,678'
 
>>> d = 0.5 + 2.5j
>>> f'd is {d:30.3e}'      # 宽度30位，科学计数法，3位小数
'd is           5.000e-01+2.500e+00j'
 
>>> import datetime
>>> e = datetime.datetime.today()
>>> f'the time is {e:%Y-%m-%d (%a) %H:%M:%S}'   # datetime时间格式
'the time is 2018-07-14 (Sat) 20:46:02'


Test Passed
Test Passed
'1\n12\n34' should equal '01\n12\n34'
'1009\n 2' should equal '1009\n0002'
'''