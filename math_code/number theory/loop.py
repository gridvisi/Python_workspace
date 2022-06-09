__author__ = 'Administrator'
num = [' ','A','B','C','D','E','F','G']
def looper(loop):
    """

    :rtype : object
    """
    loop+=1
    load = num[loop]
    num[loop] = num[loop+2]
    num[loop+2] = load

loop = 0
while loop< 4:
    looper(loop)
    loop+=1
    str = num[1]+num[2]+num[3]+num[4]+num[5]+num[6]+num[7]

i = 0
str = 'CFEDABG'
def ding(x,y):
    num = list(x)
    print(num)
    loop = 0
    while loop < 4:
        looper(loop)
        loop +=1
        temp = (num[0])+num[1]+num[2]+num[3]+num[4]+num[5]+num[6]
        num_loop = list(temp)
    num = num_loop
    i += 1
while i < 1000:
print("计算结果:",num)