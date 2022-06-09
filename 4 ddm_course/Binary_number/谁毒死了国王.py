'''
https://www.codewars.com/kata/58c47a95e4eb57a5b9000094/train/python

对100瓶毒药进行二进制编码，0000001，0000010，...，1100100

老鼠分别为A,B,C,D,E,F,G

A老鼠喝编码格式为1xxxxxx的药水

B老鼠喝编码格式为x1xxxxx的药水

C老鼠喝编码格式为xx1xxxx的药水

D老鼠喝编码格式为xxx1xxx的药水

E老鼠喝编码格式为xxxx1xx的药水

F老鼠喝编码格式为xxxxx1x的药水
G老鼠喝编码格式为xxxxxx1的药水
最后查看老鼠死亡情况，假如E和F死亡，说明0000110为毒药。

@test.describe("Basic Tests")
def tests():
    test.assert_equals(find([0,3,5,4,9,8]),825)
    test.assert_equals(find([0,1,9,3,5]),555)
    test.assert_equals(find([0,1,2,3,4,6]),95)
    test.assert_equals(find([0,1,3,4]),27)

'''
print(bin(1000))
print(type(bin(3)))
print(int('0b100000001',2))
#1-1000之内转为二进制后，第一位是1的二进制数？

rat_1 = [] #
rat_2 = []
rat_3 = []
rat_4 = []

# 例如死掉的老鼠编号是0，1，3，4，那么老鼠喝掉的哪些编号瓶子里的酒？
# 遍历0-999的每个整数n，转换二进制数后，判断第7位是1的所有数

def judgeNum(total,arr): #所有瓶子总数，arr=死去老鼠的编号数组
    start = list(len(bin(total)[2:]) * '0')
    for i, e in enumerate(start):
        if i in arr:
            start[len(start)-i-1] = '1'
    print(start)
    ans = ''.join(start[len(start)-1 - sorted(arr)[-1]:])
    return int('0b'+ans,2)
total,arr = 999,[0,1,3,4]
total,arr = 999,[0,1,2,3,4,6]
total,arr = 999,[0,1,9,3,5]
total,arr = 999,[0,3,5,4,9,8]
print('final:',judgeNum(total,arr))

common = {}
common = set(rat_1)&set(rat_2)&set(rat_3)&set(rat_4)
print('common:',common)


common = []
for n in range(1,1001):
    if n in rat_1 and n in rat_2:
        common.append(n)
print(common)


'''
find([0,1,3,4]),  27)
如果编号0，1，3，4的老鼠死了，那么就是第27号瓶子里有毒！
'''




'''
for n in range(total+1):
        
    nb,l = bin(n)[2:],len(bin(n)[2:])

    binn = (len(bin(999)[2:])-len(nb))*'0' + nb
    #print(binn)
    if binn[l-1] == '1':
        rat_1.append(n)
    if binn[l-2] == '1':
        rat_2.append(n)
    if binn[l-4] == '1':
        rat_3.append(n)
    if binn[l-5] == '1':
        rat_4.append(n)
#print(rat_1)
print(rat_4,len(rat_4))

'''

'''
def find(r):
    # Your code here

r = [0,3,5,4,9,8]
r = [0,1,9,3,5]
r = [0,1,2,3,4,6]
r = [0,1,3,4]
print(find(r))


def find(r):
    return sum(2**i for i in r)
'''
