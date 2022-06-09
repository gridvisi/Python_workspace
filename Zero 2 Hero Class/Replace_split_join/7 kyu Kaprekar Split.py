# https://www.codewars.com/kata/5b6ee22ac5cc71833f0010d7/train/python

def kaprekar_split(n):
    xstr = str(n**2)
    if n==1:return 0
    for i,e in enumerate(xstr[:-1],1):
        print(str(n**2)[:i],str(n**2)[i:])
        if int(xstr[:i]) + int(xstr[i:]) == n:
            return i
    else:
        return -1

n = 5050
n = 45
#n = 2223
#n = 5051
n = 1
print(kaprekar_split(n))

#1st
print('1st:',int('' or 0),'1' or 0)

def kaprekar_split(n):
    s = str(n ** 2)
    for i in range(len(s)):
        if int(s[:i] or 0) + int(s[i:] or 0) == n:
            return i
    return -1