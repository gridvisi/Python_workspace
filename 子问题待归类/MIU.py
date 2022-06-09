__author__ = 'Administrator'
'''
1。如果你的字符串I结束，你可以在结尾添加一个。MI MU
2。您M可以将整个字符串加倍                 MIU MIUIU
3。三个连续的S可以用一个代替              MIIIU  MU
4。可以从字符串中删除两个连续的s。          MUU   M
使用这些规则可以得到下列字符串中的哪一个？
'''
a = ['M','I']

def i(seqeue):
    if a[-1] == 'I':
        a.append('U')
        str_a = ''
        str1 = str_a.join(a)
        #print(str1)
    return str1
print(i(a))

def double(x):
    seq = a[x.index('M')+1:]
    str_a = ''
    str1 = str_a.join(a)
    print(str1)
    str = ''
    str2 = str.join(a[a.index('M')+1:])
    print(str2)
    print(str2.join(str1))
    return str2.join(str1)
print(double('MIU'))

#def tripple_rem(y):

'''
#if (a.index('M'))
try:
    str = ''
    seq = a[a.index('M'):]
    seq_a = a
    print(seq)
    str2 = str.join(a)
    a.append((seq))
    print(a)
except ValueError:
    seq = a[a.index('M'):]
    str2 = str.join(a)
    print(str2)
'''