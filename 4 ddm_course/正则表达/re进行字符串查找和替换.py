'''
re.sub()替换功能
re.sub是个正则表达式方面的函数，用来实现通过正则表达式，实现比普通字符串的replace更加强大的替换功能。
简单的替换功能可以使用replace()实现。

'''
def main():
    text = '123, word!'
    text1 = text.replace('123', 'Hello')
    print(text1)

if __name__ == '__main__':
    main()

import re
def main():
    content = 'abc124hello46goodbye67shit'
    list1 = re.findall(r'\d+', content)
    print('list1:',list1)

    mylist = list(map(int, list1))
    print('mylist:',mylist)
    print('sum(mylist):',sum(mylist))

    print(re.sub(r'\d+[shit]', ' for ', content))
    print()
    print(re.sub(r'\d+', '2020', content))

if __name__ == '__main__':
    main()
# ['124', '46', '67']
# [124, 46, 67]
# 237
#abc for ello46goodbye for hit
# abc2020hello2020goodbye2020shit

#


'''
re.match(pat, s)	
只从字符串s的头开始匹配，比如(‘123’, ‘12345’)匹配上了，而(‘123’,’01234’)就是没有匹配上，没有匹配上返回None，匹配上返回matchobject

re.search(pat, s)	
从字符串s的任意位置都进行匹配，比如(‘123’,’01234’)就是匹配上了，只要s只能存在符合pat的连续字符串就算匹配上了，没有匹配上返回None，匹配上返回matchobject

re.sub(pat,newpat,s)	
对字符串中s的包含的所有符合pat的连续字符串进行替换，如果newpat为str,那么就是替换为newpat,如果newpat是函数，那么就按照函数返回值替换。sub函数两个有默认值的参数分别是count表示最多只处理前几个匹配的字符串，默认为0表示全部处理；最后一个是flags，默认为0

import re

s='1中文中文：123456aa哈哈哈bbcc'.decode('utf8')
print(re.match(u"[\u4e00-\u9fa5]+",s))
# None. 只从字符串的开始匹配，没有匹配上返回None,否则返回matchobject

pat='中文'.decode("utf8")
print(re.search(pat,s).group())
# matchobject. 对整个字符串进行匹配，，没有匹配上返回None,否则返回matchobject

#newpat='这里是中文内容'.decode("utf8")
#news=re.sub(pat,newpat,s)
# 正则部分替换，将s中的所有符合pat的全部替换为newpat，newpat也可以是函数
#print(news)

def newpat_func(matched):
    return "这里是".decode('utf-8') + matched.group() + u"内容"
print(re.sub(pat, newpat_func, s))
'''

