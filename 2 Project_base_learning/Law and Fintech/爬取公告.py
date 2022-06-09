
import json
import requests

res = requests.get('http://www.sse.com.cn/assortment/bonds/list/info/basic/index.shtml?BOND_CODE=019627')
res.encoding = 'gbk'  # 得到的结果转换为 gbk 编码
all_news = json.loads(res.text[17:-2])  # 从第一个'['取到最后一个']'，可以先将res.text打印出来，查看里面的元素情况，以此来确定取的位置

# 遍历由json数据得到的list
for each_news in all_news:
    url = each_news[1]  # 获取公告的URL
    title = each_news[2]  # 获取公告的标题
    time = each_news[-1]  # 获取公告发布的时间
    print(url,title,time)