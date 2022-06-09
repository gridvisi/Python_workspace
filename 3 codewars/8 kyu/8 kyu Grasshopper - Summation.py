
'''

def summation(num):
    opt = []
    while num:
        opt.append(num)
        num -= 1
    return sum(opt)
num = 10
'''

def summation(num):
    return sum(range(num+1))
num = 10
print(sum(range(0,num+1,5)))
print(summation(num))