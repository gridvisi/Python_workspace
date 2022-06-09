lhf = 13
lzl = 9
# 8ky swap
lhf,lzl = lzl,lhf
#lzl = lhf
print('lhf:',lhf,'lzl:',lzl)



n = 1344567890
n = 100
age = [i for i in range(n)]
print(f"{age}",age)





def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    for step in range(x,n+1,x):
        ans = []

    return ans
x, n = 2,5
print(count_by(x, n))

'''
ans.append(x)
        ans.append(x+x)
        ans.append(x+x+x)
'''


#1 列表推导
sl = [i for i in range(11)]
print(sl)

#2
ans = []
for i in range(11):
    ans.append(i)
print(ans)













#1
animal = ['sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'wolf', 'sheep', 'sheep']
step = 0
for x in animal:
    print(f"循环第{step}步：",x)
    step += 1
    if x == 'wolf':
        print(f"羊群的第{step}位的位置有狼")

print(' -------------------------- ')
#enumerate
for i,e in enumerate(animal):
    print(f"循环第{i}步：",e)
    #step += 1
    if e == 'wolf':
        print(f"羊群的右数第{len(animal)-i}位的位置有狼")

print(animal[-3])


#车辆限行
def allow_plate(day):
    num_plate = ['渝A9919', '渝C5072', '渝A7R69', '渝A2966',
             '渝D8371', '渝A3417', '渝A5255', '渝AD991']

    week = ['Mon','Tue','Wed','Thu','Fri']
    num = list(range(10)) #车牌尾号
    print('num:',num)
    rule = {}  #字典存储每周1-5对应的限行尾号，key=周几，value=限行尾号
    # policeman：key=尾号, value = ['Mon','Tue','Wed','Thu','Fri']
    # 遍历
    i = 0
    for d in week:
        print(d)
        rule[d] = num[i::5]  #字典生成关键句法
        i += 1
    return rule,i
day = 'Fri'
print(allow_plate(day))

name = list("李泓霏")
name[1] = '一'
print(name)

phil_encn = {'hello':'你好'}  #key:value
print(phil_encn['hello'])

all_plate = {'mon':[0,5]}
print(all_plate['mon'])

n = list(range(1000))
print(n[0::76])
print([i for i in range(1000) if i%76 == 0])
# 算法效率第一个高