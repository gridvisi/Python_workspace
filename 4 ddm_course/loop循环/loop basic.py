
name = '李王优菲'
print(name[0],name[1],name[2],name[3],name[::-1])

#range(0,100,1) == range(100)

'''
for i in range(0,100,1): #start, end ,step
    print(i,end='/')
'''

for i in range(0,100,3): #start, end ,step
    print(i,end='/')

print(['李王优菲','李晶'])
s = ['李王优菲','李晶']
for i in s[0]:
    if i in s[1]:
        print(i)

print(s[0],'hello',s[1])


if 4 % 2 == 0:
    print("it is divided")
else:
    print('Not it is divided')

# 可乐一瓶3元，10元买3瓶，余下1元；3个空瓶换1瓶可乐，
# 喝掉又有1个空瓶，共喝掉4瓶，余下1元和1个空瓶
rmb = 10
print('rmb',rmb)

#loop
rmb = 10
bottle = 0  #pingzi
drink = 0
price = 3
coca = 0
# 3 bottle per 1 cococola

#when where
while rmb > 0:    #
    rmb -= 3  # rmb = rmb -3
    coca += 1 #coca = coca + 1 #每付费3元买一瓶可乐
    print(rmb)
    bottle += 1 # 喝过的空瓶
    drink += 1  # 我喝了一瓶肚子了
    if bottle == 3:
        drink += 1
        bottle -= 3

# 比预期多循环了一次，bottle多出1个，等同于借了2元rmb=-2，加上之前剩的1元，凑够3元又买一瓶
print(bottle,drink-1,rmb)


rmb = 10
bottle = 0  #pingzi
drink = 0
price = 3
while rmb > 0:
    rmb -= 3  # rmb = rmb -3
    print('status:',bottle,drink-1,rmb)
    bottle += 1
    drink += 1
    if bottle == 3:
        drink += 1
        bottle -= 3
    if rmb < 3 and bottle < 3:
        print('2nd:',bottle,drink-1,rmb+price)