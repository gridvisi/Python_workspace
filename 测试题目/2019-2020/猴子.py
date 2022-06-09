__author__ = 'Administrator'


def consume(count, num):
    if count == 0:
        return 1
    elif (num - 1) % 5 != 0:
        return -1
    num = (num - 1) * 4 / 5
    return consume(count - 1, num)


print(consume(5, 3121))

count=5
num=1
while num <10000:
    num+=1
    result=consume(count,num)
    if result == 1:
        print(num)





