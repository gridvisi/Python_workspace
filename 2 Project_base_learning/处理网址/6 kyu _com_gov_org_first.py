'''
https://www.codewars.com/kata/57f21fcd69e09cb0d2000088/train/python
n 最后的测试中，具有相同域名的连续地址将在比较前进行分组和排序，即。

假设你的解决方案返回["b.com", "a.com", "c.gov"], 测试将这样做:

把地址分成几组：[["b.com", "a.com"], ["c.gov"]]。
对每组进行排序。[["a.com"、"b.com"]、["c.gov"]]
压平它们。["a.com", "b.com", "c.gov"]

n the final tests consecutive addresses with the same domain will be grouped and sorted before
comparison, i.e.:

Given your solution returns ["b.com", "a.com", "c.gov"], the tests will do this:

Split the addresses into groups: [["b.com", "a.com"], ["c.gov"]]
Sort each group: [["a.com", "b.com"], ["c.gov"]]
Flatten them: ["a.com", "b.com", "c.gov"]

input_list = [
    "http://www.google.en/?x=jsdfkj",
    "http://www.google.de/?x=jsdfkj",
    "http://www.google.com/?x=jsdfkj",
    "http://www.google.org/?x=jsdfkj",
    "http://www.google.gov/?x=jsdfkj",
]

expected = [
    "http://www.google.com/?x=jsdfkj",
    "http://www.google.gov/?x=jsdfkj",
    "http://www.google.org/?x=jsdfkj",
    "http://www.google.de/?x=jsdfkj",
    "http://www.google.en/?x=jsdfkj",
]

Test.assert_equals(order_by_domain(input_list), expected)
'''
addresses = [
    "http://www.google.en/?x=jsdfkj",
    "http://www.google.de/?x=jsdfkj",
    "http://www.google.com/?x=jsdfkj",
    "http://www.google.org/?x=jsdfkj",
    "http://www.google.gov/?x=jsdfkj",
]
_,d = addresses[0].rsplit('.',1)
print(d[:3])

addresses = ['http://www.etpr.uxkt.bmx.com',
             'http://www.fxp.pmm.com/?qyk=ayyyv',
             'http://www.otnsf.bqhe.com',
             'http://www.oucxa.kjiqk.com/?nwjbq=bfpr',
             'http://www.qohk.ogrx.zbpr.com/?rnes=qjgx',
             'http://www.ufbwc.zhhqk.ilvpw.com/?ofrns=guzxw',
             'http://www.wmi.eyhka.gov/?feq=fhyoi',
             'http://www.ufzcf.org/?ndw=jxyli',
             'http://www.kbgb.pxqmf.ivmx/?whq=ukf',
             'http://www.ild.fwnn.bbxwz.mmv',
             'http://www.amy.eje.rxnkz/?bfuev=opuou']

from urllib.parse import urlparse
print(urlparse("http://www.vtl.tpns.scwgd/?jqr=nxpb").hostname)
print(addresses[-1],urlparse(addresses[-1]).hostname)
print(urlparse(addresses[-2]).hostname)


result=urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result),result.hostname)


from tld import get_tld
#print(addresses[0],get_tld(addresses[0]))


#9th solution
def domain(x):
    for i,e in enumerate(x[::-1]):
        if e == '.':
            return x[::-1][:i][::-1]
x = 'www.google.com'
print('domain:',domain(x))

def order_by_domain(addresses):
    urls = addresses
    ans,result = [],[]
    priority = ['com','gov','org']
    ans = [(domain(urlparse(url).hostname),url) for url in urls]
    temp = sorted([x[1] for x in ans if x[0] not in priority],key=lambda x:x[0][0])
    print('temp:',temp)
    i = 0
    while i < 3:
        for x in ans:
            if x[0] == priority[i]:
                result.append(x[1])
        i += 1
    result.extend(temp)
    return result
print(order_by_domain(addresses))


#1st solution
def ex(id):
    ext = id.split(".")[-1]
    return ext


def order_by_domain(addresses):
    com = []
    gov = []
    org = []
    res = []
    for i in addresses:
        i += ' '
        if ".com " in i or ".com/" in i:
            com.append(i[:-1])
        elif ".gov " in i or ".gov/" in i:
            gov.append(i[:-1])
        elif ".org " in i or ".org/" in i:
            org.append(i[:-1])
        else:
            res.append(i[:-1])
    return sorted(com) + sorted(gov) + sorted(org) + sorted(res, key=ex)

#2nd solution
def exten(link):
    ext=link.split('.')[-1]
    return ext


def order_by_domain(addresses):
    com=[]
    gov=[]
    org=[]
    res=[]
    for i in addresses:
        i+=' '
        if ".com " in i or ".com/" in i:
            com.append(i[:-1])
        elif ".gov " in i or ".gov/" in i:
            gov.append(i[:-1])
        elif ".org " in i or ".org/" in i:
            org.append(i[:-1])
        else:
            res.append(i[:-1])
    return sorted(com)+sorted(gov)+sorted(org)+sorted(res,key=exten)

#3rd solution
def order_by_domain(addresses):
    def weights(a):
        _, d = a.rsplit('.', 1)
        return {'com': 0, 'gov': 1, 'org': 2}.get(d[:3], 3), d

    return sorted(addresses, key=weights)


#4th solution
def sort(address):
    domains = {"org": "aac", "gov": "aab", "com": "aaa"}
    domain = address.split('/?')[0].split('.')[-1]
    return domain if domain not in domains else domains[domain]


def order_by_domain(addresses):
    addresses = sorted(addresses, key=sort)
    return addresses

#5th solution
REGEX = __import__("re").compile(r"(?<=\.)[a-z]+(?=\/|$)").search
S = {"com", "gov", "org"}

def my_key(a):
    ext = REGEX(a).group()
    return (ext not in S, ext)

def order_by_domain(addresses):
    return sorted(addresses, key=my_key)


#6th solution
import requests

def order_by_domain(addresses):
    get_dom = lambda url: requests.utils.urlparse(url).netloc.split('.')[-1]
    priority_dom = lambda dom: ('org|gov|com'.find(dom) * -1, dom)
    return sorted(addresses, key = lambda i: priority_dom(get_dom(i)))

#7th solution
from urllib.parse import urlparse

def order_by_domain(addresses):
    def weights(a):
        p = urlparse(a).netloc.split('.')
        return {'com': 0, 'gov': 1, 'org': 2}.get(p[-1], 3), a.split(p[-2])[-1]

    return sorted(addresses, key=weights)

def order_by_domain(addresses):
    pars = [urlparse(add) for add in addresses]

    return


'''


def order_by_domain(addresses):
    urls = addresses
    ans,result = [],[]
    priority = ['com','gov','org']
    for url in urls:
        try:
            ans.append((url,get_tld(url)))
        except Exception as e:
            print("unkonw")
    temp = sorted([x[0] for x in ans if x[1] not in priority])
    print(ans,temp)
    i = 0
    while i < 3:
        for x in ans:
            if x[1] == priority[i]:
                result.append(x[0])
    #        elif x[1] not in priority:
    #            temp.append(x[0])
        i += 1
    result.extend(temp)

    return result
print(order_by_domain(addresses))



'''