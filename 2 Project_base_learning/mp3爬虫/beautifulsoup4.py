#https://www.jianshu.com/p/865d73b70ec7

'''
4 解析 BeautifulSoup 对象
想从 html 中获取到自己所想要的内容，我归纳出三种办法：

1）利用 Tag 对象
从上文得知，BeautifulSoup 将复杂 HTML 文档转换成一个复杂的树形结构,每个节点都是Python对象。跟安卓中的Gson库有异曲同工之妙。节点对象可以分为 4 种：Tag, NavigableString, BeautifulSoup, Comment。

Tag 对象可以看成 HTML 中的标签。这样说，你大概明白具体是怎么回事。我们再通过例子来更加深入了解 Tag 对象。以下代码是以 prettify() 打印的结果为前提。

例子1
获取head标签内容

作者：猴哥Yuri
链接：https://www.jianshu.com/p/865d73b70ec7
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
print(soup.head)
# 输出结果如下：
#<head><title>The Dormouse's story</title></head>

'''
例子2 获取title标签内容
'''
from bs4 import BeautifulSoup

#soup = BeautifulSoup(response)
#print(soup.prettify())
'''
例子3  获取p标签内容
'''
print(soup.p)
# 输出结果如下：
#<p class="title" name="dromouse"><b>The Dormouse's story</b></p>




'''
<html>
 <head>
   <title>
       The Dormouse's story
   </title>
 </head>
 <body>
   <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
   <p class="story">Once upon a time there were three little sisters; and their names were</p>
   <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>
 </body>
</html>
'''

soup = BeautifulSoup(open("index.html"))
# 打开当前目录下 index.html 文件