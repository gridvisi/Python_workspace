#python入门到实践

name = "\tEric Matthes\n"

print("Unmodified:",name)
print(" -------------------  ")

print("\nUsing lstrip():")
print(name.lstrip())

print("\nUsing rstrip():")
print(name.rstrip())

print("\nUsing strip():")
print(name.strip())

fav_num = 42
msg = "My favorite number is " + str(fav_num) + "."
print(msg)

my_age = 10
father_age = 40

#1 定义一个函数 years_after()，分别输出我和父亲的年龄

def years_after(my_age,father_age):
    return                 #左边补齐代码

#2 11月的第1天开始小明买保质期内的牛奶，每天喝1包，现在要求牛奶公司
#  每次送3天的牛奶，这个月按照30天计，请列出牛奶公司送奶的日期,[1,4,7 ... ...]
#  和总共需要送多少包牛奶？



#2-1 上题基础上，改写为函数形式：def milkCount():
# 输入参数分别是：
# 总共需要送的天数 days；
# 每隔几天送： per_day

# 输出的结果是：
# 牛奶公司送奶的日期 [数组格式]
# 总共需要送多少包牛奶 int 整数形式

def milkCount(days,per_day):
    return       #date-> list, total_milk


#3
'''
小喵去一家未来的餐厅，餐厅根据小喵的体检结果建议一份菜单，
按顺序列出菜名，并且建议按顺序取餐，而且当喝到橙汁的时候，建议结束用餐。

中英文对照：
基围虾 = Shrimp
牛排 = steak
'chicken' = 鸡肉
'orange_juice' = 橙汁
'vegetable' = 蔬菜

你的任务是编写一段程序，分别运用while 和 for循环实现下面任务：
显示客人一共吃了哪些菜？

你发现有些写法是错的，你能指出是哪些正确的吗？
'''
#例如 菜单如下
menu = ['Shrimp','steak','chicken','orange_juice','vegetable']
# 正确的输出是 ['Shrimp','steak','chicken','orange_juice']


#第1种 while continue的写法
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



#第3种while 的写法
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
print(ans)

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
        print('第7种:', menu[i])
    else:
        ans.append(menu[i])
    i += 1


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
