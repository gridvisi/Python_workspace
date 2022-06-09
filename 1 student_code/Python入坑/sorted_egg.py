
def usdcny(usd):
    return f"{round(usd * 6.75,2)} Chinese Yuan"

usd = 1
print(usdcny(usd))

def usdcny(usd):
    return '%.2f'%usd * 6.75 #+ "Chinese Yuan"
usd = 1
print(usdcny(usd))
'''
'%.2f' %

方法一：round（）函数
方法二：'%.2f' %f 方法
方法三：Decimal（）函数
'''


num = [-9,-13,-8,-11,-10,-3]
max_num = float("-inf") # 负穷大 infinite

'''
a = float("inf")
b = float("-inf")
'''
for i in num:  #打擂台
    if i > max_num:
        max_num = i
        print('t:',max_num)
print('max:',max_num)

# 求最小
num = [19,13,8,-11,-10,-3]
min_num = 0
for i in num:  #打擂台
    if i < min_num:
        min_num = i
        #print('t:',max_num)
print('min:',min_num)





print(sorted(num))

location = '重庆shi'
print(location[::-1])
end = len(location)
print(end)
print(location[0:end-1:1])
print(location[0:end:2])
# 1- 100
print([i for i in range(101) if i%5 == 0])
print(list(range(101)[::5]))

print('bool:',11%5 == True,11%5 == False)



#先有鸡，还是先有蛋？
#学习sorted排序，看出排序的规律吗

print(sorted(['鸡','蛋']))
print(sorted(['ji','dan']))
print(sorted(['chicken','egg']))

#sorted函数更多用法-2：

print(sorted(['chongqing','Chongqing']))

#为什么大写在前？
print(ord('C'),ord('c'))
print(chr(60))
print(sorted(['china','taiwan']))

#了解sorted引入key 强大的理由

import string
print(string.ascii_lowercase)
# phil -> qijm
result = ''
for e in 'xyz':
    n = ord(e)
    result += chr(n+1)
print(result)

#Good solution carsae
for e in 'xyz':
    n = ord(e)
    result += chr(n+1)
print(result)

print(100%26)
print('abcdefghijklmnopqrstuvwxyz'[22])

