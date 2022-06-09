'''
https://www.codewars.com/kata/5816b76988ca9613cc00024f/train/python
'''

from itertools import groupby, chain

def sort_sequence(sequence):
    return list(chain.from_iterable(sorted((sorted(grp) + [0] for k, grp in groupby(sequence, key=bool) if k), key=sum)))

def sort_sequence(sequence):
    zeros=[i for i,v in enumerate(sequence) if v==0]
    s1=sorted([sorted(sequence[i+1:j])+[0] for i,j in zip([-1]+zeros,zeros)],key=sum)
    return [v for si in s1 for v in si]

def sort_sequence(sequence):
    l = []
    cur = []
    for e in sequence:
        if e==0:
            l+=[cur]
            cur = []
        else:
            cur+=[e]
    listList = l
    a = [sorted(l)+[0] for l in listList]
    sortedA = sorted(a, key = sum)
    l = []
    for e in sortedA:
        l+=e
    return l

#not work
def sort_sequence(sequence):
    seq = []  #不能用字典，因为切片元素之和有可能相同，位置靠后的覆盖靠前的
    indx = [0,len(sequence)]
    indx = sorted(indx+[i for i,e in enumerate(sequence) if e==0])
    print(indx)
    ans = []
    for i in range(len(indx)-1):
        st,end = indx[i],indx[i+1]
        print(st,end)
        seq.append((sum(sequence[st:end]),sequence[st:end]))
    seq = sorted(seq)
    print('seq',seq)
    for s in seq:
        if s[0] != 0:
            ans += sorted(s[1])
        else:flag = s
    #else:ans += flag[1]
    return ans + flag[1]    #,seq,indx
#sequence = [3, 2, 1, 0, 5, 6, 4, 0, 1, 5, 3, 0, 4, 2, 8, 0]
sequence = [2, 2, 2, 0, 5, 6, 4, 0, 1, 5, 3, 0, 3, 2, 1, 0]
#print(sort_sequence(sequence))


#13rd by ericlee
def sort_sequence(seq):
    i,j = 0,1
    ans,temp = [],[]
    while j <= len(seq):

        if seq[i] != 0 and seq[j] == 0:
            ans.append([sum(seq[i:j]),sorted(seq[i:j])])
            i = j+1
            j = i+1
            print(ans)
        elif seq[i] == 0 and seq[j] != 0:
            j += 1

        elif seq[i] != 0 and seq[j] != 0:
            j += 1

        #elif seq[i] != 0 and seq[j] == 0:
    res = [i[1]+[0] for i in sorted(ans,key=lambda x:x[0])]
    #for i in res:
    #    temp.extend(i)
    return [i for j in res for i in j]
seq = [3, 2, 1, 0, 5, 6, 4, 0, 1, 5, 3, 0, 4, 2, 8, 0]
print('i,j point:',sort_sequence(seq))

import operator
from functools import reduce
a = [[1, 2, 3, 0], [1, 3, 5, 0], [2, 4, 8, 0], [4, 5, 6, 0]]
print(reduce(operator.add, a))


# not work
def sort_sequence(sequence):
    seq = {}
    indx = range(1,sequence.count(0))
    print(indx)
    for i in indx:
        st,end = sequence.index(0,i),sequence.index(0,i+1)
        print(st,end)
        seq[sum(sequence[st:end+1])] = sequence[st:end+1]

    return seq,indx
sequence = [3, 2, 1, 0, 5, 6, 4, 0, 1, 5, 3, 0, 4, 2, 8, 0]
#print(sequence.index(0,2))
#print(sort_sequence(sequence))

#Not work
def sort_sequence(sequence):
    print(''.join([str(i) for i in sequence]).split("0"))
    sl = map(sum,''.join(sequence).split("0"))
    return sl
sequence = [3, 2, 1, 0, 5, 6, 4, 0, 1, 5, 3, 0, 4, 2, 8, 0]
#print(sort_sequence(sequence))