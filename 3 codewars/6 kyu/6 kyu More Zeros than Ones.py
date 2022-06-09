'''
https://www.codewars.com/kata/5d41e16d8bad42002208fe1a/train/python
创建一个moreZeros函数，该函数将接收一个字符串以供输入，并返回一个数组，该数组只包含
该字符串中的字符，该字符串的ASCII值的二进制表示形式由多于一个的零组成。

您应该删除任何重复的字符，保留任何此类重复的第一次出现，以便它们在最终数组中的顺序与
第一次出现在输入字符串中的顺序相同。

@test.it("Basic tests")
def basic():
    test.assert_equals(more_zeros('abcde'), ['a', 'b', 'd'])
    test.assert_equals(more_zeros('thequickbrownfoxjumpsoverthelazydog'), ['h', 'b', 'p', 'a', 'd'])
    test.assert_equals(more_zeros('THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG'), ['T', 'H', 'E', 'Q', 'I', 'C', 'B', 'R', 'F', 'X', 'J', 'P', 'L', 'A', 'D'])
    test.assert_equals(more_zeros('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_'), ['a', 'b', 'd', 'h', 'p', 'A', 'B', 'C', 'D', 'E', 'F', 'H', 'I', 'J', 'L', 'P', 'Q', 'R', 'T', 'X', '0'])
    test.assert_equals(more_zeros('DIGEST'), ['D', 'I', 'E', 'T'])
'''

print(ascii('a'),bin(ord('a'))[2:])
print(str(bin(ord('D'))[2:]).count('0'),bin(ord('D')))
s = 'DIGEST'
#s = 'thequickbrownfoxjumpsoverthelazydog'
def more_zeros(s):
    return [e for e in s if str(bin(ord(e))[2:]).count('0')- str(bin(ord(e)))[2:].count('1')== 1]
print(more_zeros(s))

def more_zeros(s):
    return
print(more_zeros(s))