from bs4 import BeautifulSoup

infos = soup.find('div',{'class':'content__list'}).find_all('div',{'class':'content__list--item'})
name = info.find('p',
                 {'class': 'content__list--item--title twoline'}).find(
    'a').get_text().strip()
mix = info.find('p', {'class': 'content__list--item--des'}).get_text()
mix = re.split(r'/', mix)

area = mix[1].strip()
address = mix[0].strip()
door_orientation = mix[2].strip()
style = mix[3].strip()


urls = ['https://sh.lianjia.com/zufang/jingan/pg{}/'.format(str(i)) for i in range(1, 79)]

import requests, time, re, csv
from bs4 import BeautifulSoup
import codecs

with open(r'C:\Users\小阿辰\Desktop\链家上海\静安.csv', 'ab+')as fp:
    fp.write(codecs.BOM_UTF8)
f = open(r'C:\Users\小阿辰\Desktop\链家上海\静安.csv','a+',newline='', encoding='utf-8')
writer = csv.writer(f)
writer.writerow(('名称', '租金', '面积', '具体地址', '门朝向', '户型', '地区'))
r'C:\Users\小阿辰\Desktop\链家上海\静安.csv'
urls = ['https://sh.lianjia.com/zufang/jingan/pg{}/'.format(str(i)) for i in range(1, 79)]

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.9 Safari/537.36'
}
for url in urls:
    res = requests.get(url, headers=headers)
# print(res.text)  网页内容  文本
# print(res.content.decode('utf-8'))  #网页内容 二进制
    html = res.text
    soup = BeautifulSoup(html, 'lxml')
# print(soup)
    infos = soup.find('div',{'class':'content__list'}).find_all('div',{'class':'content__list--item'})
# print(infos)
    for info in infos:
        name = info.find('p',
                         {'class': 'content__list--item--title twoline'}).find(
            'a').get_text().strip()
        price = info.find('span',
                          {'class': 'content__list--item-price'}).get_text()
        mix = info.find('p', {'class': 'content__list--item--des'}).get_text()
        mix = re.split(r'/', mix)
        area = mix[1].strip()
        address = mix[0].strip()
        door_orientation = mix[2].strip()
        style = mix[3].strip()
        # advantage = info.find('p',{'class':'content__list--item--bottom oneline'}).get_text()
        region = re.split(r'-', address)[0]
        writer.writerow((name, price, area, address, door_orientation, style, region))
        time.sleep(1)

f.close()
