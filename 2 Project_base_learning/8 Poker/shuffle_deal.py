

def maxseq(seq):
    d = {'A': '1', 'J': '11', 'Q': '12', 'K': '13'}
    #print(d.get(seq[-1][:-1],int(seq[-1][:-1])))
    # 高能预警，get的default输出报错是因为字符'J'不能用 int('J')
    seq = [int(d.get(c[:-1],c[:-1])) for c in seq]
    final = set(seq) ^ set(list(range(min(seq),max(seq)+1)))

    return final
seq = 'cdeffggfghijkaabcdecabccdd'
seq = '34567885678910111212345'
seq = ['10D', 'KD', '8D', '7D', 'JD']
print('No.1st solution:',maxseq(seq))


# nested list solve Maxseq
def maxseq(seq):
    #d = {'A': 1, 'J': 11, 'Q': 12, 'K': 13}
    d = {'A': '1', 'J': '11', 'Q': '12', 'K': '13'}
    #print(d.get(seq[-1][:-1],int(seq[-1][:-1])))
    # 高能预警，get的default输出报错是因为字符'J'不能用 int('J')
    seq = [int(d.get(c[:-1],c[:-1])) for c in seq]
    print(seq)
    seq = sorted(seq)
    print(seq)
    #last_idx = [seq[0]]
    maxSrg = [[seq[0]]]
    for i,e in enumerate(seq[1:]):
        #if e not in last_idx:
        if int(e) == int(maxSrg[-1][-1])+1:
            maxSrg[-1].append(e)
            print(maxSrg, e)
            #continue
        else:
            maxSrg.append([e])
            print(maxSrg)
    return maxSrg
seq = 'cdeffggfghijkaabcdecabccdd'
seq = '34567885678910111212345'
seq = ['10D', 'QD', '8D', 'KD', 'JD']
print('No.2th solution:',maxseq(seq))