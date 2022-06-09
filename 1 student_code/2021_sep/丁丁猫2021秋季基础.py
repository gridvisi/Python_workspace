#https://brilliant.org/daily-problems/duplicated-instruction/


#第一题 字符串练习
# 例如同学的名字用拼音表示，并赋值给变量name，即：
name = "lizhenjie"
#那么，姓li，我们用切片操作可以实现得到他的姓
surname = name[0:2]
#我们打印出来，看看对不对？
print(surname)

#老师的提出的任务是，
# 每位同学按照上面的步骤，打印出自己的姓和名

#第二题：整数
# 两个同学买书，书的价格是10元，现在两个人一起买算团购，可以打8折，也就是8元每本；
# 价格用英语book_price作为变量的名字，amount变量是买书共花费的人民币

book_price = 10
amount = book_price * 2 * 0.8
print(amount)

#老师的提出的任务是，增加一个变量名 discount，团购打折的幅度，用来计算实际购买的总金额？
# 参考上面的代码？

#第三题 切香肠
#有17根香肠，3个人分，如果不许切开香肠，保证每人拿到整根香肠，平均每人拿到几根，剩下几根？
print(17//3) # 注意运算符合是 //
print(17%3)  # 注意运算符合是 %

#现在容许切开香肠，问平均每人分得香肠多少？不足一根的部分也算进去
# 同学们用什么运算符合？请写出代码：

'''
1、fruit指“水果”时为集体名词，只用单数，不用复数，如果指不同种类的水果或事情的结果时，
则用复数fruits。

2、fruit例句：

Fresh fruit and vegetables provide fibre and vitamins.

新鲜水果和蔬菜提供植物纤维素和维生素。

Eat plenty of fresh fruit and vegetables.

要多吃新鲜水果和蔬菜。


3、fruits例句：

tropical fruits, such as bananas and pineapples.

热带水果，如香蕉和菠萝。

Apples and melons are my favourite fruits.

苹果和甜瓜是我喜爱的水果。
apple 苹果  

pear 梨  

apricot杏  

peach 桃  

grape 葡萄  

banana 香蕉  

pineapple 凤梨  

plum 李子  

watermelon 西瓜  

orange 橙  

lemon 柠檬  

mango 芒果  

strawberry 草莓  

medlar 欧查果  

loquat 枇杷  

A
Apple [pl] 苹果Apricot [eprkɑt] 杏桃Almond ['ɑmnd]杏仁
B
Banana [bnɑ:n] 香蕉Betelnut ['bitl,nt]槟榔Bitter orange 苦柑橘Blackberry ['blk'bri] 黑莓Blueberry ['blubri] 蓝莓
C
Cherry [teri] 樱桃Crabapple ['krb'pl] 海棠果Carambola [,krm'bol]杨桃Cherry tomato圣女果Chestnut ['tsnt] 栗子
Coconut ['koknt] 椰子Cranberry ['krn'bri]曼越莓Cumquat['kmkwt]金桔Custard['kstd] apple 番荔枝Common fig [fɡ]无花果
D
Damson ['dmzn] 洋李子（黑紫色）Dates 枣子Durian ['drn]榴莲
G
Grape [grep] 葡萄Grapefruit ['ɡrepfrut]葡萄柚Guava ['ɡwɑv]番石榴
H
Haw [h]山楂Hami melon 哈蜜瓜
K
Kiwifruit['kiwi,frt]奇异果，猕猴桃
L
Lemon [lemn] 柠檬Lichee[,l'ti] 荔枝Longan ['lɡn]龙眼、桂圆Loquat ['lokwɑt]枇杷Lotus nut (seed) 莲子
M
Mango [mg] 芒果Mandarin['mndrn] 中国柑桔Mangosteen['mg,stin]山竹Muskmelon['msk,mln]甜瓜总称Mulberry ['ml'bri]桑果
N
Nectarine[nktrin] 油桃
O
Olive 橄榄Orange 橙子
P
Papaya [p'pa] (Pawpaw) 木瓜Peach 桃子Peanut 花生Pear 梨Persimmon[p'smn] 柿子Pineapple ['pan'pl] 菠萝Pistachio[pstio]开心果Pitaya ['ptj]火龙果Plum 李子Pomegranate ['pɑmɡrnt]石榴Pomelo ['pɑmlo]柚子
R
Rambutan [rm'butn]红毛丹Raspberry ['rzbri] 树莓
S
Shaddock ['dk] 文旦Strawberry 草莓Sugar cane 甘蔗Sunflower seeds 瓜子
T
Tangerine ['tnd'rin]橘子
W
Walnut['wlnt]核桃Water Caltrop['kltrp]菱角Water-chestnut['tsnt]马蹄、荸荠Watermelon['wtmln] 西瓜Waxberry['wks,bri]杨梅Wax apple莲雾
'''
# slice string or words
fruits = ['apple','banana','carrot','dates']
for f in fruits:
    print(f[0])

print([f[0] for f in fruits])

# in
#8 kyu Enumerable Magic #3 - Does My List Include This?


# 7kyu map(function,seq)
# 7 kyu Enumerable Magic #5- True for Just One?


#8 kyu Enumerable Magic #30 - Split that Array

#8 kyu Enumerable Magic #20 - Cascading Subsets


#recursion [::-]
#回文的几种写法

#输入：“爸爸的爸爸是爷爷”
#输出：“爷爷是爸爸的爸爸”

#第一种递归：简洁易懂


def revers_self(sl):

    if len(sl[1:]) == 0:return sl

    else:return revers_self(sl[1:])+sl[0]

sl = 'I love python'
sl = "爸爸的爸爸是爷爷"

print(revers_self(sl))

#爷爷是爸爸的爸爸

# 第二种：循环
inp = "爸爸的爸爸是爷爷"
out = "爷爷是爸爸的爸爸"

rev = []
for i in range(len(inp)-1,0,-1):
    #why len(inp)-1 intead of len(inp)
    rev.append(inp[i])
print(''.join(rev))


# 第三种：地址下标切片
inp = "爸爸的爸爸是爷爷"
out = "爷爷是爸爸的爸爸"

print(inp[::-1])


# 第四种：reverse函数

inp = "爸爸的爸爸是爷爷"
out = "爷爷是爸爸的爸爸"
print(''.join(reversed(inp)))


#判断变量类型的综合任务
template = {'name':str, 'age':int, 'h_weight':tuple}
phil = ['lihongfei',(145,40),True,9]
