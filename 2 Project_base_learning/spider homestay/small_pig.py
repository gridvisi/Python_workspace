#https://www.yht7.com/news/17750

import requests
from lxml import etree
import time
url3 = 'http://cq.xiaozhu.com/'
data3 = requests.get(url3).text
h = etree.HTML(data3)
titles = h.xpath('//*[@id="page_list"]/ul/li/div[2]/div/a/span/text()')
time.sleep(2)#注意，小猪在发爬虫方面做得比较好，防止被封IP就加个睡眠吧
for title in titles:
    print(title)


#https://www.jianshu.com/p/8321702bddc6