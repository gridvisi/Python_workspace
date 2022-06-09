__author__ = 'Administrator'
'''
i = 1
s = 1
while i < 6:
    i += 2
    s *= 2
print('i=',i,'s=',s)
'''

def cube(n):
    """

    :rtype : object
    """
    if n==1:
        return 1
    return cube(n-1)+n*n*0.5+n*0.5
total = int(input('cube total number:'))
layer = 1
while cube(layer) < total or cube(layer) == total:
    layer+=1
print('最多能搭的层数是：',layer-1,'共用去木块数量是：',cube(layer-1),'剩余的木块数量：',total-cube(layer-1))