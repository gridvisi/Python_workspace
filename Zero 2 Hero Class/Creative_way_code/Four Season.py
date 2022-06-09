age = [9, 8,10]
print([i%2==0 for i in age])

print(10%3,11%3)

dan = []
shuan = []
for i in range(11):
    if i%2 == 0:
        shuan.append(i)
    elif i%2 == 1:
        dan.append(i)


print(11/3)

import math
print(math.ceil(1.1),math.floor(1.1),round(10/3,2))
print('ceshi:',math.ceil(10/3))
print(math.ceil(11/3))

def season(month):
    return math.ceil(month/3)
month = [season(i) for i in range(1,13)]
print(month)

def season(month):
    return int(str(month),8)


def season(month):
    return [i for i in range(1,13,3)]
month = 6
print(season(month))

# 1-3; 4-6; 7-9; 10-12
month = 9
# 秋天
# 季节
def season(month):

    return '季节:'

'''
name = 'dingdingmao' #字符串
print('3:',name[8:11])

for i in range(10):
    print('hour:',i)

i = 0
stage = ['shallow','deep','by myself']
print(stage[2])

wake_up = 'by myself'
while stage[i] != wake_up:
    stage[i] += 1
    print(i)


name = 'my name is dingdingmao'  #遍历
print(len(name))  #
l = 0
for i in name:
    #print(i)
    l = l+1
print(l)
    #print(i,end="")





num = [1,2,3,4] # key
season = ['spring','summer','autumn','winter'] #value
dict_season = dict(zip(num,season))
print(dict_season)
# {1: 'spring', 2: 'summer', 3: 'autumn', 4: 'winter'}

print(dict_season[1])
print(dict_season.get(1,'only 1,2,3,4 is valid'))
'''