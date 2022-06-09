
#1 mystr.find(str, start=0, end=len(mystr))
#检测str是否包含在mystr中，如果是返回开始的索引值，否则返回-1.
words = "we have so much need , but finally all we need is to be needed"
print(words.find('need'))
#如何输出need在字符串的起始坐标
for i,e in enumerate(words):
    if words[i:i+4] == 'need':
        print(i)  # why we have three result shown?
print(words.find('need',0,15))

#2 mystr.index(str, start=0, end=len(mystr))
# 跟find()方法一样，只不过如果str不在mystr中会报一个异常.
# 利用find取文件后缀：
file_name = '6 kyu Sort Arrays (Ignoring Case).py'
st = file_name.find('.')
print(file_name[st:])

#3. mystr.count(str, start=0, end=len(mystr))
# 返回str在star和end之间 在mystr里面出现的次数
file_name = '6 kyu Sort Arrays (Ignoring Case).py'
print(file_name.count('py'))

#4. mystr.replace(str1, str2, mystr.count(str1))
# 　把mystr中的str1替换成str2，若果count指定，则替换不超过count次。
#　 注意，替换后的字符串并未赋值给mystr

lauguage = 'life is short ,i love python,so we choose python to learn programming'
print(lauguage.replace('python','c++',lauguage.count('python')))

#5. mystr.split(str, maxsplit)
#　以str为分隔符切片mystr， 如果maxsplit有指定值，则仅分隔maxsplit个字符串
print(lauguage.split())

#6. mystr.capitalize()　　把字符串的第一个字符大写
# . mystr.title()　　把字符串的每个单词首字母大写
print('chongqing'.capitalize(),'chongqing'.title())

#7. mystr.startswith('A')　　检查字符串是否以obj开头，是则返回True，否则返回False.
# . mystr.endswith('.')
print('apple'.startswith('ap'),'apple'.endswith('ple'))

'''
12. mystr.ljust(width)　　返回一个原字符串左对齐，并使用空格填充至长度width的新字符串. 
13. mystr.rjust(width)　　返回一个原字符串右对齐，并使用空格填充至长度width的新字符串. 
　　----请回想print（）左对齐展示和右对齐展示。
14. mystr.center(width)　　返回一个原字符串居中，并使用空格填充至长度width的新字符串. 
15. mystr.lstrip()　　删除mystr字符串左端的空白字符.
16. mystr.rstrip()　　删除mystr字符串末尾的空白字符.
17. mystr.strip()　　删除mystr字符串两端的空白字符.
18. mystr.rfind()　　类似于find()，不过是从右边开始查找.
19. mystr.rindex()　　类似于index()，不过是从右边开始.
20. mystr.partition(str)　　把mystr分割成三部分，str前，str和str后.
21. mystr.rpartition(str)　　类似于partition()，不过是从右边开始.
22. mystr.splitlines()　　 按照行分隔，返回一个包含各行作为元素的列表。
　　----文件的读取
23. mystr.isalpha()　　如果mystr所有字符都是字母则返回True, 否则返回False. 
24. mystr.isdigit()　　如果mystr只包含数字则返回True, 否则返回False. 
25. mystr.isalnum()　 如果mystr所有字符都是字母或数字则返回True, 否则返回False. 
26. mystr.isspace()　如果mystr只包含空格，则返回True, 否则返回False. 
27. str.join(mystr)　　mystr中每个字符后面插入str, 构造出一个新的字符串。 

from translate import Translator
#在任何两种语言之间，中文翻译成英文
#在anconda3下找到Anaconda Prompt终端平台，输入pip install translate，这里的translate包是微软的，翻译良好。等待安装完成即可
#实例在Spyder编辑器中输入以下的示例：
translator=Translator(from_lang="chinese",to_lang="english")
translation = translator.translate("床前明月光，疑是地上霜;举头望明月,低头思故乡")
print(translation)
'''


