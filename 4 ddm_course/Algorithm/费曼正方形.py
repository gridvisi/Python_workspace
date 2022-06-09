
def count_squares(n):
    #对角线共有n-1个正方形
   #网格上的点x,y：range(0,n)有min(n-i,n-j)种正方形
    cunt = 0
    for i in range(n):
        for j in range(n):
            cunt += min(n-i,n-j)
    return cunt

n = 4
print(count_squares(n))
#1240


#伪代码

def count_squares(n):
    '''
    n * n
         2）2*(n+1) - 1
         两者之和为(n+1 )*( n+1)
    '''

    if n == 1:
        return 1
    else:
        return n**2 + count_squares(n - 1)


'''

while "xing go to school":
    "垃圾带走" \
    "" \
    ""

'''
