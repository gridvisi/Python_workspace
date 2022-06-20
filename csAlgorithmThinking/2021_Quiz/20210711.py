
print('mayun')
print(1 + 2)
print('1' + '2')
print('1 + 2')

print('li','jing')

namelist_python = ['phil','morgan'] #list 列表
family = [45,43,15] #number 数字


print(namelist_python)
namelist_python = 'phil','morgan'
print(namelist_python)

print('how to spell your spare time?')
print('football')
spare_time = 'football'
spare_time = None
spare_time = coding = 1
spare_time,coding = 1,1
print(id(spare_time),id(coding))
#身份证号 ID identify
print(spare_time,coding)

'''
https://www.codewars.com/kata/574b3b1599d8f897470018f6/train/python
我这道题来自codewars 8kyu难度，题目名字是8 kyu
What's the real floor
'''
print(1 + True)
print(2 + False)


def getReal(n):
    return n if n <= 0 else n-1 if 1 <= n <= 12 else n-2
    if n <= 0:
        return n
    if 1 <= n <= 12:
        return n-1
    if n > 13:
        return n-2
print("GETREAL:"+str(getReal(-1)))





def get_real_floor(n):
    # code here
    if n==0:return 0
    if n==1:return 0
    if n==5:return 4
    if n==15:return 13




code_ma = 'b11'
code_li = 'b12'

code_ma,code_li = code_li,code_ma

#swap(x,y)
