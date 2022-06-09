
'''
作者：猴哥Yuri
链接：https://www.jianshu.com/p/2e190438bd9c
来源：简书

本文是爬虫系列文章的第一篇，主要讲解 Python 3 中的 urllib 库的用法。
urllib 是 Python 标准库中用于网络请求的库。该库有四个模块，分别是
urllib.request，urllib.error，urllib.parse，urllib.robotparser。
其中urllib.request，urllib.error两个库在爬虫程序中应用比较频繁。
那我们就开门见山，直接讲解这两个模块的用法。

1 发起请求
模拟浏览器发起一个 HTTP 请求，我们需要用到 urllib.request 模块。urllib.request
的作用不仅仅是发起请求， 还能获取请求返回结果。发起请求，单靠 urlopen() 方法就可以叱咤风云。
我们先看下 urlopen() 的 API
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
import urllib.request
#urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)

'''
第一个参数 String 类型的地址或者
data 是 bytes 类型的内容，可通过 bytes()函数转为化字节流。它也是可选参数。使用 data 参数，请求方式变成以 POST 方式提交表单。使用标准格式是application/x-www-form-urlencoded
timeout 参数是用于设置请求超时时间。单位是秒。
cafile和capath代表 CA 证书和 CA 证书的路径。如果使用HTTPS则需要用到。
context参数必须是ssl.SSLContext类型，用来指定SSL设置
cadefault参数已经被弃用，可以不用管了。
该方法也可以单独传入urllib.request.Request对象
该函数返回结果是一个http.client.HTTPResponse对象。
1.1 简单抓取网页
我们使用 urllib.request.urlopen() 去请求百度贴吧，并获取到它页面的源代码。

作者：猴哥Yuri
链接：https://www.jianshu.com/p/2e190438bd9c
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

url = "http://tieba.baidu.com"
response = urllib.request.urlopen(url)
html = response.read()         # 获取到页面的源代码
print(html.decode('utf-8'))    # 转化为 utf-8 编码

'''
1.2 设置请求超时
有些请求可能因为网络原因无法得到响应。因此，我们可以手动设置超时时间。当请求超时，
我们可以采取进一步措施，例如选择直接丢弃该请求或者再请求一次。
'''
import urllib.request

url = "http://tieba.baidu.com"
response = urllib.request.urlopen(url, timeout=1)
print(response.read().decode('utf-8'))

