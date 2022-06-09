# object programming 面向对象的编程,万物皆是对象
# https://www.codewars.com/kata/588a3c3ef0fbc9c8e1000095/solutions/python
def max_diff(list):
    return max(list) - min(list) if list else 0

word = "客上天然居，居然天上客"
print('客上天然居，居然天上客1:',word[0:4:1]==word[6:10:1][10:6:-1])

def lyc(): #function
    return print("I am niubility coder")
lyc()

print(type(lyc))

word = "油灯点灯油，火柴当柴火"
print(word[0:5][::-1])
print(word.split("，")[1])
print(word.split(","))


'''

def horse(x):
    move
'''


arr = [172,165,160,142,135]
arr = [150]+arr
print(arr)

print('arr[0:4:2]',arr[::-1])

for i in range(0,len(arr),2):
    print(arr[i])
print('[0::2]',arr[0::2])

print(arr[0:len(arr):2])
print(arr[::-1])
print(arr[1:3+1])
print(sorted(arr)[::-1])


word = "上海自来水来自海上"
word = "天连碧水碧连天"

word = "油灯点灯油，火柴当柴火"
print(word[0:5][::-1])
print(word.split(",")[1])

word = "12,21,24,42".split(',')
#word = "奥利;奥"

ans = []
print("ANS: ", end='')
for i in range(0, len(word), 2):
    ans.append(word[i] == word[i+1][::-1])
print(ans)
word = "客上天然居，居然天上客"
print('客上天然居，居然天上客:',word[0:4:1]==word[5:0:1][10:7:-1])
print(word[2],word[2][::-1])
print(word[i+1][::-1])
#print("ANS collection:", [word[i] == word[i+1][::-1] for i in range(0,len(word),1)])

print('回文联:', word[0:5][6:]== word[0:5][6:][::-1])           #sorted(list(word),reverse=True)
print(word[0:5][6:10])

arr = ["ddm"] * 10
print(arr.pop())
print(len(arr))
print('how much ddm in arr:',arr.count("ddm"))
print(arr)

re = []
for i in range(1,10,2):
    re.append(i)
print(re)
#for i in arr:

for i,e in enumerate(arr):
    print(i,e)

#res = [i+1 for i in arr]
#print(res)

n = 2

'''

import queue

from collections import deque
#dq=deque(['a','b','c'])
dq=deque(arr)
s = dq.popleft()
dq.append(s+1)

dq.appendleft(dq.pop())

print(dq)


#dq.append('c')
print (dq)
print (dq.pop())
print (dq)
print (dq.popleft())
print (dq)
#dq.appendleft('d')
print (dq)
print (len(dq))
'''



