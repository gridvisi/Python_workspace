__author__ = 'Administrator'


def move(n, a, b, c):
    count = 0
    if n == 1:
        print(a + ' move to ' + c)
        return 1
    else:
        count += move(n - 1, a, c, b)
        count += move(1, a, b, c)
        count += move(n - 1, b, a, c)
        return count


n = int(input("输入汉诺塔的个数："))
print(move(n, 'A', 'B', 'C'))

############################
'''
i = 0
def Num():
    global i
    i=i+1
    print('cishu',i)
############################

if __name__=="__main__":
    n = int(input("请输入需要移动的盘子数："))
    # a = str(input("第一个柱子的名字"))
    # b = str(input("第二个柱子的名字"))
    # c = str(input("第三个柱子的名字"))
    move(n, 'a', 'b', 'c')    # 这里需要给 a b c 加 '' ，不然会显示未定义 a b c
'''
'''
n = int(input('box:'))
counter = 1
while True:
    if n > 1:
        if int(n%2) == 0:
            counter += 1
            n /= 2
        if int((n%2) == 1:
            counter += 1
            n = (n-1)/ 2

    break
print(n,counter)

    #if n == 1:
print(counter,n)
#print(box)
'''

box = [i for i in range(n)]

# print(int(242/2) == n/2,int(242/2),242/2)
def divide(n, i):
    if n % 2 == 0:
        i += 1
        n = n / 2

    elif n % 2 == 1:
        i += 1
        n = (n - 1) / 2
    return n, i


print(divide(243, 0))
'''
#for n in range(3000):
n = 3000
counter = 10


def div(n, counter):
    global n
    while n > 1 and counter > 0:
        if int(n % 2) == 0:
            counter -= 1
            n /= 2
        elif int(n % 2) == 1:
            counter -= 1
            n = (n - 1) / 2
        return n,counter

for  i in range(10):

    div(n, counter)
    counter -= 1
    print(div(n, counter)) #counter == 0 and n == 1:

'''

n = int(input('box:'))
counter = 0
while n > 1:
    if int(n%2) == 0:
        counter += 1
        n /= 2
    if int(n%2) == 1:
        counter += 1
        n = (n-1)/2
print(n,counter)




