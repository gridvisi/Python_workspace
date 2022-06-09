

def main():
    my_dict = {'子': '鼠', '丑': '牛', '寅': '虎', '卯': '兔',
               '辰': '龙', '巳': '蛇', '午': '马', '未': '羊',
               '申': '猴', '酉': '鸡', '戌': '狗', '亥': '猪'}

    print(my_dict.get('子', '你所查询的键不存在'))

    print(my_dict.get('行', '你所查询的键不存在'))

    # 不设置参数的话，返回None
    print(my_dict.get('行'))


if __name__ == '__main__':
    main()


#2 case

d = {1: 2}
#print(d.get(0, default=0))
#Traceback (most recent call last):  File "<stdin>", line 1, in <module> TypeError: get() takes no keyword arguments
print(d.get(0, 0))