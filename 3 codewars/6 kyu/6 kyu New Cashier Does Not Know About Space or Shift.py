'''
https://www.codewars.com/kata/5d23d89906f92a00267bb83d/train/python
一些新的收银员开始在你的餐厅工作。
他们善于接受订单，但他们不知道如何将单词大写，或使用空格键！他们创建的所有订单看起来是这样的。
他们所做的所有订单看起来都是这样的：
"奶昔披萨鸡肉薯条可乐汉堡披萨三明治奶昔披萨"
厨房的工作人员都威胁要辞职，因为阅读订单是多么的困难。
他们喜欢把订单写成一串漂亮的、干净的、有空格和大写字母的字符串，就像这样："汉堡、薯条、鸡肉、比萨、三明治、奶昔、可乐"。
"汉堡 薯条 鸡肉 披萨 披萨 三明治 奶昔 奶昔可乐"
厨房的工作人员希望菜品的顺序与菜单上出现的顺序一致。
菜单上的项目相当简单，项目名称没有重叠。

1. 汉堡
2. 薯条
3. 鸡肉
4. 比萨
5. 三明治
6. 洋葱圈
7. 奶昔
8. 可乐
'''
from collections import Counter

order = "milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"
#"Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke"
item = 'Burger Fries Chicken Pizza Sandwich Milkshake Coke'

def get_order(order):
    item = 'Burger Fries Chicken Pizza Sandwich Milkshake Coke'
    key = item.split(' ')
    value = [order.count(k.lower()) for k in item.split(' ')]
    return dict(zip(key,value))
print(get_order(order))



print(order.find('piza'),order[4:])
print(order.count('pizza'))
i,re = 0,[]
x = 'milk'
x = 'pizza'
while order[i:].find(x) > -1:
    re.append(x)
    #print(re)
    i += order[i:].find(x) + len(x) + i
print(re,len(re))

order = "pizzachickenfriesburgercokemilkshakefriessandwich"
#"Burger Fries Fries Chicken Pizza Sandwich Milkshake Coke"
print(order.find('burger'))

def get_order(order):
    re = []
    item = 'Burger Fries Fries Chicken Pizza Sandwich Milkshake Coke'
    menu = {1:'Burger',
            2:'Fries',
            3:'Chicken',
            4:'Pizza',
            5:'Sandwich',
            6:'Onionrings',
            7:'Milkshake',
            8:'Coke',
            }
    for k,v in menu.items():
        i = 0
        while order[i:].find(v.lower()) > -1:
            re.append(v)
            i += order[i:].find(v.lower())+len(v)
    return ' '.join(re)
print('while solution:',get_order(order))

MENU = ["Burger", "Fries", "Chicken", "Pizza", "Sandwich", "Onionrings", "Milkshake", "Coke"]

def get_order(order):
    result = []
    for item in MENU:
        result.extend([item for _ in range(order.count(item.lower()))])
    return " ".join(result)

def get_order(order):
    re = []
    item = 'Burger Fries Fries Chicken Pizza Sandwich Milkshake Coke'
    for x in item.split(' '):
        if order.find(x):
            re.append(x)
    return re
print(get_order(order))

'''
Some new cashiers started to work at your restaurant.
They are good at taking orders, but they don't know how to capitalize words, or use a space bar!
All the orders they create look something like this:

"milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"

The kitchen staff are threatening to quit, because of how difficult it is to read the orders.
Their preference is to get the orders as a nice clean string with spaces and capitals like so:
"Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke"
The kitchen staff expect the items to be in the same order as they appear in the menu.
The menu items are fairly simple, there is no overlap in the names of the items:

1. Burger
2. Fries
3. Chicken
4. Pizza
5. Sandwich
6. Onionrings
7. Milkshake
8. Coke

print(order.count('milk'))
print([order.count(k) for k in item.split(' ')])

for k in item.split(' '):
    print(k)
    print(order.count(f"{k}"))

'''




