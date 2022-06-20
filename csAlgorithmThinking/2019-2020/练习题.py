__author__ = 'Administrator'
def cal(*args):
    for n in args:
        print(n)
L = [1, 2, 3]
T = (1, 2, 3)
cal(*L)
cal(*T)


def tmpF(a):
    a=10
nint=2
tmpF(nint)
print(nint) #结果仍是2

def tmpF(a):
    a.append(2)
nx=[]
tmpF(nx)
print(nx) #nx=[2]

# 以问路的生活实例来解释递归函数
import time

# 问路，得先有问的人，需要定义一个列表
person_list=['alex','wupeiqi','yuanhao','linhaifeng','sb']
#
def ask_way(person_list):
    print('-'*60)
    if len(person_list) == 0:   # 该条件表示该问的人都问完了，没人知道路
        return '没人知道'       # 终止
    person=person_list.pop(0)    # 一次弹出一个人
    if person == 'linhaifeng':   # 该条件表示这个人知道路
        return '%s说:我知道,老男孩就在沙河汇德商厦,下地铁就是' %person
    print('hi 美男[%s],敢问路在何方' %person)
    print('%s回答道:我不知道,但念你慧眼识猪,你等着,我帮你问问%s...' %(person,person_list))
    time.sleep(3)
    res=ask_way(person_list)
    print('%s问的结果是: %res' %(person,res))
    return res

res=ask_way(person_list)
print(res)