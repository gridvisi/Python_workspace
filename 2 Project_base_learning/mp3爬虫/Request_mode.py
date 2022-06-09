
import requests
import time
import re

#目标网址http://www.htqyy.com/top/hot的音乐资源爬取3页
#分析网页：
#第一页url：http://www.htqyy.com/top/musicList/hot?pageIndex=0&pageSize=20
#第二页url：http://www.htqyy.com/top/musicList/hot?pageIndex=1&pageSize=20
#第三页url：http://www.htqyy.com/top/musicList/hot?pageIndex=2&pageSize=20
#分析结果：pageIndex0,1,2的序列排列那么在请求中用循环的方式爬取页面
#想要爬取的音乐链接
#<a href="/play/59" target="play" title="阿兰胡埃斯之爱" sid="59">阿兰胡埃斯之爱</a>
#歌曲网页地址http://f2.htqyy.com/play7/20/mp3/5

songid=[]
songname=[]
for i in range(0,3):
    url="http://www.htqyy.com/top/musicList/hot?pageIndex="+str(i)+"0&pageSize=20"
    url = "https://www.kugou.com/song/#hash=C3D89D61D0B504038C69D641A148B96F&album_" + "id=1594820"
    res=requests.get(url)
    strr=res.text
    pat1=r'title="(.*?)" sid'
    pat2=r'sid="(.*?)"'
    titlelist=re.findall(pat1,strr)
    idlist=re.findall(pat2,strr)
    #print(titlelist,idlist)
    songid.extend(idlist)#通过列表组合将3页的id组合成新的列表
    songname.extend(titlelist)#通过列表组合将3页的歌曲名组合成新的列表

#通过二次爬取将歌曲的下载到本地
for i in range(0,len(songid)):
    musicurl="http://f2.htqyy.com/play7/"+str(songid[i])+"/mp3/5"
    musicname=songname[i]
    musicres=requests.get(musicurl).content

    print("正在下载第", i + 1, "首.............")
    with open("E:\\music\\{}.mp3".format(musicname),"wb") as f:
        f.write(musicres)

    time.sleep(0.5)