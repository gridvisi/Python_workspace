'''
https://www.codewars.com/kata/5635e7cb49adc7b54500001c/train/python
'''
qian = {100:0,50:0,20:0,10:0,5:0,1:0}
#change = {100:0,50:0,25:0,5:0}
ticket = 25


line = [25,25,50,100,50,25,25]
print(''.join([str(i) for i in line]))
line_2 = [50,25,50]

zhaoqian = 55 - 25
#for k,v in change.items():
m = zhaoqian

# 比较low的写法
if m in [k for k in change.items()]:
    if change[m] > 0:
        change[m] -= 1
else:
    #for k,v in qian.items():
    for k,v in change.items():
        if m >= k:
            #qian[k] += m // k
            change[k] += m//k
            m = m - k * (m // k)
    #print(qian,m%k)
    print(change, m % k)




zhanghq = {"zhq":"zipman"}
jerom = {"jerom":"lizhenghao"}


name = {"ddm dragonfly":"丁丁猫"}
name["ddm dragonfly"] = "丁丁猫亲子创客"
print(name["ddm dragonfly"])

#for i in range('jerom','alex','emma'):print(i)
for i in range(len(['jerom','alex','emma'])):
    print(['jerom','alex','emma'][i])

for i in (['jerom','alex','emma']):print(i)

bill = {10:0, 20:0, 50:0, 100:0, 200:0,500:0}

for k,v in bill.items():print(k)

def solve(n):
    bill = {10:0, 20:0, 50:0, 100:0, 200:0,500:0}

    for i in [k for k,v in bill.items()][::-1]:
        if n > i:
            bill[i] += n//i
            #print(bill,i)
            n = n - i*(n//i)
    return bill
n = 122
print(solve(n))

n = 590
bill_s = [500,200,100,50,10]
for i in bill_s: #逐个取元素
    if n > i:
        bill[i] += n // i
        # print(bill,i)
        n = n - i * (n // i)
