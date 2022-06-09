'''
# 16. Parisa set her stones in groups on the desk.
After she arranged the stones in groups of
3, she found that there were 2 stones left.
Then she arranged the stones in groups of 5, and
again there were 2 stones left.
At least how many more stones does she need so that there
won’t be any left when she arranges them in groups of 3 and
in groups of 5?
'''
# math solution:
'''
suppose the stone's number is x:
The number of group-3 is i,number of group-5 is j

x = 3*i + 2 = 5*j + 2

如果满足x同时除尽3和5，那么至少增加多少？
问题等价转换为：2+delta整除5，同时整除3
那么3和5的最小公倍数是3*5 = 15
推得，可以忽略3*i和5*j，只需考虑从2开始递增直到能同时整除3和5即是答案
delta = 13，x = 3*i + 15整除3；5*j + 15整除5
所以答案是还需要添加13块石头
'''

for stone in range(1,977):
    if stone % 5 == 2 and stone % 3 == 2:
        bench = stone
        #print(bench)
    elif stone%5 == 0 and stone%3 == 0:
        result = stone - bench
        break
print('for loop:',stone - bench,stone,bench)



stone = 1 #初始化变量stone
while stone%5 != 0 or stone%3 != 0:
    if stone%5 == 2 and stone%3 == 2:
        bench = stone
#    elif stone%5 == 0 and stone%3 == 0:
#        result = stone - bench
    stone += 1
print('while loop:',stone - bench)

'''
# 19. There are 5 songs: song A lasts 3 minutes, song B 2 minutes 30 seconds, song C 2
minutes, song D 1 minute 30 seconds, and song E 4 minutes. These 5 songs are playing in the
order A, B, C, D, E in a loop without any breaks. Song C was playing when Andy left home.
He returned home exactly one hour later. Which song was playing when Andy got home?
'''



'''
# 24. Granny has 10 grandchildren. Alice is the eldest. One day, Granny notices that her
grandchildren all have different ages. If the sum of her grandchildrens’ ages is 180, what is the
youngest Alice could be?

(A) 19 (B) 20 (C) 21 (D) 22 (E) 23
'''

refer = 0


def oldest(ages):
    s, total = 1, 0  # smallest
    while total <= 180:
        total = sum([i for i in range(s, s + 10)])
        s += 1
    seq = [i for i in range(s-1, s-1 + 10)]
    bench = ['old:',s,max(seq),seq,sum(seq)]
    return max(seq)
ages = 180
print(oldest(ages))

s = 0
while True:
    total = sum([i for i in range(s, s + 10)])
    if total <= 180:
        s += 1
    else:
        print('old',s,max([i for i in range(s, s + 10)]))
    break




print(sum([i for i in range(13,23)]))
print(sum([i for i in range(14,24)]))
print('total=180:',sum([14,15,16,17,18,19,20,21,22,23]))

refer = 0
num = [i for i in range(100)]
for start in num:
    if sum(num[start:start+10]) == 180:
        #print(max(num[start:start+10]))
        refer = max(num[start:start+10])
        print(refer)


'''

smallest = 1
while True:
    if sum([i for i in range(smallest, smallest + 10)]) == 180:
        print(max([i for i in range(smallest, smallest + 10)]))
    smallest += 1

'''

