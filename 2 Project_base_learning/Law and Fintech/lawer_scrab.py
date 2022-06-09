import requests
import json

session = requests.Session()  # 实例化一个session对象  需要提前引入requests库
session.headers.update({  # 设置请求头部，这里我将请求的Origin 设置为了他们主站网站，其实不设置也没关系
    "Origin": "https://splcgk.court.gov.cn"
})
list_url = 'https://splcgk.court.gov.cn/gzfwww//qwallist'  # 我们要请求的网站，即接口地址
# 最高法院指导案例的参数 start
data = {
    "fbdw": '最高人民法院',
    'lx': 'lzdx',
    'bt': '',
    'pageNum': '1'
}
# 最高法院指导案例的参数 end
response = session.post(list_url, data=data, timeout=(60, 60))  # 发出post请求，设置超时为60秒
result = response.text  # 获得返回的内容


# request

result = json.loads(result)  #将json字符串转为字典格式
_list = result['list']   #获取字典中键为list的值，得到了我们想要的结果列表

for item in _list:   #遍历列表，将列表中的数据提取并存储到mysql数据库中
	title = unescape(item['cBt'])  # 这个item['cBt']是详情页的url
	public_org = unescape(item['cFymc'])
	docid = item['cBh']      #docid是每个案例的编号，这个编号加上地址前缀就可以获得详情页的地址
	public_date = item['dtUpdatetime']
    #查找数据库中是否有同样docid的内容
	sql='select * from '+ self.config['table']+' where docid=%s'
	cursor.execute(sql, (docid))
	row_1 = cursor.fetchone()
    #如果没有的话就将这些信息存入数据库，这里包含了案例名称，发布单位，发布日期等内容
	if row_1 is None:
		sql="INSERT INTO "+self.config['table']+" (name,public_org,public_date,class,docid,rawdata) " \
										   "VALUES (%s,%s,%s,%s,%s,%s)"
		cursor.execute(sql, (title, public_org, public_date, _class, docid, str(item)))
		db.commit()
		success = success + 1    #计数，每成功一次success增加一次

url = 'https://splcgk.court.gov.cn/gzfwww//qwal/qwalDetails?id='
 _url = url + row_1['docid']      #row_1['docid']是我之前存储在数据库里的案例列表中每个案例的docid
session = requests.Session()
session.headers.update({
     "Origin": "https://splcgk.court.gov.cn",
     "Referer": "https://splcgk.court.gov.cn/gzfwww//qwal"
 })

respond = session.get(_url, timeout=(45, 45)) # proxies=proxies,
content = respond.text

p_detail = '<div class="fd-fix">(.*?)<div class="fd-file-tips"  >'  #正则表达式规则
res_detail = re.search(p_detail, content, re.M | re.I | re.S)  #查询是否有符合正则表达式的内容
#有就更新进数据库，没有就失败
if res_detail is not None:
	_detail = res_detail.groups()[0]
	cursor.execute("update guidecase set content=%s where docid=%s", (_detail, row_1['docid']))
	db.commit()
	success = success + 1
	print('插入成功，success', success)
else:
	fail = fail + 1
	bad = bad + ',' + row_1['docid']
	print('fail,focid=', row_1['docid'])
	print('bad:', bad)             