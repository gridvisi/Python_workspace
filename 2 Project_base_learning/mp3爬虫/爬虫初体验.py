
import request
import urllib.request
html = request.get("https://www.baidu.com/")
print(html)

#<Response [200]> success access!

html.encoding = html.apparent_encoding
print(html.text)


data = urllib.request.urlopen("https://www.zhihu.com/question/382573541").read()
print(data)

