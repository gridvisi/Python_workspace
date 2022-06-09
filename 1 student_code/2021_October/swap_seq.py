
print(bin(3),oct(12),oct(10),oct(31))
print(oct(25)) #10.31 -> 12.25

seq = ['jiajia','lucas','Peter_parker','mcree','alex','tommy']
seq_dis = ['jiajia','alex','lucas','Peter_parker','mcree','tommy']

print(seq.index('alex'))
seq[1],seq[4] = 'lucas','alex'
print(seq)



print(seq_dis.pop(1))
print('pop:',seq_dis)
seq_dis.insert(4,'alex') #class
print('insert',seq_dis)

for i in range(len(seq)):
    if seq[i] != seq_dis[i]:
        print(i,seq[i],seq_dis[i])


'''
seq是申请python课程的
'''