'''
https://brilliant.org/daily-problems/sekou-waiter/


'''

meal = ['a','b','c','d']
person = ['1','2','3','4']
choice = ['a1','b2','c3','d4']
print(set(choice))

from itertools import combinations
all = list(combinations(meal+person,2))
print(list(all),len(list(all)))
all_valid = [i for i in all if i[0] in meal and i[1] in person]
print(all_valid)
print('combination:',len(list(all)),len(all_valid))

from itertools import permutations
all_p = permutations(meal+person,2)
print(list(all_p),len(list(all_p)))  ##显示了数组长度==0

all_p = list(permutations(meal+person,2)) #正确显示了数组长度
print(all_p,len(all_p))

all_p_valid = [i for i in all_p if i[0] in meal and i[1] in person]
print('permutations:',len(all_p),len(all_p_valid),all_p_valid)


ans = []
p = 0
for i in meal:
    for j in person:
       ans.append(i+j)

result = list(combinations(ans,4))
#print(len(result),result)

ans = []
for c in result:
    if len(set([i[0] for i in c])) == 4 and len(set([i[1] for i in c])) == 4:
        ans.append(c)

print(len(ans),ans)

right_choice = ['a1','b2','c3','d4']
final= [i for i in ans if set(i)&set(right_choice)]
print(len(final),final)


