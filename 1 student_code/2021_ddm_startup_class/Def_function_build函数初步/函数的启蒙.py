li = 9
liu = 10

print(li + liu)

def plus(a,b):
    return a * b
a,b = 10,10
print(plus(a,b))

apples = [1,2,3,4]
print(sum(apples)) #ne

ans = 0
for i in apples:
    ans += i
print(ans)


names = ['zhang',"su zhuoyao","zhimo","xing"]

def sort_alpha(names):
    return sorted(names)
print('姓名排序：',sort_alpha(names))



import random
print("who answer question? ",random.choice(names))

# 蜜雪冰城点饮料
# 你买了 2 杯饮料：
items = ['coffee','tea'] # list
#items.remove("coffee")
print('remove testing:',items)

# Ada咖啡
items = ['coffee','tea']

# Ada 说我喝咖啡喝茶都可以,但有咖啡的时候，先选咖啡
Ada_like = ['coffee','tea']
items.remove("coffee")
items.remove("tea")
items.append("orange juice")
items.extend(Ada_like)
items.append(['coffee','tea']) #追加，添加
items.extend(['coffee','tea']) #延长

items.extend("milk tea")
print('items',items)
#expand : 拓展, 搬家公司，点菜；append 整存争取，extend；银行零存整取，
Ada_like = "Ada drink:",  "coffee" if "coffee" in items else "tea" if "tea" in items else "不选了"
print(Ada_like)

#expand ： 一个一个，整体一起；

#delete
#Xing deepl
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
# 先判断桌子上的饮料是否能满足Ada？思考为什么用 or ？
print(items)
print("Ada-1:","coffee" not in items or "tea" in items)

# 测验：
print("测验1：",1 == 1 or "coffee") #输出结果是什么？

print("测验2：",1 == 0 or "coffee") #输出结果是什么？
# 体验：
print("体验3：",'coffee' or 'tea')

print("测验4：",1 == 0 or "coffee" == "tea") #输出结果是什么？

#carefree
# 接着Betty来了，她只喝咖啡
Betty_like = ['coffee']
#Betty_like = 'coffee'
print("Betty drink:","coffee" if Betty_like[0] in items else "不点喝的了")

# 桌上只剩茶了
items.remove("coffee")
items = ['tea']

#下面表达正确吗？Yes or Not
print('python answer:',"coffee" or "tea")
print('python answer:',"python" or "tea") #

print("Betty:","coffee" in items or "tea" in items)

# 这种表达对吗？s
print("Betty:","coffee" if "coffee" in items else "tea" or "tea" in items)

print('10 % 2:',10 % 2 == 1) #取余数,pear 不能梨

if 10 % 2:  # 0 == false  #改成11以后，为啥还是要学编程
    print("xing play game!")
print("study proramming")

#只游戏，不编程的写法, ada 人在家，但是魂在教室，下不为例
if 10 % 3:  # 0 == false  #改成11以后，为啥还是要学编程
    print('ada plan a',"xing play game!")
else:
    print('ada paln b',"study proramming")

print("永远想玩游戏的条件：")
if True:
    print("xing play game!")
print("study proramming")

print("永远不想让他玩游戏的条件：")
if False:
    print("永远没有机会：","Xing play game!")
print('一定会显示:',"study proramming")

print("%%%%%%%%%%%%%  the fourth solve   %%%%%%%%%%%%%%%%%%%%%%")

if True:
    print("xing play game!")
else:
    print("study proramming")

print('逻辑判断符合和数字的关系：',1 == True, 0 == False)

print("%%%%%%%%%%%%% the fourth solve %%%%%%%%%%%%%%")
if 1:
    print("xing play game!")
else:
    print("study proramming")

x = - 1
print( -x)
#结论：等同学到齐了，再决定分给每个人喜欢的饮料！

# Cathy进来点咖啡
items = ['tea']
print("coffee" and "tea") #
print('tomas:',1 or 0)
print('xing:',0 or 1)

print('sun:',1 and 0)
print('zimo:',0 and 1)
# 100 内所有能被3，7整除数？
ans = []
for n in range(1,101):
    if n % 3 == 0 or n % 7 == 0:
        ans.append(n)
print(ans)

'''
1、公历年份是4的倍数的，不肯定都是闰年。
2、公历年份是整百数的，必须是400的倍数才是闰年。
3、500，1000，1200，
如何判断？下一个闰年是哪一年

要判断某一年是不是闰年，一般方法是用4或400去除
这一年的年份数：

如果if除得的商是整数而没有余数，那么这一年是闰年；

如果if有余数，那么这一年是平年。
'''
year = 2100
# 能整除100，再看能不能整除400

def hundred(n):
    return n % 100 == 0
#n = 101
#print('Step 1st: 能整除100？',hundred(n))

def fourhundred(n):
    return n % 400 == 0
#n = 800
#print('Step 2nd:能整除100？',hundred(n))

def four(n):
    return n % 4 == 0
#n = 800
#print('Step 3rd : 能整除4？',hundred(n))
n = 2000

#算法思路：
#1 至少要满足，或必须满足的条件是什么

#2 还有哪些条件要满足？and 还是 or？

#3 如何用编程语言表达第1和2的逻辑关系？

n = 2020  #year

#1 讨论下列写法一是否正确？
if four(n) and hundred(n) and fourhundred(n):
    print(f"n = {n}是闰年")
else:
    print(f"n = {n}不是闰年")


#2 讨论下列写法二是否正确？
n = 2000
if four(n) or hundred(n) and fourhundred(n):
    print(f"n = {n}是闰年")
else:
    print(f"n = {n}不是闰年")

#3 讨论下列写法三是否正确？
n = 2000
if four(n) or hundred(n) and fourhundred(n):
    print(f"n = {n}是闰年")
else:
    print(f"n = {n}不是闰年")


#其他写法
print(year)
if year % 4 == 0 or year % 400 <= 100:
    print(f"{year}是闰年")
else:
    print(f"{year}不是闰年")

print("************************")

def leapYear(n):
    if fourhundred(n) or not hundred(n) and four(n):
        return True
n = 2400
print('leapY：',leapYear(n))

year = 2021
while not leapYear(year):
    year += 1
print(year)

for i in range(2020,2101):
    if leapYear(i):
        print(i)
        break

def leapYear1(n):
    if  hundred(n) and not fourhundred(n) :
       return f"n = {n} 不是闰年"

    elif hundred(n) and fourhundred(n) :
        return f"n = {n}是闰年"

    elif four(n):return f"n = {n}是闰年"
    else: return f"n = {n} 不是闰年"

def leapYear2(n):
    if hundred(n) and fourhundred(n):
        return f"n = {n}是闰年"
    else:
        if fourhundred(n) or four(n):
            return f"n = {n}不是闰年"

