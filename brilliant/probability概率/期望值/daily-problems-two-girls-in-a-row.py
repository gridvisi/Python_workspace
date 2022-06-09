print(bin(10))
print(int(0b1010))
print(int(int('1'*41 + '0'*41)))
print(0b1111111111111111111111111111111111111111100000000000000000000000000000000000000000)
print(len("4835703278456317675569152"))

'''
Samuel, a midwife at Brilliant Hospital, wants to know how often 
two girls are born in a row. For example, in a sequence of births 
"girl-girl-boy-girl-girl-girl," 
two girls in a row appear three times — the first and second babies, 
the fourth and fifth, and the fifth and sixth.

连续 形容词 ()
successive 形 
sequential 形 
连续 ()
serial  · in a row 

This week, 8282 babies are scheduled to be born at Brilliant Hospital. 
Assuming that all these births go according to plan and that a girl and a 
boy are equally likely to be born, what is the expected number of times 
two girls will be born in a row?
'''
# n = 9 find 3 girls born in a row?

maxBin = 0b111110000
minBin = 0b11111

#不足9位的，凑足4个1和5个0补齐9位
# 参数 x 连续boy or girl


def inARow(s,seq,gender):
    i = 0
    cunt = 0
    while i < len(s)-seq:
        if all([g==gender for g in s[i:i+seq]]):
            cunt += 1
        i += 1
    return cunt
#s,seq,gender = '0b100000000011111111',2,'1'
#print('inARow:',inARow(s,seq,gender))

def bornInRow(seq,n):
    girl,boy = [],[]
    minBin,maxBin = 0b1000000000111111111,0b1111111111000000000
    #n is 18 bit length of minBin and maxBin except head of '0b1'
    #print('min-max:',list(map(len,(str(minBin),str(maxBin)))))
    for i in range(int(minBin),int(maxBin)+1):
        s = str(bin(i))[3:]

        if s.count('1') == n-n//2 and s.count('0') == n//2:
            #print(len(s)) #18bit
            girl.append(inARow(s,seq,'0'))
            boy.append(inARow(s,seq,'1'))
    return sum(girl)/len(girl),sum(boy)/len(boy),len(girl),len(boy) #,girl,boy

seq = 2
n = 18
#print(n//2,n-n//2)
print(bornInRow(seq,n))
# 20 boys and 20 girl, solve = 3.25
# 24 boys and 24 girl, solve = 3.92
print('00100100010100'.count('00'))

minBin,maxBin = 0b1000000000111111111,0b1111111111000000000
print(int(maxBin) - int(minBin))
print((int(maxBin) - int(minBin))/bornInRow(seq,n)[2])
#math solve

#print(bornInRow(3,n))
# 'ggg','ggb','gbb','bbb',gbg','bgb','bgg','bbg'
g = 0.25
print(g * 18)

'''

def bornInRow(seq,n):
    girl,boy = [],[]
    minBin,maxBin = 0b10000000000111111111,0b11111111110000000000
    for i in range(int(minBin),int(maxBin)+1):
        s = str(bin(i))[2:]
        if s.count('1') == n-n//2 and s.count('0') == n//2:
            try:
                sec = s[s.index('00')+1:].count('0'*seq)
            except:
                sec = 0
            girl.append(s.count('0' * seq) + sec)
            boy.append(s.count('1' * seq))
    return girl,boy,sum(girl)/len(girl),sum(boy)/len(boy)

'''