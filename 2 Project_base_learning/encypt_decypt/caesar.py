
#Step-1

print((ord('a') - ord('A')))

import string
print(chr(110))
print(ord('l'))
print('alphabet:',[ord(x) for x in string.ascii_lowercase])

xs = 'jerryisspy'
step = -17

xs = 'jerryisspy'

step  = -17

def shift(xs,step):
    res =  ''
    for i in xs:
        x_asc = chr(ord(i) + step)
        #res += x_asc  # 为何这样写
        print('step by step:',i,res)
        res = res + x_asc
    return res
xs = 'jerryisspy'
step = -17
print(shift(xs,step))
#'jerryisspy'  -> YTaahXbb_h

def shift(x, step):
    x_asc = chr(ord(x) + step)
    return x_asc
x,step = 'W',4
print(f"'{x}'shift'{step}'s space:",shift(x,step))


alphabet = "abcdefghijklmnopqrstuvwxyz "
print(alphabet.find(" "),len(alphabet))
# convert between letters and numbers up to 26
def number_to_letter(i):
	return alphabet[i % 26]    # %26 does the wrap-around
i = 27
print(number_to_letter(i),len(alphabet))
#  /  % //

def letter_to_number(l):
	return alphabet.find(l)  # index in the alphabet
print(letter_to_number('l'))

# How to encode a single character (letter or not)
def caesar_shift_single_character(l, amount):
    i = letter_to_number(l)
    if l == " ":  # character not found in alphabet
        return " "  # remove it, it's space or punctuation
    else:
        return number_to_letter(i + amount)  # Caesar shift

# How to encode a full text
def caesar_shift(text, amount):
    shifted_text = ""
    for char in text.lower():
        # also convert uppercase letters to lowercase
        shifted_text += caesar_shift_single_character(char, amount)
    return shifted_text
text = 'apple'
amount = 3
print('加过密的文本',caesar_shift(text, amount))

text = 'oxfdv'
re = []
for i in range(28):
    re.append(caesar_shift(text, i))
print('加过密的文本',re)

    ### MAIN PROGRAM ###


message = """

    Once upon a midnight dreary, while I pondered, weak and weary,
    Over many a quaint and curious volume of forgotten lore—
    While I nodded, nearly napping, suddenly there came a tapping,
    As of some one gently rapping, rapping at my chamber door—
    "'Tis some visitor," I muttered, "tapping at my chamber door—
    Only this and nothing more."

    """
message = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"
#http://www.pythonchallenge.com/pc/def/map.html

"i hope you didnt translate it by handb thats what computers are forb doing it in " \
"by hand is inefficient and thatbs why this text is so longb using stringbmaketransbb " \
"is recommendedb now apply on the url"

code = caesar_shift(message, 2)
print(code)  # 输出结果

import string

s = 'abcd--dcba'

# 参数from和to的长度必须一致
#table = string.maketrans('', '')  # type(table) is 'str'
#print(s.translate(table))



'''
"qpegwrqpcokfpkijvftgctayjkngkrqpfgtgfygcmcpfygctaqxgtocpacswckpvcpfewtkqwuxqnwogqhhqtiqvvgpnqtgyjkngkpqffgf
pgctnapcrrkpiuwffgpnavjgtgecogcvcrrkpicuqhuqogqpgigpvnatcrrkpitcrrkpicvoaejcodgtfqqtvkuuqogxkukvqtkowvvgtgfv
crrkpicvoaejcodgtfqqtqpnavjkucpfpqvjkpioqtg"
# 练手之二 密码中出现次数最多的字母是？
'''
text = code
alphabet = "abcdefghijklmnopqrstuvwxyz"

def count_most(text):  # a-z遍历26字母表
    bench, res = 0, sorted(text)
    for e in alphabet:
        # e_most是出现次数最多的字母，bench是出现总次数
        if res.count(e) > bench:
            bench = res.count(e)
            e_most = e
    return e_most, bench
text = "In this article, you will learn the fundamentals of Sets in Python. This is a very powerful built-in data type that you can use in your Python projects."
print(count_most(text))

def count_most(text):
    bench, res = 0, sorted(text)
    for e in set(text):
        # e_most是出现次数最多的字母，bench是出现总次数
        if res.count(e) > bench and e != " ":
            bench = res.count(e)
            e_most = e
    return e_most, bench
print(count_most(text))

