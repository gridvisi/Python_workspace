# 反复做不烦的，吃饭
# 打游戏越打越好玩，所有的游戏，哈利波特魔法觉醒；环球影城；喝牛奶；
# 越做越烦，写作业；点击关闭网络广告；打不了游戏；
# 不复习;不写作业；

like_junlin = ["play game","Universal Studios","buy"
               "computer","starbuck","harrypott",
               "Severus Snape","萨拉查斯莱特林","snake"                                         
               "Jurassic","Kentucky","哈利波特斯内普"]

like_feifei = ['eat',"food","milk",'play game','comic'
               ,'aotuworld',"ray"]

dislike_junlin = ['chatter',"banana","Broccoli","egg"]

dislike_feifei = ["homeworks","Broccoli"]

#set 集合

common = set(like_junlin) & set(like_feifei)
print('common:',common)

commondislike = set(dislike_junlin) & set(dislike_feifei)
print(commondislike)


print('俊霖喜欢的项目有：',len(like_junlin)) #length
print('俊霖不喜欢的项目有：',len(dislike_junlin))


def prices(s):
    if s >= 1 and s < 3:
        return s * 40
    if s > 3 and s < 7:
        return s * 40 - 20
    if s >= 7:
        return s * 40 -50



#第一题：输出我最喜欢的数字
#先赋值给变量 fav_num
#然后，用字符串形式输出

fav_num = 42
msg = "My favorite number is " + str(fav_num) + "."
print(msg)


#第二题：若干年后各自多少岁？

#定义一个函数 years_after(my_age,father_age, n)，
#输入：我和父亲今年的多少岁，n是若干年后各多少岁
#输出：我和父亲的年龄

def years_after(my_age,father_age, n):
    return                 #左边补齐代码

my_age = 10
father_age = 40
#print(years_after(my_age,father_age)



#第三题 送牛奶的日期
#每月的第1天开始小明买保质期内的牛奶，每天喝1包，现在要求牛奶公司
#每次送3天的牛奶，按照30天计，请列出牛奶公司送奶的日期,[1,4,7 ... ...]
#和总共需要送多少包牛奶？

# 提示可以运用切片，或者是for循环实现


#第四题是在上题基础上，改写为函数形式：
def milkCount(days,per_day):
    return ""
'''
输入参数分别是：
总共需要送的天数 days；
每隔几天送： per_day
输出的结果是：

牛奶公司送奶的日期 [数组格式]
总共需要送多少包牛奶 int 整数形式
'''
def milkCount(days,per_day):
    return       # 补齐代码 date-> list, total_milk

'''


第五题 结束用餐

小喵去一家未来的餐厅，餐厅根据小喵的体检结果建议一份菜单，
按顺序列出菜名，并且建议按顺序取餐，而且当喝到橙汁的时候，建议结束用餐。
菜单如下
'''
menuEN = ['Shrimp','steak','chicken',
        'orange_juice','vegetable']

menuCN = ['基围虾','牛排','鸡肉','橙汁','蔬菜']


print(zip(menuEN,menuCN)) #地址
# list()
print(list(zip(menuEN,menuCN)))
# dict()
print(dict(zip(menuEN,menuCN)))

menuDict = dict(zip(menuEN,menuCN))
print(menuDict['steak'])
#print(menuDict['hotpot']) #key
print(menuDict.get('fish',"没有这盘菜"))
print(list(range(1,10)))

#算法
#1 - 100 偶数：even，odd：奇数 字典：{even：
print([i for i in range(250) if not i%2])
print(list(range(250))[0:101:2])
#算法！

#1 == True, 0 == False
print(not False)

# statement
# 公鸡一打鸣，天就会亮！
print(all([i%2==0 for i in [2,4,6]])) #True
# all 全部
# any 只要有一个满足，就输出True

print(any([i%2==0 for i in [2,4,6]])) #True


#lizhenjie online study
#False


ddmStudent = {'ddm':"刘致远",
              'phil':"李鸿飞",
              'lzj':"lizhengjie"}
#字典 key:value

print('ddmstudent:',ddmStudent['ddm'])

'''

[Shrimp
牛排 = steak
'chicken' = 鸡肉
'orange_juice' = 橙汁
'vegetable' = 蔬菜]
'''

#正确的输出是 ['Shrimp','steak','chicken','orange_juice']

'''

附上中英文对照：
基围虾 = Shrimp
牛排 = steak
'chicken' = 鸡肉
'orange_juice' = 橙汁
'vegetable' = 蔬菜

你的任务是编写一段程序，分别运用while 和 for循环实现下面任务：
显示客人一共吃了哪些菜？

你发现有些写法是错的，你能指出是哪些正确的吗？
'''

#第1种 while continue的写法
menu = ['Shrimp','steak','chicken',
        'orange_juice','vegetable']
i = -1
ans = []
while i < len(menu)-1:
    i += 1
    if menu[i] != 'orange_juice':
        ans.append(menu[i])
        continue
print('第1种:',ans)
#第2种for 循环的写法

menu = ['Shrimp','steak','chicken','orange_juice','vegetable']
ans = []
for dish in menu:
    if dish == "orange_juice":
        break
    else:ans.append(dish)
print('第2种：',ans)

#第3种while 循环写法

menu = ['Shrimp','steak','chicken','orange_juice','vegetable']
i = 0
ans = []
while i < len(menu)-1:
    if menu[i] != 'orange_juice':
        ans.append(menu[i])
        i += 1
print('第3种:',ans)

#第4种while continue的写法

menu = ['Shrimp','steak','chicken','orange_juice','vegetable']
i = 0
ans = []
while(i < len(menu)-1):
    if menu[i] != 'orange_juice':
        ans.append(menu[i])
        continue
    i += 1
print('第4种:',menu[i])

#第5种for循环的写法

menu = ['Shrimp','steak','chicken','orange_juice','vegetable']
ans = []
for dish in menu:
    if dish == "orange_juice":
        break
    else:ans.append(dish)
print("第5种：",ans)

#第6种while continue的写法

menu = ['Shrimp','steak','chicken','orange_juice','vegetable']
i = 0
ans = []
while(i < len(menu)-1):
    if menu[i] != 'orange_juice':
        ans.append(menu[i])
    i += 1
print('第6种:',menu[i])
#第7种while的写法

menu = ['Shrimp','steak','chicken','orange_juice','vegetable']
i = 0
ans = []
while i < len(menu)-1:
    if menu[i] == 'orange_juice':
        ans.append(menu[i])
        print('第7种:', ans)
    else:
        ans.append(menu[i])
    i += 1


