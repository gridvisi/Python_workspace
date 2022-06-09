urls = ["http://meiwen.me/src/index.html",
          "http://1000chi.com/game/index.html",
          "http://see.xidian.edu.cn/cpp/html/1429.html",
          "https://docs.python.org/2/howto/regex.html",
          """https://www.google.com.hk/search?client=aff-cs-360chromium&hs=TSj&q=url%E8%A7%A3%E6%9E%90%E5%9F%9F%E5%90%8Dre&oq=url%E8%A7%A3%E6%9E%90%E5%9F%9F%E5%90%8Dre&gs_l=serp.3...74418.86867.0.87673.28.25.2.0.0.0.541.2454.2-6j0j1j1.8.0....0...1c.1j4.53.serp..26.2.547.IuHTj4uoyHg""",
          "file:///D:/code/echarts-2.0.3/doc/example/tooltip.html",
          "http://api.mongodb.org/python/current/faq.html#is-pymongo-thread-safe",
          "https://pypi.python.org/pypi/publicsuffix/",
          "http://127.0.0.1:8000"
          ]

from urllib.parse import urlparse
url = 'https://blog.csdn.net/fisherming/article/details/89450841'
print(urlparse(url).hostname)
'''
观察实例，'http://www.baidu.com/index.html;user?id=5#comment'

可以发现，urlparse（）方法将其拆分为6个部分，分别是

scheme='http',代表协议

netloc='www.baidu.com',代表域名

path='/index.html', 代表path，即访问路径

params='user', 代表参数

query='id=5', 代表查询条件，一般用作get类型的URL

fragment='comment'代表锚点，用于直接定位页面内部的下拉位置，

所以一个标准的链接应该是

scheme://netloc/path;params?query#fragment

接下来讲述其API用法

'''

import re
pattern = re.compile(
    r'^(([a-zA-Z]{1})|([a-zA-Z]{1}[a-zA-Z]{1})|'
    r'([a-zA-Z]{1}[0-9]{1})|([0-9]{1}[a-zA-Z]{1})|'
    r'([a-zA-Z0-9][-_.a-zA-Z0-9]{0,61}[a-zA-Z0-9]))\.'
    r'([a-zA-Z]{2,13}|[a-zA-Z0-9-]{2,30}.[a-zA-Z]{2,3})$'
)


def is_valid_domain(value):
    """
    Return whether or not given value is a valid domain.
    If the value is valid domain name this function returns ``True``, otherwise False
    :param value: domain string to validate
    """
    return True if pattern.match(value) else False


#2 domin

from tld import get_tld
print("--"*40)
for url in urls:
    try:
        print(get_tld(url))
    except Exception as e:
        print("unkonw")


'''
些python使用中遇到的坑点，记录一下。。同样的问题也可能只是对当前我的环境下有作用，，，，

AttributeError: module ‘urllib’ has no attribute ‘splittype’：使用urllib中的一些工具时，
提示这个函数不存在，因为网络上很容易找到的一些关于这个的使用年代比较久远，基本都是python2的写法，
对于python3，中间添个： request 就行了，也就是：
 urllib.request.splittype(url) urllib.request.splithost(rest)
 
 import urllib
#from urllib import splittype
print("--"*40)
for url in urls:
    proto, rest = urllib.request.splittype(url)
    res, rest = urllib.request.splithost(rest)
    print("unkonw" if not res else res)
'''

