
'''

Prefix	Interpretation	Base
0b (zero + lowercase letter 'b')
0B (zero + uppercase letter 'B')	Binary	2
0o (zero + lowercase letter 'o')
0O (zero + uppercase letter 'O')	Octal	8
0x (zero + lowercase letter 'x')
0X (zero + uppercase letter 'X')	Hexadecimal
'''
print(0o10) #8
print(0x10) #16
print(0b10) #2

'''
深入浅出。浮点数表示法

下面是关于Python内部如何表示浮点数的更深入的信息。你可以很容易地在Python中使用浮点数，
而不需要了解到这个层次，所以如果这些信息看起来过于复杂，也不用担心。这里介绍的信息是为了防止你好奇。

根据IEEE 754标准，几乎所有平台都将Python浮点数表示为64位 "双精度 "值。在这种情况下，
一个浮点数的最大值大约是1.8 ⨉ 10308。Python会用字符串inf来表示一个大于这个值的数字。
'''
print(1.79e308) #1.79e+308
print(1.8e308)

'''
Complex Numbers
Complex numbers are specified as <real part>+<imaginary part>j. For example:
'''
print(2+3j) #(2+3j)
print(type(2+3j)) #<class 'complex'>

'''
顺序 通常的解释
反斜杠后的字符 "逃 "的解释
\'以单引号开头的定界符结束字符串 单引号(')字样
\"	用双引号开头的定界符终止字符串 双引号(")字样的字符
\终止输入行 忽略新行。
\\ 引入转义序列 字面的反斜杠（）字样。

Escape
Sequence	Usual Interpretation of
Character(s) After Backslash	“Escaped” Interpretation
\'	Terminates string with single quote opening delimiter	Literal single quote (') character
\"	Terminates string with double quote opening delimiter	Literal double quote (") character
\newline	Terminates input line	Newline is ignored
\\	Introduces escape sequence	Literal backslash (\) character
'''

print('a\
... b\
... c')
#a... b... c

print('foo\\bar')
#foo\bar

'''
Escape Sequence	“Escaped” Interpretation
\a	ASCII Bell (BEL) character
\b	ASCII Backspace (BS) character
\f	ASCII Formfeed (FF) character
\n	ASCII Linefeed (LF) character
\N{<name>}	Character from Unicode database with given <name>
\r	ASCII Carriage Return (CR) character
\t	ASCII Horizontal Tab (TAB) character  

逃逸序列 "逃逸 "解释
\一个ASCII贝尔（BEL）字符。
\b ASCII Backspace (BS)字符。
\f ASCII格式输入（FF）字符
\ASCII 线路输入（LF）字符
\ñ{<name>}来自Unicode数据库的字符与给定的<name>。
\r ASCII回车（CR）字符
\t ASCII 水平制表符（TAB）字符

'''

# \uxxxx	Unicode character with 16-bit hex value xxx)
# \Uxxxxxxxx	Unicode character with 32-bit hex value xxxxxxxx
# \v	ASCII Vertical Tab (VT) character
# \ooo	Character with octal value ooo  \xhh	Character with hex value hh
# \uxxxx 16位16进制的Unicode字符 xxxx
# \Uxxxxxxxx Unicode字符，32位16进制值xxxxxxx
# \ASCII垂直制表符（VT）字符
# \oooo 有八进制值的字符 oooo
# \xhh 字符的十六进制值 hh