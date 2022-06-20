__author__ = 'Administrator'
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