'''
https://www.codewars.com/kata/55b4d87a3766d9873a0000d4/train/python
Imagine I have between m and n Zloty..." (or did he say Quetzal? I can't remember!)
"If I were to buy 9 cars costing c each, I'd only have 1 Zloty (or was it Meticals?) left."
"And if I were to buy 7 boats at b each, I'd only have 2 Ringglets (or was it Zloty?) left."

Test.assert_equals(howmuch(1, 100), [["M: 37", "B: 5", "C: 4"], ["M: 100", "B: 14", "C: 11"]])
Test.assert_equals(howmuch(1000, 1100), [["M: 1045", "B: 149", "C: 116"]])
Test.assert_equals(howmuch(10000, 9950), [["M: 9991", "B: 1427", "C: 1110"]])
Test.assert_equals(howmuch(0, 200), [["M: 37", "B: 5", "C: 4"], ["M: 100", "B: 14", "C: 11"], ["M: 163", "B: 23", "C: 18"]])
Test.assert_equals(howmuch(2950, 2950), [])
Test.assert_equals(howmuch(20000, 20100), [["M: 20008", "B: 2858", "C: 2223"], ["M: 20071", "B: 2867", "C: 2230"]])
'''
#[list(zip(['M:','B:','C:'],x)) for x in re]:
def howmuch(m, n):
    if m > n: m,n = n,m
    re,res = [],[]
    for f in range(m,n+1):
        if (f - 1) % 9 == 0 and (f - 2) % 7 == 0:
            b,c = (f - 2)//7,(f - 1)//9
            re.append([f'{x + str(y)}' for x, y in zip(['M:', 'B:', 'C:'], [f, b, c])])
    return re
m, n = 1, 100
print(howmuch(m, n))

howmuch=lambda m,n:[[f"M: {M}",f"B: {M//7}",f"C: {M//9}"]for M in range(min(m,n),max(m,n)+1)if M%7==2and M%9==1]

def howmuch(m, n):
    return [['M: %d'%i, 'B: %d'%(i/7), 'C: %d'%(i/9)] for i in range(min(m,n), max(m,n)+1) if i%7 == 2 and i%9 == 1]

def howmuch(m, n):
    i = min(m, n)
    j = max(m, n)
    res = []
    while (i <= j):
        if ((i % 9 == 1) and (i %7 == 2)):
            res.append(["M: " + str(i), "B: " + str(i // 7), "C: " + str(i // 9)])
        i += 1
    return res

# reshape new solution
def howmuch(cash):
    re, res = [], []
    for i in cash:
        if (i - 1) % 9 == 0 and (i - 2) % 7 == 0:
            f, n = (i - 2) // 7, (i - 1) // 9
    return [f'{x + str(y)}'for x, y in zip(['M:', 'F:', 'S:'], [i,f,n])]
cash = [10, 20, 50, 100]
# [f'{x + str(y)}' for x, y in zip(['M:', 'F:', 'S:'], [f, f,n])
print(howmuch(cash))

def howmuch(cash):
    return [['M:%d'%i, 'B:%d'%(i/7), 'C:%d'%(i/9)] for i in cash if i%7 == 2 and i%9 == 1]



