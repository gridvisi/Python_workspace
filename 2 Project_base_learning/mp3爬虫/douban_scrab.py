'''
https://blog.csdn.net/mario_faker/article/details/79618235
获取正在热映的电影：https://douban.uieee.com/v2/movie/in_theaters
访问参数：
start : 数据的开始项

count：单页条数

city：城市

获取电影Top250：https://douban.uieee.com/v2/movie/top250
访问参数：
start : 数据的开始项

count：单页条数

获取即将上映电影：https://douban.uieee.com/v2/movie/coming_soon
访问参数：
start : 数据的开始项

count：单页条数

电影搜索：https://douban.uieee.com/v2/movie/search
访问参数：
start : 数据的开始项

count：单页条数

q：要搜索的电影关键字

tag：要搜索的电影的标签

电影详情：https://douban.uieee.com/v2/movie/subject/:id
访问参数：电影id
如：电影《小飞象》的电影id为：25924056，搜索此电影的详细信息：
https://api.douban.com/v2/movie/subject/25924056

电影本周口碑榜： https://douban.uieee.com/v2/movie/weekly?apikey=0df993c66c0c636e29ecbb5344252a4a
北美票房榜： https://douban.uieee.com/v2/movie/us_box?apikey=0df993c66c0c636e29ecbb5344252a4a
新片榜： https://douban.uieee.com/v2/movie/new_movies?apikey=0df993c66c0c636e29ecbb5344252a4a
影人剧照: https://douban.uieee.com/v2/movie/celebrity/:id/photos?apikey=0df993c66c0c636e29ecbb5344252a4a
电影条目剧照： https://douban.uieee.com/v2/movie/subject/:id/photos?apikey=0df993c66c0c636e29ecbb5344252a4a
豆瓣音乐
搜索 https://douban.uieee.com/v2/music/search?q=欧美&count=15?
详情 https://douban.uieee.com/v2/music/:id
豆瓣图书
搜索，例如：
https://douban.uieee.com/v2/book/search?q=虚构类&count=8
https://douban.uieee.com/v2/book/search?q=非虚构类&count=8
https://douban.uieee.com/v2/book/search?q=旅行&count=8
获取电影条目短评论: https://douban.uieee.com/v2/movie/subject/:id/comments?start=xxx&count=xxx&apikey=0df993c66c0c636e29ecbb5344252a4a
'''


import requests
def get_content(start_page):
   url = 'https://api.douban.com/v2/movie/top250?'
   url = 'https://douban.uieee.com/v2/movie/coming_soon?'
   params = {
       'start':start_page,
       'count':50
       }
   response = requests.get(url,params=params).json()
   print(response)
   movies = response['subjects']
   data = [{
       'rating':item['rating']['average'],
       'genres':item['genres'],
       'name':item['title'],
       'actor':get_actor(item['casts']),
       'original_title':item['original_title'],
       'year':item['year'],
   } for item in movies]
   write_to_file(data)

def get_actor(actors):
   actor = [i['name'] for i in actors]
   return actor

def write_to_file(data):
   with open('douban_def.csv','a',encoding='utf_8_sig',newline='') as f:
       w = csv.writer(f)
       for item in data:
           w.writerow(item.values())

def get_douban(total_movie):
   # 每页50条，start_page循环5次
   for start_page in range(0,total_movie,50):
       get_content(start_page)
if __name__ == '__main__':
   get_douban(250)