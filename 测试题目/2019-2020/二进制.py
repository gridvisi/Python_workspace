
#1 取出每一个车牌
#2 判断车牌号尾数是不是奇数
#3 如果是奇数，那么就不同意上路
#4 如果是偶数，那么就同意上路
num_plate = ['渝A9919','渝C5072','渝A2966','渝D8371','渝A3417','渝A5255']
for s in num_plate:
    if int(s[-1]) % 2 == 1:
        print(s,'okay')
    if int(s[-1]) % 2 == 0:
        print(s,'not access')




x = '渝A9919'[-1]
print(type(x))  #字符串
x = 7
print(type(x))
if int(x) % 2 == 1:
    print('通过')


fruit = ['apple', 'orange', 'banana']
s = 'pear'
if s in fruit:
    print('有货')
if s not in fruit:
    print('没货')

#4 仔仔为新年买了一大袋苹果，仔仔说见面就分一半。回学校的路上，仔仔前后遇到了5个同学争着要去帮他提，
#  等仔仔到了学校后，苹果只剩一个了，请问仔仔最初买了多少苹果？
#  用数学直接算，但还要用编程实现：如果遇到n个同学，如何迅速得到结果
#  考察二进制的理解
#  请在下面写下你的代码：
#

# 二进制的 1111

person = 5
def apple(person):
    nd = 1
    for i in range(person):
        nd = nd*2
    return nd
print(apple(person))

for s in num_plate:
    if int(s[-1]) % 2 == 1:
        print('okay')
    if int(s[-1]) % 2 == 0:
        print('not access')
'''

10=2
100 = 4
1000 = 8
10000 = 16
100000 = 32

'''