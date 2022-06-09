name = ['xuer','xiaozhe','feifei','liu'] #collections 集合

student = {'xiaozhe':"小哲"}
print(student['xiaozhe'])

code = [1,2,3,4]
codes = [i for i in range(1001)]
print(dict(zip(code,name)))  # dictionary 字典

#餐单
menu = {'sousi': 17,'doufu':10} #key:value
# 客人点菜按菜名，按价格
food = []
price = []

for k,v in menu.items():
    food.append(k)
    price.append(v)
    print(k,v)
print(food,price)

menu_special = dict(zip(price,food))
print(menu_special)
# 张三点豆腐，
print('张三点豆腐:',menu['doufu'])
# 李四说点一盘17块钱
print(menu_special[17])
tony = 10
tony = "fefei"
manvei = {'tony':'钢铁侠'}


# boss
menu_special = {17: 'sousi', 10: {'doufu','vegetable'}}

liu = {''}

conection = {
            "liu":['li','tony'],'feifei':['li','zhangsan'],
             'xiaozhe':['xueer','li'],'xuer':['li','liu'],
            'li':['xuer','feifei','xuer']
             }


#面向对象的编程

#zip:


#Compound interest cal per day 复利计算 @丁丁猫编程营
# 2020
# limited to the "e"  nature whatever period as short as possible
task = '丁丁猫编程营' + '复利的极限是自然数'
# 10000,一年利息 300

capital = 10000
interest_rate = 100*10**-2
period = 1     # interest cal per day
rate = float(period/365)  # 利息折算日利息 print(interest_rate * rate)
def max_interest(capital,interest_rate,round=365//period):
    while round > 0:
        interest = interest_rate * capital * rate
        capital,round = capital + interest,round - 1
    return capital
print(max_interest(capital,interest_rate,round=365//period))
#1万元一年存27145.67482021876