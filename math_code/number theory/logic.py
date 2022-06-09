__author__ = 'Administrator'

#true=诚实, false=说谎; A 说 B，C说谎；B说：A或C说谎；C说A或B说谎；if A,B,C只有一人说谎，who is he？

T = 1
F = 0

logic_status = ['100','011','110','011','101'] # 枚举题目中给出的情况
a = [0,1,1]
b = [1,0,1]
c = [1,1,0]
#print(reversed('helloruby'))

def Not(x):
    if x == 1:
        return 0
    else:return 1
z = []
def rev(y):
    for i in range (len(y)):
        z.append(Not(y[i]))
        if len(z) == len(y):
            return z
print (rev(c))
'''
def rev(y):
    print(len(y))
    reversed_a = []
    i = 0
    for i in range(int(len(y))):
        print(y[i])
        z = y[i]
        reversed_a.append(Not(z))
        print(z)
        print(Not(y[i]))
        i += 1
        return reversed_a

print(rev(b))
'''