'''
https://stackoverflow.com/questions/19422695/python-continue-with-while?r=SearchResults

'''

for i  in range(1,10):
    if i % 2 == 0:
         continue
    print(i)


print("*" * 20)

# Not properly run due to while stuck in i
# continue without increment the value of i <-- stuck here!
i = 0
'''
while(i < 10):
    if i % 2 == 0:
        #print('i = ',i)
        continue
    i += 1
    print(i)
    break
'''


# Move the i += 1 before the even test:

while(i < 10):
    i += 1
    if i % 2 == 0:
        continue
    print(i)

'''
continue操作
小喵将自助餐的每份菜的名字做了英文标记。例如：
基围虾 = Shrimp
牛排 = steak
等等；

他有个习惯，每次吃自助餐总按一个顺序取餐，而且当他取橙汁喝的时候，就意味着用餐结束。
'''
menu = ['Shrimp','steak','chicken','orange_juice','Broccoli']

i = 0
while(i < len(menu)-1):
    i += 1
    if menu[i] != 'orange_juice':
        continue
    print(menu[i])


#第二种while continue的写法
'''
i = 0
while(i < len(menu)-1):
    if menu[i] != 'orange_juice':
        continue
    i += 1
    #print(menu[i])
'''


#Case_study_continue
# 两份菜单，一份是回转寿司；另一份平常点菜

foods_1 = ["Ice cream", "Ham", "Relish", "Pancakes", "Ketchup",
         "Cheese", "Eggs", "Cupcakes", "Sour cream",
         "Hot chocolate", "Avocado", "Skittles","Ice cream",
         "Ham", "Relish", "Pancakes"]

foods_2 = ["Ice cream", "Ham", "Relish", "Pancakes", "Ketchup",
         "Cheese", "Eggs", "Cupcakes", "Sour cream",
         "Hot chocolate", "Avocado", "Skittles","Ice cream",
         "Eggs", "Relish", "Cheese"]


def judgeRotating(arr):
    cunt = 0
    for i in range(len(arr)//2):
        #遍历至折半处
        if arr[:i] == arr[len(arr)-i:]:
        #由两端位置向中间靠近，直至相同时。才执行cunt=i
            cunt = i
        continue #作用是不相同时，循环继续执行

    return arr[:len(arr)-cunt]
arr = foods_1
#arr = foods_2
print(judgeRotating(arr))


