# https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas/55557758?r=SearchResults#55557758
from collections import namedtuple

#Cartesian coordinates 笛卡尔坐标
CommentInfo = namedtuple('CommentInfo', ["stt", "gid", "uid"])
dct = {
    "stt": "Tom",
    "gid": 24,
    "uid":2
        }
c = CommentInfo._make(dct)
print('c实例化：',c)

x = CommentInfo(stt=1,gid=12,uid=222)
print(x._asdict())



#重庆经度:106.55 纬度:29.57
#'Latitude', 'Longitude
#Latitude: 经度
#Longitude：纬度
#然后，我们可以使用Coords该类来实例化一个对象，该对象将是一个命名元组。
Coords = namedtuple('Coords', ['Latitude', 'Longitude'])
home = Coords(Latitude=-37.8871270826,Longitude=144.7558373041)
print(isinstance(home,tuple))
print(home)
chongqing = Coords(Latitude=106.55,Longitude=29.57)
print(chongqing)

ChongqingInfo = namedtuple('chongqing', ['Latitude', 'Longitude', "areacode"])
profile = ChongqingInfo(Latitude=106.55,Longitude=29.57,areacode='028')
chongqing = ChongqingInfo._make(dct)
print(chongqing)

#tuple convert to dict字典格式
print(profile._asdict())

#dict convert to tuple
#dictprofile = profile._asdict()
dct = {'Latitude':106.55, 'Longitude':29.57,'areacode':'028'}
chongqing = ChongqingInfo._make(dct)
print('chongqingDct:',chongqing)

#case 1st
import pandas as pd
inp = [{'c1':10, 'c2':100}, {'c1':11,'c2':110}, {'c1':12,'c2':120}]
df = pd.DataFrame(inp)
print(df)
'''
   c1   c2
0  10  100
1  11  110
2  12  120
'''

#Case 2nd
CommentInfo = namedtuple('CommentInfo', ["stt", "gid", "uid"])
x = CommentInfo(stt=1,gid=12,uid=222)
print(x._asdict())
#OrderedDict([('stt', 1), ('gid', 12), ('uid', 222)])
#{'stt': 1, 'gid': 12, 'uid': 222}

#Case 3rd

import pandas as pd

df = pd.DataFrame({'c1': [10, 11, 12], 'c2': [100, 110, 120]})

for index, row in df.iterrows():
    print(row['c1'], row['c2'])


import pandas as pd
import numpy as np

df = pd.DataFrame( { 'x':[1,2,3,4,5,6], 'y':[1,1,1,0,1,1]  } )
print(df)
#   x  y  desired_result
#0  1  1               1
#1  2  1               3
#2  3  1               6
#3  4  0               4
#4  5  1               9
#5  6  1              15



a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

mjr = pd.DataFrame({'a':a, 'b':b})
print(mjr)
size = mjr.shape

for i in range(size[0]):
    for j in range(size[1]):
        print(mjr.iloc[i, j])



#case 5th
'''
import time
df = pd.DataFrame({'a': randn(1000), 'b': randn(1000),'N': randint(100, 1000, (1000)), 'x': 'x'})

%timeit [row.a * 2 for idx, row in df.iterrows()]
# => 10 loops, best of 3: 50.3 ms per loop

%timeit [row[1] * 2 for row in df.itertuples()]
# => 1000 loops, best of 3: 541 µs per loop
'''


#case 6th

df = pd.DataFrame({'col1': [1, 2], 'col2': [0.1, 0.2]}, index=['a', 'b'])
#Iterating over the rows:

for row in df.itertuples(index=False, name='Pandas'):
    print(np.asarray(row))

'''
[1.  0.1]
[2.  0.2]
'''


from collections import namedtuple
two_d = namedtuple('twoDPoint', ['x', 'y'])
x = two_d(1, 2)
#x = two_d(1, 2)
three_d = namedtuple('threeDPoint', ['x', 'y', 'z'])
print(x)
#twoDPoint(x=1, y=2)

y = three_d(*x, z=3)
print(y)
#threeDPoint(x=1, y=2, z=3)