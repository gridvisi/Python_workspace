'''
https://zhuanlan.zhihu.com/p/78760387?utm_source=wechat_session
'''

#导入库，如果还没有库就去学怎么安装这些库
import requests
import re
import os


#这个模块的作用是抓取网页源代码，也就是你在浏览器中单击鼠标右键中查看源代码出现的内容
def getHTMLText(url):
 try:
  kv={'user-agent':'Mozilla/5.0'} #模拟头文件，相当于用假冒的身份证骗过网站的门卫
  r = requests.get(url, timeout=30,headers=kv) #抓取网页源代码
  r.raise_for_status() #查看状态
  r.encoding = r.apparent_encoding #自动识别并更改编码方式
  return r.text #爬下来的源代码保存在内存中的r.text中
 except:
  return ""


#这个模块的作用是通过榛果民宿首页源代码，获取全国所有城市的名字，为后面分城市抓取数据做铺垫
def getLoc(lst,page):
 try:
  r=getHTMLText(page) #抓取首页源代码
  elt=re.findall('<li><a href="/(.*?)/" class="btn btn-default">',r) #找到所有城市对应的拼音简称
  clt=re.findall('class="btn btn-default">(.*?)</a></li>',r)  #找到所有城市对应的中文简称
#将中英文简称填入lst表中，方便之后留用
  for i in range(len(elt)):
   eng=elt[i]
   chn=clt[i]
   lst.append([eng,chn])
 except:
  print("")


#页面解析，每个城市对应的源代码被抓取后，在这里进行解析
def parsePage(ilt, html):
 try:
  plt = re.findall('</i>([\d]*)</span>',html) #找到抓取源代码中的所有价格信息
  alt = re.findall('<span class="room-prop">(.*?)</span></div><div',html) #找打抓取源代码中的所有位置区域信息
#将位置和价格信息导入到ilt表中
  for i in range(len(plt)):
   price = plt[i]
   area = alt[i].split('</span><span class="room-prop">')[-1]
   ilt.append([price , area])
 except:
  print("")


#将结果打印到屏幕上，以查看是否爬取成功
def printGoodsList(ilt):
 tplt = "{:4}\t{:8}\t{:16}"
 print(tplt.format("序号", "价格", "区域"))  #画出表头
 count = 0
 for g in ilt: #将存储到ilt中的价格和区域数据逐行打印到屏幕上
  count = count + 1
  print(count),
  print(g[0]),
  print(g[1])


#指挥官登场
def main():
 page="https://www.zhenguo.com/" #网站首页网址
 lst=[] #设定一个空表，用来存之后的地址信息
 getLoc(lst,page) #运行上面构造的用于提取全国城市名称的模块
 for k in lst: #得到了全国城市名称后，开始逐个爬取
  loc = k[0] #爬取单个城市的信息，需要将城市的拼音简称加入到网址中
  depth = 60 #爬取深度为60，即需要爬取60页的数据
  begin=20191017 #爬取时向网站提交的入住时间
  end=20191018 #爬取时向网站提交的离店时间
  start_url = 'https://www.zhenguo.com/' + loc + '/'  #整合到一起后的网址
  infoList = [] #构造一个空表，用于保存价格和区域信息
  for i in range(depth):
   try:
    i=i+1
    url = start_url+"pn"+str(i)+"/?dateBegin="+str(begin)+"&dateEnd="+str(end)             #每个城市对应的网址
    html = getHTMLText(url) #启动网页爬取模块，爬取网页源代码
    parsePage(infoList, html) #源代码解析，只提取其中的价格和区域信息
   except:
    continue
  printGoodsList(infoList) #将提取好的信息打印到屏幕上
  f=open(k[1]+'.txt','w') #将提取好的信息保存到本地的txt文件
  for k in infoList:
   for m in k:
     m=m.encode('utf-8')
     print (f,m)
   print (f,'\n')
  f.close()


print(main()) #启动指挥官