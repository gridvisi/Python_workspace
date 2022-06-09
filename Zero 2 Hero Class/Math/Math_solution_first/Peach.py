__author__ = 'Administrator'
'''
1979年，李政道博士给中国科技大学少年班出过一道知趣题：5只猴子分一堆桃子，怎么也分不成5等分，
只好先去睡觉，准备第二天分。夜里1只猴子偷偷爬起来，先吃掉一个桃子，然后将其分为5等份，
藏起自己的一份就去睡觉了；第二只猴子又爬起来，吃掉一个桃子后，也将桃子分成5等份，藏起自己的一份睡觉去了；
以后的3只猴子都先后照此办理。问最初有多少个桃子？
'''
total=1

for i in range(5):
    total=total*5+1
print(total)


'''
def consume(monkey):

    if monkey == 1:
        return 4
    elif monkey == 2:
        return consume(1)*1.25+1
    elif monkey == 3:
        return consume(2)*1.25+1

print(consume(3))
'''
'''
monkey=1
peaches=1
peach=1

while monkey<=5:
    if peach%5==1 and (peach-1)%5==0:
        peach=(peach*4)/5
        monkey+=1
    else:
        peaches+=1
        peach=peaches
        monkey=1
print(peaches)
'''
'''
def peach(num,monkey):
    """

    :rtype : object
    """
    if((num-1)%monkey)==0 and ((num)%monkey==1):
        return (num-1)*0.8
    else:return 0
print(peach(1001,5))

monkey=5
num=1
for num in range(1000):
    if((num-1)%monkey)==0 and ((num)%monkey==1):
        print(num)

'''
'''
f = lambda x: x - x//5 - 1
f(f(f(f(f(5**5)))))
            # 当然这样写，比较丑陋

x = 5**5
for _ in range(5):
    x = f(x)
print(x)

'''

def peach(monkey=5):
    pea = 4  ##最后一个猴子分完剩余的桃子
    while 1:
        num = pea
        for i in range(monkey):
            num = num + num / 4 + 1
            if num % 1 != 0:  ##如果分出了小数则结束内层循环
                pea += 4  ##最后的桃子一定是4的整数倍
                break
        if num % 1 == 0:  ##如果是整分 则结束
            break
    return pea, num


if __name__ == '__main__':
    pea, num = peach()
    print(pea, num)


