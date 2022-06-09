'''
https://www.codewars.com/kata/57f75cc397d62fc93d000059/train/python
test.assert_equals(calc('ABC'), 6)
test.assert_equals(calc('abcdef'), 6)
test.assert_equals(calc('ifkhchlhfd'), 6)
test.assert_equals(calc('aaaaaddddr'), 30)
test.assert_equals(calc('jfmgklf8hglbe'), 6)
test.assert_equals(calc('jaam'), 12)
test.assert_equals(calc('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'), 96)

  (6 + 5 + 6 + 6 + 6 + 7)
- (6 + 5 + 6 + 6 + 6 + 1)
-------------------------
                       6

# 用户输入字符
c = input("请输入一个字符: ")

# 用户输入ASCII码，并将输入的数字转为整型
a = int(input("请输入一个ASCII码: "))


print( c + " 的ASCII 码为", ord(c))
print( a , " 对应的字符为", chr(a))

ans.replace('7','1')
'''

def calc(x):
    ans = ''
    for i in x:
        ans += str(ord(i))
    seven_count = ans.count('7')     # jaam : 1069797109 ans.replace('7','1')
    return seven_count*6
x = 'jaam'
print(calc(x))


#1st
def calc(s):
    total1 = ''.join(map(lambda c: str(ord(c)), s))
    total2 = total1.replace('7', '1')
    return sum(map(int, total1)) - sum(map(int, total2))

#2nd
def calc(x):
    return ''.join(str(ord(ch)) for ch in x).count('7') * 6