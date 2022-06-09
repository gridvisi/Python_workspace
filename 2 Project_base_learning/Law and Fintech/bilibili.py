import json
import requests


page = 1
session = requests.Session()
target_url = "https://api.bilibili.com/x/web-interface/search/type?context=&search_type=video" \
             "&page=" + str(page) + "&order=&keyword=%E8%94%A1%E5%BE%90%E5%9D%A4&duration=&category_id=" \
                                    "&tids_1=&tids_2=&__refresh__=true&highlight=1&single_column=0&jsonp=jsonp&callback=__jp2"

imageUrl = "https://search.bilibili.com/all?keyword=%E8%94%A1%E5%BE%90%E5%9D%A4&from_source=nav_search"  # &spm_id_from=333.851.b_696e7465726e6174696f6e616c486561646572.10
response = requests.get(SPLASH_URL + 'render.png?url=' + imageUrl + '&wait=2.5&render_all=1')  # 获取页面图片 &width=1000&height=1500
with open('pics/caixukun_' + str(page) + '.png', 'wb') as f:
    f.write(response.content)  # 保存截图
response = session.get(target_url, cookies=cookies, timeout=(20, 20), verify=False)
result = response.text

#encoding:utf-8
import json
import pandas as pd

with open("caixukun_1.txt","r",encoding='utf-8',errors='ignore') as f:
    data=f.read()
data=data.replace("None",'"none"')
data = data.replace("True", '"true"')
data = data.replace("False", '"false"')

data=json.loads(data,strict=False)
result=data['data']['result']
df = pd.DataFrame(result)
df.to_excel("demo1.xlsx", sheet_name="蔡徐坤", index=False, header=True)