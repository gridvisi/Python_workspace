'''
https://www.codewars.com/kata/592645498270ccd7950000b4/train/python
'''

#8th solve by ericlee
def typist(s):
    cunt,flag = 0,True
    for i in s:
        if i.islower() and flag:
            cunt += 1

        elif i.islower() and not flag:
            cunt += 2
            flag = True

        elif i.isupper() and flag:
            cunt += 2
            flag = False

        elif i.isupper() and not flag:
            cunt += 1
            #flag = False
    return cunt
s = 'BeiJingDaXueDongMen'
print(typist(s))


