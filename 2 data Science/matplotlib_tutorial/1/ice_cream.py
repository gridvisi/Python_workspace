
def hour2sec(h):
    return h * 60 * 60
h = 24
print(hour2sec(h))

def usd2rmb(n):
    return f"{n}美元折合人民币是{n * 6.31}元"
print(usd2rmb(100))


n = 1000000000
print(len(str(n)))

for i in range(1,11):
    for j in range(1,i+1):
        print('%d*%d=%2ld '%(i,j,i*j),end='')
    print()


#1、字典
#2、输出
#3、计算总价并输出的格式，涉及小数点

price_sheet = {'ha gendasi': 15, 'Cold Stone': 5,
               'VIVOLI GELATO': 9, 'COPPELIA ': 7,
               'Dairy Queen(DQ)': 11, "Wall's": 8,
               'que chao': 10, 'wu yangpai': 4,
               'ba xi': 12, 'yi li': 13, 'le keke': 14}

#print(price_sheet['lekeke'])#
print(price_sheet.get('lekeke'))
#
# key:value

def icecreamshop(n: int, c: str):  #input name,number
    ans = price_sheet.get(c)
    print('ans',ans)
    if ans: return ans * n *1.0
    return f"抱歉没有{c}"
n,c = 2,"Wall's "
print(icecreamshop(n,c))


import numpy as np
import matplotlib.pyplot as plt

#解决中文显示问题
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False


# 中文乱码和坐标轴负号处理
# matplotlib.rc('font', family='Calibri', weight='normal')  #'bold'
#plt.rcParams['axes.unicode_minus'] = False

# 指定图形的字体

font = {'family' : 'serif',

        'color'  : 'darkred',

        'weight' : 'normal',

        'size'   : 16}

# 绘图。

# fig, ax = plt.subplots()

# b = ax.barh(range(len(job)), data, color='palegreen')



# params

# x: 条形图x轴

# y：条形图的高度

# width：条形图的宽度 默认是0.8

# bottom：条形底部的y坐标值 默认是0

# align：center / edge 条形图是否以x轴坐标为中心点或者是以x轴坐标为边缘



c = ['lightcoral', 'coral', 'darkorange', 'gold' ,'palegreen',

     'paleturquoise' ,'skyblue' ,'plum' ,'hotpink' ,'pink' ,'yellowgreen']



job = ["ha gendasi" ,"Cold Stone" ,"VIVOLI GELATO",

       "COPPELIA " ,"Dairy Queen(DQ)" ,"Wall's" ,"que chao"

                                              "wu yangpai" ,"ba xi" ,"yi li" ,"le keke"]



percentage = [17 ,14 ,12 ,11 ,10 ,8 ,7 ,7 ,6 ,5 ,3]

# 为横向水平的柱图右侧添加数据标签。



plt.xlabel('percentage of aspirants interest' ,fontsize=17)

plt.ylabel('Domains' ,fontsize=30)

plt.barh(range(len(percentage) ,0 ,-1), percentage, tick_label=job, color=c)
#plt.legend()
#plt.show()




