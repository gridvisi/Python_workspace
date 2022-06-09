'''
https://www.codewars.com/kata/61055e2cb02dcb003da50cd5/train/python

Pair elements of [1, 2] with elements of [6, 7, 8, 9]

Valid Result:

[[(1, 6), (2, 7)],
 [(1, 6), (2, 8)],
 [(1, 6), (2, 9)],
 [(1, 7), (2, 8)],
 [(1, 7), (2, 9)],
 [(1, 8), (2, 9)]]
'''

#1st
from itertools import combinations

def pair_items(a, b):
    n = min(len(a), len(b))
    return [list(zip(x, y)) for x in combinations(a, n) for y in combinations(b, n)]



#fail to try !
def pair_items(list1, list2):
    if len(list1) == len(list2):
        return [list(zip(list1,list2))]

    elif len(min([list1,list2],key=len)) <= 1:
        print(max([list1,list2],key=len))
        return [[[x,y] for x in list1 for y in list2]]
    else:
        i,j,s,ans = 0,0,0, []
        for _ in range(len(list1)):
            while j < len(list2)-1:
                #print(list1[i:i+2],list2[j:j+2])
                temp =list(zip([list1[i],list1[i+1]],[list2[i+s],list2[j+1]]))
                ans.append(temp)
                j += 1

            s += 1
            j = s
    return ans
list1,list2 = [1, 2] , [6, 7, 8, 9]


list1,list2 = ['c', 'o', 'd', 'e'], ['w', 'a', 'r', 's']
list1,list2 = [], []
print(max([list1,list2],key=len))
# [[('c', 'w'), ('o', 'a'), ('d', 'r'), ('e', 's')]])

list1,list2 = ['a', 'b', 'c'], ['x', 'y']

list1 = ['electric', 'horse', 'fly']
list2 = ['1st', '2nd']
print(pair_items(list1,list2))

def pair_items(list1, list2):
    #i,j = 0, 0
    ans = []
    for i in range(len(list1)-1):
       for j in range(len(list2)-1):
            print(list1[i:i+2],list2[j:j+2])
            ans.append(list(zip([list1[i],list1[i+1]],[list2[i],list2[j+1]])))
    return ans
list1,list2 = [1, 2] , [6, 7, 8, 9]
#print(pair_items(list1,list2))