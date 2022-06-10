

# continue usage
menu = ['Shrimp','steak','chicken','orange_juice','Broccoli']

i = 0
while(i < len(menu)-1):
    i += 1
    if menu[i] != 'orange_juice':
        continue
    else:
        print('while_solve-1',menu[i])


#第2种 while continue的写法 bad infinite loop ?
'''

i = 0
while(i <= len(menu)-1):
    print('test:',i)
    if menu[i] != 'orange_juice':
        #
        continue
    i += 1
print('while_solve_2',menu[i])
'''



#什么时候退出while循环？

#判断满足条件时，退出循环

prompt = "\nTell me something, and I'll"
prompt += " repeat it back to you."
prompt += " \nEnter 'quit'to end the program."

message = " "

while message !='quit':
    message = input(prompt)
    if message !='quit':
        print(message)

#2使用标记flag退出循环

prompt = "\nTell me something, and I'll "
prompt+= "repeat it back to you."
prompt += " \nEnter 'quit'to end the program."

active = False
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:print(message )


#Using break to exit a loop
#使用break退出循环

prompt = "\nwhat cities have you visited?"
prompt +="\nEnter 'quit'when you're done."

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I've been to" + city +"I" + "!")



#
'''
在美国的3亿3千万个手机中寻找一个手机的主人是一个更大的问题。
如果电话公司想通过逐一扫描所有的号码来搜索这3亿个手机号码，
它平均需要检查多少个号码才能找到一个特定的手机号码？

一到一百之间
一百到一百万之间
一百万到十亿之间
十亿或更多
'''
n = 3300000000
cunt = 0
while n > 2:
    n //= 2
    cunt += 1
print(cunt)