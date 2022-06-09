import random
name = 'xingtianrui'
name = 'liuxuejun'
print('输出结果：',name.index('u',5,len(name)))

#index '012345678910'

print(len(name))
print(name[0])
#print(name[11-1]) #string index out of range

print(list(range(10,-10,-5)))

print(list(range(10,0,1)))
start = int(10.5*2)
end = int(0.5*2)
step = -2
print('int:',list(range(start,end,step*2)))

dice = [1,2,3,4,5,6]
dice = [i for i in range(1,7)]
#range 整数 -> 整数 -> step步数
range(9,49)
print('range:',list(range(0,100,17)))
print('cellphone:',len(list(range(0,365,3))))
print('computer/laptop:',len(list(range(0,365,5))))



print('dice:',dice)
dices = ["Rock", "Paper", "Scissors"]
print(dice)
print(random.choice(dices))

#Rock, Paper, Scissors


#Top 1 不习惯用高级数据结构
def common_elem(list1,list2):
    common = []
    for i in list1:
        if i in list2:
            common.append(i)
    return common
list1,list2 = [1,3,5,7],[2,4,6,8]
print(common_elem(list1,list2))


def common_elem(list1,list2):
     common = set(list1).intersection(set(list2))
     return common
list1,list2 = [1,3,5,7],[2,4,6,8]
print(common_elem(list1,list2))


# dict.get


# tuple: enumerate, dict.item()