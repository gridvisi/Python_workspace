
#Part B Q7-9
# 8 小佩的家务清单 B完成队尾出现 2 个C,以此类推 A->B->C->D-E

def appendTask(bench,seq):
    s = seq
    for i in s:
        if bench.index(i) <= len(bench)-2:
            s += 2 * bench[bench.index(i)+1]
    return len(s),s
bench = 'ABCDE'
tasks = ['EDEDE','BED','BC','ABCDE']


seq = 'ABCDE'
seq = 'BED'

print(appendTask(bench,seq))
print([appendTask(bench,i) for i in tasks])



def appendTask(bench,seq):
    s = seq
    i = 0
    while i < len(s):
        #print(s)
        if bench.index(s[i]) < len(bench)-1:
            s += 2 * bench[bench.index(s[i])+1]
        i += 1
    return len(s),s
bench,sq = 'ABCDE','BED'
print(appendTask(bench,seq))

tasks = ['A','EDEDE','BED','BC','ABCDE']
print([appendTask(bench,i) for i in tasks])


def appendTask(bench,seq):
    s = seq
    i = 0
    while i < len(s):
        #print(s)
        if bench.index(s[i]) < len(bench)-1:
            s += 2 * bench[bench.index(s[i])+1]
        i += 1
    return len(s),s
bench,sq = 'ABCDE','BED'
print(appendTask(bench,seq))

tasks = ['A','EDEDE','BED','BC','ABCDE']
print([appendTask(bench,i) for i in tasks])