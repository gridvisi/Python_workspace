'''
Top 10 countries ranked by retail e-commerce share or total sales, 2022

1 China 🇨🇳 46.3%
2 UK 🇬🇧 36.3
3 South Korea 🇰🇷 32.2
4 Denmark 🇩🇰  20.2
5 Indonesia 🇮🇩  20.2
6 Norway 🇳🇴    19.4
7 United States 🇺🇸 16.1%
8 Finland 🇫🇮 14.6
9 Sweden 🇸🇪  14.3
10 Canada 🇨🇦 13.6

rank = [46.3,36.3,32.2,20.2,20.2,19.4,16.1,14.6,14.3,13.6]
按零售电子商务份额或总销售额排名的前10个国家，2022年

1 中国🇨🇳46.3%。
2 英国 🇬🇧 36.3
3 韩国 🇰🇷 32.2
4 丹麦 🇩🇰 20.2
5 印度尼西亚 🇮🇩 20.2
6 挪威 🇳🇴 19.4
7 美国 🇺🇸 16.1
8 芬兰 🇫🇮 14.6
9 瑞典 🇸🇪 14.3
10 加拿大🇨🇦 13.6
如何实现条形图？


#y = np.random.randint(0,20,size=5)
#x = np.linspace(0,5,5)
#y = np.random.randint(0,20,size=5)
#axes = plt.subplot(1,2,1)#1x2的区域，一行两列
#axes.bar(x,y)#垂直条形图
#axes = plt.subplot(1,2,1)
'''
import matplotlib.pyplot as plt
import numpy as np
#plt.colorbar("green")
rank = [46.3,36.3,32.2,20.2,20.2,19.4,16.1,14.6,14.3,13.6]
x = np.linspace(0,len(rank),len(rank))
y = rank[::-1]

axes2 = plt.subplot(1,1,1)

for a,b in zip(x,y):
    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=7)
axes2.barh(x,y) #水平条形图
plt.show()

'''

plt.bar(np.arange(8), data.loc[3, :][1:], bottom=data.loc[0, :][1:] + data.loc[1, :][1:] + data.loc[2, :][1:],

color='black', alpha=0.8, label='air transport', align='center')

for x_t, y_t in enumerate(zip(x,y)):

    plt.text(x_t, y_t / 2, '%sW'% (round(y_t / 10000, 2)), ha='center', color='white', fontsize=8)
'''