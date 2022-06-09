'''
在Python中从字符串中删除特定字符的5种不同方法
1. 删除字符串中的特定字符
2. 从字符串中删除除英文字母以外的所有字符。
3. 删除字符串中除字母和数字外的所有字符
4. 使用正则表达式从字符串中删除所有数字。
5. 删除字符串中除数字外的所有字符
1. 从字符串中删除特定的字符
使用'str.replace'
使用str.replace()，我们可以替换一个特定的字符。如果我们想删除这个特定的字符，
就用一个空字符串来替换这个字符。str.replace()方法将替换上述特定字符的所有出现。

'''
s="Hello$ Python3$"
s1=s.replace("$","")
print (s1)
#Output:Hello Python3




s="Hello$ Python3$"
s1=s.replace("$","",1)
print (s1)
#Output:Hello Python3$


s="Hello$@ Python3&"
s1="".join(c for c in s if c.isalpha())
print (s1)
#Output:HelloPython


s="Hello$@ Python3&"
f=filter(str.isalpha,s)
s1="".join(f)
print (s1)


s="Hello$@ Python3$"
import re
s1=re.sub("[^A-Za-z]","",s)
print (s1)
#Output:HelloPython




s="Hello$ Python3$"
s1=s.replace("$","")
print (s1)

s="Hello$ Python3$"
s1=s.replace("$","",1)
print (s1)

'''
使用're.sub()'
re.sub(pattern, repl, string, count=0, flags=0)
"返回通过替换replate替换字符串中pattern最左边的非重叠出现的地方得到的字符串。如果没有找到pattern，
则返回字符串不变。"
- Python文档
如果我们要删除特定的字符，替换的字符串会被提到一个空字符串。
'''

s="Hello$@& Python3$"
import re
s1=re.sub("[$|@|&]","",s)
print (s1)
#Output:Hello Python3
'''
isalpha() 用于检查字符串是否包含字母。如果它只包含字母表，则返回True。
它将遍历字符串，检查字符串中的每个字符是否是字母，如果是字母，则返回。
s="Hello$@ Python3&"
(c for c in s if c.isalpha())
结果 → ['H', 'e', 'l', 'l', 'o', 'P', 'y', 't', 'h', 'o', 'n'] 。
这是一个生成器表达式。它返回一个包含字符串中所有字母的生成器对象。
s1="".join(c for c in s if c.isalpha())
"".join将使用一个空字符串连接迭代表中的所有元素。
使用'filter()'
'''

s="Hello$@ Python3&"
f=filter(str.isalpha,s)
s1="".join(f)
print (s1)
'''
f=filter(str.isalpha,s)
filter()函数将对字符串中的每个元素应用str.isalpha方法，如果为True，则返回该项目。否则，它将跳过该项。
s1="".join(f)
filter()将返回一个包含字符串中所有字母的迭代器，join()将用一个空字符串连接迭代器中的所有元素。

'''

'''
s1=re.sub("[$|@|&]","",s)
要替换的图案→"[$|@|&]"
[]用于表示一组字符
$|@|& →将匹配$或@或&。
替换字符串以空字符串的形式给出
如果在字符串中发现这些字符，它们将被替换为空字符串
2. 从一个字符串中删除除字母以外的所有字符。
'''
s="Hello$@ Python3&"
s1="".join(c for c in s if c.isalnum())
print (s1)
#Output:HelloPython3
#Using ‘re.sub()’


s="Hello$@ Python3&_"
import re
s1=re.sub("[^A-Za-z0-9]","",s)
print (s1)#Output:HelloPython3
'''
s1=re.sub("[^A-Za-z]","",s)
"[^A-Za-z]" → 会匹配除字母外的所有字符。如果集合的第一个字符是'^'，那么集合中没有的所有字符都会被匹配。
所有匹配的字符将被替换为一个空字符串
除英文字母外的所有字符都被删除了。
3. 从一个字符串中删除除字母和数字以外的所有字符。
使用'isalnum()'
'''
s="Hello$@ Python3$"
import re
s1=re.sub("[^A-Za-z]","",s)
print (s1)
#Output:HelloPython

'''
3. 从一个字符串中删除除字母和数字以外的所有字符。
使用'isalnum()'

isalnum() 用于检查字符串中的字符是否为字母数字（字母 [A-Z, a-z] 和数字 [0-9] 是字母数字）。
它将遍历字符串，检查字符串中的每个字符是否为字母数字，如果是字母/数字，则返回它。
'''

s="Hello$@ Python3&"
s1="".join(c for c in s if c.isalnum())
print (s1)
#Output:HelloPython3
#Using ‘re.sub()’
s="Hello$@ Python3&_"
import re
s1=re.sub("[^A-Za-z0-9]","",s)
print (s1)#Output:HelloPython3

'''
s1=re.sub("[^A-Za-z0-9]","",s)
"[^A-Za-z0-9]" → 会匹配除了字母和数字以外的所有字符。如果集合的第一个字符是'^'，那么集合中没有
的所有字符都会被匹配。
所有匹配的字符将被替换为一个空字符串
除英文字母和数字外，所有的字符都被删除。
4. 使用正则表达式从一个字符串中删除所有数字。
使用're.sub()'
'''
s="Hello347 Python3$"
import re
s1=re.sub("[0-9]","",s)
print (s1)
#Output:Hello Python$

'''
s1=re.sub("[0-9]","",s)
0-9]将匹配0-9的数字。
re.sub("[0-9]","",s,如果找到了，将用空字符串代替。
5. 删除字符串中除数字以外的所有字符
使用'isdecimal()'
isdecimal() 如果字符串中的所有字符都是小数并且至少有一个字符，则返回 True。否则，它返回False。
小数是可以用来组成10进制数字的数字。
'''

s="1-2$3%4 5a"
s1="".join(c for c in s if  c.isdecimal())
print (s1)
#Output:12345

'''
s1="".join(c for c in s if c.isdecimal())
它遍历字符串，检查字符串中的每个字符是否是数字，如果是数字就返回。
"".join()将用一个空字符串连接所有返回的元素。
使用're.sub()'

'''
s="1-2$3%4 5a"
import re
s1=re.sub("[^0-9]","",s)
print (s1)
#Output:12345

'''
s1=re.sub("[^0-9]","",s)
[^0-9]将匹配除数字0-9以外的所有字符。
re.sub("[^0-9]","",s。如果发现任何不是数字的字符，它将被一个空字符串所取代。
使用'filter()'
'''
s="1-2$3%4 5a"
f=filter(str.isdecimal,s)
s1="".join(f)
print (s1)
#Output:12345

'''

f=filter(str.isdecimal,s)
filter()函数将对字符串中的每个元素应用str.isdecimal方法，如果为True，则返回该项。否则，它将跳过该项。
s1="".join(f)
filter()将返回一个包含字符串中所有数字的迭代器，join()将用一个空字符串连接迭代器中的所有元素。
关于filter()与filterfalse()，请参考我的故事。
注意：Python字符串是不可变的，所以所有关于提到的方法都会从字符串中删除字符并返回一个新的字符串。它不会修改原始字符串。
'''

