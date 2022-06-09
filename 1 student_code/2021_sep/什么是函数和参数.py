


bread,days = 4,5
print(bread * days)

def totalBread(bread,days): # 一共有多少，总数
    return bread * days
bread,days = 100,7
banana = 300
days = [50,100,150,200]

def totalBread(bread,days): # 一共有多少，总数
    total = []
    for d in days:
        print('d:',d)
        total.append(d * bread)
    return total

print('total: ',totalBread(banana, days))


names = []
print(names)
names.append('Ada')
print(names)
names.append('Thomas')
print(names)
names.append('Phil')
print(names)
print(len(names))
names.append('Jack')
print(len(names))
print(names.index('Jack') + 1)

def two_highest(arg1):  #define two_bigger()
    pass