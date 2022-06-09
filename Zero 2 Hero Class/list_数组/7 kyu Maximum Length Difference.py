'''
https://www.codewars.com/kata/5663f5305102699bad000056/train/python


'''

def mxdiflg(a1, a2):
    if len(a1)==0 or len(a2) == 0:return -1
    a,b = sorted(a1,key=len),sorted(a2,key=len)
    return max(abs(len(a[0])-len(b[-1])),abs(len(a[-1]) - len(b[0])))            #sorted([len(i) for i in a1])#[0,len(a1),len(a1)]
a1 = "cccooommaaqqoxii"
print(mxdiflg(a1,1))

def mxdiflg(a1, a2):
    if a1 and a2:
        return max(
            len(max(a1, key=len)) - len(min(a2, key=len)),
            len(max(a2, key=len)) - len(min(a1, key=len)))
    return -1