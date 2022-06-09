#https://www.codewars.com/kata/52608f5345d4a19bed000b31/train/python

'''
Test.assert_equals(to_chinese_numeral(9),'九')
Test.assert_equals(to_chinese_numeral(-5),'负五')
Test.assert_equals(to_chinese_numeral(0.5),'零点五')
Test.assert_equals(to_chinese_numeral(10),'十')
Test.assert_equals(to_chinese_numeral(110),'一百一十')
Test.assert_equals(to_chinese_numeral(111),'一百一十一')
Test.assert_equals(to_chinese_numeral(1000),'一千')
Test.assert_equals(to_chinese_numeral(10000),'一万')
Test.assert_equals(to_chinese_numeral(10006),'一万零六')
Test.assert_equals(to_chinese_numeral(10306.005),'一万零三百零六点零零五')

'''

def to_chinese_numeral(n):
    numerals = {
        "-":"负",
        ".":"点",
        0:"零",
        1:"一",
        2:"二",
        3:"三",
        4:"四",
        5:"五",
        6:"六",
        7:"七",
        8:"八",
        9:"九",
        10:"十",
        100:"百",
        1000:"千",
        10000:"万"
    }
    sl = list(str(abs(n)))
    s = [numerals[int(i)] if i not in ('-','.') else numerals[i] for i in sl]

    idotd = str(abs(n)).split('.')
    integ = str(abs(n))[:len(idotd)]
    #intg = [numerals[int(e)]+ for i,e in enumerate(integ[::-1])]
    st,p,recn = 0,4,''
    x = str(integ)
    def y(x):
        return [numerals[int(e)]+numerals[10**(len(x)-i-1)] if len(x)-i > 1 and e != '0' else numerals[int(e)] for i,e in enumerate(x)]
    s = str(n).split('.')
    while st <= len(x)%4:
        init, res = int(x)%(10**p),int(x)//(10**p)
        if init == 0:
            recn += y(str(res))
            recn = ''.join(recn) + numerals[10000] * st
        else:
            x = str(res)
            st = +1
        print(recn)

    dec = ''.join(s[len(idotd[0]):])
    print(dec,sl[:len(idotd)])
    #scn = [intg + numerals[10**((len(intg) -i)%4)] for i,e in enumerate(sl[:len(idotd)])]
    return recn,s
n = 313333.5
n = 10306.005
n = 0.5
n = 11
n = -204.23
n = -10.07
print(to_chinese_numeral(n))
#print((n==0)*7)


import re

NEG, DOT, _, *DIGS = "负点 零一二三四五六七八九"
POWS = " 十 百 千 万".split(' ')
NUMS = {str(i):c for i,c in enumerate(DIGS)}
for n in range(10): NUMS[str(n+10)] = POWS[1] + DIGS[n]*bool(n)


def to_chinese_numeral(n):
    ss = str(abs(n)).split('.')
    return NEG*(n<0) + parse(ss[0]) + (len(ss)>1 and decimals(ss[1]) or '')

def decimals(digs): return DOT + ''.join(NUMS[d] for d in digs)

def parse(s):
    if s in NUMS: return NUMS[s]
    s = ''.join(reversed([ NUMS[d] + POWS[i]*(d!='0') for i,d in enumerate(reversed(s))]))
    return re.sub(f'零+$|(?<=零)零+', '', s)

'''
[numerals[int(e)]*(i!=0) + numerals[10**((len(sl[:len(idotd)])-int(i)-1)%4)]]

    def y(x):
        return [numerals[int(e)]+numerals[10**(len(x)-i-1)] if len(x)-i > 1 and e != '0' else numerals[int(e)] for i,e in enumerate(x)]
    s = str(n).split('.')

    sl = [i[::-1] for i in [s[0][::-1][i:i+4] for i in range(0,len(s[0]),4)][::-1]]
    it = [y(i) for i in sl]
    it_res = [''.join(x)+ (len(it)-i-1)*"万" for i,x in enumerate(it)]
    dec = '点'+''.join([numerals[int(e)] for i,e in enumerate(s[1])])
    #dec = [numerals[int(i)] if i != '.' else numerals[i] for i in s[1]]
    #dec = ''.join([numerals[int(i)] for i in s[1]])
    return sl,it,dec,it_res,''.join(it_res)+dec  #f'{it}'.join(f'{dec}')
'''