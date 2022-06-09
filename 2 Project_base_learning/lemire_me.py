#  https://lemire.me/blog/page/98/
# https://blog.csdn.net/xydqsy/article/details/80195684?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task
'''
​编码：将字符转换为字节的过程
解码：将字节转换为字符的过程
常见的编码有：UTF-8、GBK等
什么是Unicode
Unicode定义了Unicode码点和字符之间的映射关系。一个Unicode码点就是一个非负整数，每个Unicode码点唯一对应一个字符。
目前Unicode码点的范围从 0 到0x10FFFF。由于整数范围足够大，Unicode可以表示任何可见或不可见的字符。

Unicode和UTF-8的关系
Unicode只是定义了Unicode码点和字符之间的映射关系，至于如何在内存中表示Unicode码点，并没有规定。
因此，Unicode是一个映射关系，而不是一套具体的编码。
而UTF-8则定义了如何用字节的方式表示Unicode码点，进而表示了每个字符，因此UTF-8是一套具体的编码方案。
除了UTF-8，基于Unicode的编码还有UTF-16、UTF-32等。

Python与Unicode
python3默认采用utf-8编码，并且可以在字符串中，通过指定unicode码点的方式表示任意合法的Unicode字符，如下所示：
'''
import re
s = 'abcchinaxyz'
str.maketrans('abcxyz','xyzabc')
print(s.translate(str.maketrans('abcxyz','xyzabc')))

s = 'www.qq.com\cgi-bin\ frame_html'
str_strans = str.maketrans(' ',' ',".\-_ ")
print(s.translate(str_strans))


t="éee"
print(t)
print (t.encode('latin-1')) #b'\xe9ee'
print(t.encode('iso-8859-1'))
#print(t.unicode('latin-1'))

'''
1F600   '😀'; GRINNING FACE
1F609   '😉'; WINKING FACE
'''

print(ord('I'),ord('!'),ord('👍'))
s = ' china  '
u = chr(73) + chr(9899) + s + chr(33)
print(u)
print(s.isascii())
print(s.isnumeric())
print(s.islower())
s = '1F609'
print(chr(65))

u = chr(40960) + 'abcd' + chr(1972)
print(u)
print(u.encode('ascii', 'ignore'))
print(s.encode())

#str:
s = "你好"
#unicode:
u = u"你好"

#unicode转化为str，采用encode 编码：
str = u.encode('gbk')

#str转化为unicode ，采用decode 解码：
#unicode = s.decode('gbk')