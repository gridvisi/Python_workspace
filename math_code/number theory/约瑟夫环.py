nums = 41
call = 3

# 参数定义：
peoples = []
for _ in range(nums):
    peoples.append(True)

result = []
num = 1
# 主逻辑
while (any(peoples)):
    for index, people in enumerate(peoples):
        if people:
            if num == call:
                peoples[index] = False
                result.append(index + 1)
                #                print(index+1)#每轮的出局者
                #                print(peoples)#每次的队列状态
                num = 1
            else:
                num += 1
print('-' * 25)
print('\n总数为%d,报数为%d' % (nums, call))
print('约瑟夫序列为：\n%s\n' % result)
print('-' * 25)

'''
什么是约瑟夫环问题？
约瑟夫，是一个古犹太人，曾经在一次罗马叛乱中担任将军，后来战败，他和朋友及另外39个人躲在一口井里，
但还是被发现了。罗马人表示只要投降就不死，约瑟夫想投降，可是其他人坚决不同意。怎么办呢，他想到一个主意：

让41个人围成一个圆圈，从第一个人开始报数，数到3的那个人被旁边的人杀死。这样就可以避免自杀了，
因为犹太人的信仰是禁止自杀的。结果一群人杀来杀去最后只剩下两个了，就是约瑟夫和他朋友，
于是两人愉快地去投降了。
约瑟夫和朋友站在什么位置才保住了性命呢，这就是我们今天要讲的约瑟夫环问题。
'''
from collections import deque
def dead_live(person,nth):
    circle = [i for i in range(nth,person)]+[i for i in range(nth)]
    #print(circle)
    d, result = deque(circle), []
    while d:
        result.append(d.popleft())
        d.rotate(-(nth-1))
    return result
person,nth = 41,3
print(dead_live(person,nth))

'''
Test.assert_equals(josephus_survivor(7,3),4)  pass
Test.assert_equals(josephus_survivor(11,19),10) = 12 should equal 10
Test.assert_equals(josephus_survivor(1,300),1) = 265 should equal 1
Test.assert_equals(josephus_survivor(14,2),13)  pass
Test.assert_equals(josephus_survivor(100,1),100) = 0 should equal 100

'''

def josephus_survivor(n, k):
    v = 0
    for i in range(1, n + 1): v = (v + k) % i
    return v + 1
n, k = 41,3
print(josephus_survivor(n, k))
