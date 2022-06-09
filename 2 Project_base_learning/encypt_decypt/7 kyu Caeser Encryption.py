'''
https://www.codewars.com/kata/56dc695b2a4504b95000004e/train/python

You have invented a time-machine which has taken you back to
ancient Rome. Caeser is impressed with your programming skills
and has appointed you to be the new information security officer.

Caeser has ordered you to write a Caeser cipher to prevent
Asterix and Obelix from reading his emails.

A Caeser cipher shifts the letters in a message by the value
dictated by the encryption key. Since Caeser's emails are very
important, he wants all encryptions to have upper-case output,
for example:

If key = 3 "hello" -> KHOOR If key = 7 "hello" -> OLSSV
Input will consist of the message to be encrypted and the
encryption key.

你发明了一台时间机器，把你带回了古罗马。凯撒对你的编程能力印象深刻，并任命
你为新的信息安全官。

凯撒命令你编写一个凯撒密码，以防止阿斯特里克斯和欧比里克斯阅读他的邮件。

凯撒密码会根据加密密钥所决定的值来转移信息中的字母。由于Caeser的邮件非常
重要，所以他希望所有的加密都有大写的输出，例如。

如果密钥=3 "hello" -> KHOOR 如果密钥=7 "hello" -> OLSSV (大写)

输入的内容包括要加密的信息和加密密钥。

test.describe("Basic Tetsts")
test.assert_equals(caeser("hello world", 0), "HELLO WORLD")
test.assert_equals(caeser("hello", 7), "OLSSV")
'''

def caeser(message, key):
    return "".join( char_if(c,key) for c in message.upper() )

def char_if(char, key):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return alpha[(alpha.index(char)+key)%26] if char in alpha else char

def caeser(message, key):
    return ''.join(chr(65 + (ord(c.upper()) + key - 65) % 26) if c.isalpha() else c for c in message)

from string import maketrans, lowercase, uppercase
def caeser(message, key):
    return message.translate(maketrans(lowercase, uppercase[key:] + uppercase[:key]))
def caeser(message, key):
    return ''.join([chr(ord(i) + key) if i != " " else " " for i in message.uppercase()])

# Not good
def caeser(message, key):
    return ''.join([chr(ord(i) + key - 32) if i != " " else " " for i in message])