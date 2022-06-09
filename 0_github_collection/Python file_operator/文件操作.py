
# -*- coding:utf-8 -*-
import csv
csvfile = open('csv_test','w',newline='')
writer = csv.writer(csvfile)
writer.writerow(['name','age','sex','phone'])
data  = [('bbc','18','M','7458025'),
         ('cnn','17','F','9969966'),
         ('CCTV','12','M','1100901')]
writer.writerow(data)
csvfile.close()

'''
str = "1234567"
print( str[0:5:] )# 左闭右开区间,元素下标 从min到max-1（右边是指中间位置）
print( str[2:10:] )# 右边超出可当作len值
print( str[::])# 原串
print( str[6::])# 左边若是超过len-1则为空串，右边不写默认 len
print(str[2]," ",str[-2])# 单个点索引不可超出范围[0,len)或[0,len-1]
print( str[-2::])# 左边为负数-则表示从倒数第i个数开始往右
print( str[:-2:])# 左边不写默认为0，右边为负数-截取至i-1（即：依旧是左闭右开）
print( str[2:-2:])# 345
print( str[-4:-2:])# 45
print( str[::-1])# 反序字串,相邻索引值差为1
print( str[::-2])# 反序字串，按照相邻索引值差为2截取部分
print( str[::-4])# 反序字串# 反序字串，按照相邻索引值差为4截取部分
print( str[3::-1])# 4321 逆序，索引i在左、正数，取str[i]左侧、含str[i]
print( str[:3:-1])# 765 逆序，索引i在右、正数，取str[i]右侧、不含str[i]
print( str[:-3:-1])# 76 逆序，索引i在右、负数，取str[len-i]右侧、不含str[len-i]
print( str[-3::-1])# 54321 逆序，索引i在右、负数，取str[len-i]左侧、含str[len-i]
print( str[-2:-4:-1])# 65
print( str[-2:2:-1])# 654
三个参数“左起点a：右起点b：顺序及步距标志c”。
	a、b可正可负，正则从左往右数、负则自右往左数、区间始终是左闭右开区间。
	c通常省略默认正序步距为1或者置c为-1表示逆序步距为1，也可修改步距大小（可正可负）
'''

#字符串截取
str = "abcABCaBcD"
print( str.replace('c','E'))# abEABCaBED 大小写敏感
print( str) # abcABCaBcD 由此可知，替换生成了新对象、原字串不受影响
print( str.replace('Bc','E'))# abEABCaBED 替换并不要求元素的位数相同
print( str.replace('Bc',' '))# abEABCaB D 替换成空格
print( str.replace('Bc',''))# abEABCaBED 替换成空串时默认为删除该（片段）元素
print( str.replace('Bc','  '))# abEABCaB  D 替换成空格

#字符串替换

str = "ABCDABCDABCD"
print( str.split('A'))# 返回元组（元组的元素不可更改）
print( str.split('A',2))# 分割成 i+1份（i为数字参数）在最左边分割，左侧将会产生空串
print( str.split('B',2))# 分割成 i+1份（i为数字参数），分割时去除分隔符
print( str.split('D',2))# 在最右边元素产生分割无效，有且仅有此种情况保留分隔符

# 字串分割
str = '123123'
all = []
for i in range(0,len(str),1): # 开始的索引位置 i
    for j in range(1,len(str)+1,1):# 子串长度 j ，而且还是字符串截取的有区间点（左闭右开）
        # print("i=", i, " ", "j=", j)
        if i>=j:
            continue
        all.append( str[i:j:])
print( all)
print( set( all)) # 可以直接输出，也可以赋成新的列表
print( all) # 并不对列表的原始数据造成影响

# 字串的分割和替换是数据清洗的基本

#字符串生成所有非空子串
# -*- coding:utf-8 -*-#
Html_content = """<html><head><title> Python</title></head>
<p class="title"><b>Beautiful Soup的学习</b></p>
<p class="study">学习网址：http://blog.csdn.net/huangzhang_123
 <a href="www.xxx.com" class="abc" id="try1">web开发</a>,
<a href=" www.ccc.com " class="bcd" id="try2">网络爬虫</a> and
<a href=" www.aaa.com " class="efg" id="try3">人工智能</a>;
</p>
<p class="other">...</p>"""

from bs4 import  BeautifulSoup # 引入beautifulsoup
soup = BeautifulSoup(Html_content,'html5lib') #
print(1,soup.head) # 头部原样
print(soup.head.getText()) # 头部数据（即内容）
print(2,soup.title) # 标题原样
print(soup.title.getText()) # 标题数据
print(3,soup.body.b) # 可直接指定标签类别
print(soup.body.b.getText()) # 标签数据
print(4,soup.a)  # 获取指定标签的第一个
print(soup.a.getText()) # 标签内容
print(soup.a['class']) # 标签属性值，若有多个时，同样是返回列表
print(5,soup.find_all('a')) # findall返回的是列表list
for i in soup.find_all('a'): # list的没一个元素是一个标签原样
    print(i)    # 标签原样
    print(i.getText()) # 标签内容
print(7,soup.select('#try3')) # id
print(soup.select('.efg')) # class
print(soup.select('a[class="efg"]')) # 属性

# CSS选择器，可以通过以下3种方式进行查找
# soup.select('#try3') # id
# soup.select('.efg') # class
# soup.select('a[class="efg"]') # 属性
# <a href="www.aaa.com" class="efg" id="try3"> 人工智能</a>

