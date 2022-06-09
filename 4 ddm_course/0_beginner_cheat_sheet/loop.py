'''
一、一个整数n, 如何知道n是几位数？
例如：100，999都是3位数；10，90都是2位数
下面哪个函数是可以实现？

1）len(n)
2)  len(str(n))
3)  while
'''

def cuntDigit(n):
    cunt = 0
    while n > 0:
        n //= 10
        cunt +=1
    return cunt
n = 9223
print(cuntDigit(n))





'''

#什么时候退出while循环？invalid character in identifier识别码中的无效字符
 prompts = "\nTell me something, and I'll"
prompt s += "repeat it back to you." 
prompts += " \nEnter 'quit'to end the program. "

message = " " 

while message !='quit':
    message = input(prompts)
    if message !='quit': 
        print(message)

'''

s = "\nTell me something, and I'll"
s += " repeat it back to you."
s += " \nEnter 'quit'to end the program:  "

message = ""

while message != "quit":
    message = input(s)
    if message !='quit':
        print(message)

#Using flag
s = "\nTell me something, and I'll"
s += " repeat it back to you."
s += " \nEnter 'quit'to end the program:  "
active = True
while active:
    message = input('请输入：')
    if message == 'quit':
        active = False
    else:
        print(message)


#Using break to exit a loop 

prompt = "\nwhat cities have you visited?"
prompt +="\nEnter 'quit'when you're done."

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I've been to" + city +"I " + "!")


# 7 kyu Driving School Series #1
# https://www.codewars.com/kata/58999425006ee3f97c00011f/train/python
def passed(lst):
    s = [i for i in lst if i <= 18]
    return round(sum(s)/len(s)) if len(s) else 'No pass scores registered.'

from statistics import mean
def passed(demerits):
    return int(round(mean([d for d in demerits if d < 19] or [0]))) or 'No pass scores registered.'