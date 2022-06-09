__author__ = 'Administrator'

set = [[1,2,3,3],[4,2,3,3],[1,2,3],[1]]

print(len([i for i in set]))
print(len([j for i in set for j in i]))

'''
i = int(input('chess length:'))
j = int(input('chess width:'))

po = []
for x in range(i+1):
    for y in range(j+1):
        po.append([x,y])
        print(po,len(po))

def knight(*po):
    """

    :rtype : object
    """
    for x in range(i+1):
        for y in range(j+1):
        return po[1][1]
print(knight(po))
'''