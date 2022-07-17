__author__ = 'Administrator'

def move(n,a,b,c):
    count=0

    if n == 1:
        print(a,'move to',c)
        return 1
    else:
        count+=move(n-1,a,c,b)
        count+=move(1,a,'move to',c)
        count+=move(n-1,b,a,c)
    return count

print(move(8,'a','b','c'))

'''
 if n == 2:
        print(a,'move to',b)
        print(a,'move to',c)
        print(b,'move to',c)   # 2pcs from a move to c
'''