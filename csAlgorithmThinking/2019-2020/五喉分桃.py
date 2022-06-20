
'''
Description

有一堆桃子和N只猴子，第一只猴子将桃子平均分成了M堆后，还剩了1个，它吃了剩下的一个，并拿走一堆。
后面的猴子也和第1只进行了同样的做法，请问N只猴子进行了同样做法后这一堆桃子至少还剩了多少个桃子
(假设剩下的每堆中至少有一个桃子)？而最初时的那堆桃子至少有多少个？

Input

第一个数据为猴子的只数N(1≤N≤10)
第二个数据为桃子分成的堆数M(2≤M≤7)。

Output

输出包含两行数据，第一行数据为剩下的桃子数，第二行数据为原来的桃子数。

Sample Input

3 2

Sample Output

1 15
n = int(input())
m = int(input())
'''
t = f = 1
n = 5
m = 5
sum = m-1
while t <= n:
    if sum % (m-1) != 0:
        #print(sum)
        t = 1
        f += 1
        sum = f*(m-1)
    sum = sum*m/(m-1)+1
    t += 1
print('final',f,sum)
'''

n,m = 6,3
n,m = 3,3
print(str(11.5)[-1])
def monkey(n,m):
    step = 0
    st = m + 1
    while step < n-1:
        step += 1
        st = st * m / (m - 1) + 1
        if str(st)[-1] != 0:
            step = 1
    print(m,st)
    return ':',m-1,st,step
print(monkey(n,m))
#31 727.0
#727 242
#484 161
#322 107
#214
'''



#print('3' >= 3)

'''

def consume(m, n, num):
    if m == 0:   # 猴子的数量
        return num
    elif (num - 1) % n != 0:
        return -1
    num = (num - 1) * (n - 1) // n
    m -= 1
    print(m,n,num)
    return consume(m,n,num)

def main(m,n):
    for i in range(1,100000):
        result = consume(m,n,i)
        #print('re', result)
        if result != -1:
            return 'res',i,result

m,n = 5,4 #('res', 4093, 1)
m,n = 5,3 #('res', 727, 1)
m,n = 5,2 #('res', 63, 1)
m,n = 4,2 #('res', 31, 1)
m,n = 4,3 #('res', 241, 1)
m,n = 6,5 #('res', 78121, 1)
m,n = 6,4 #('res', 16381, 1)
m,n = 6,3 #('res', 2185, 1)
m,n = 6,2 #('res', 127, 1)
m,n = 7,4 #('res', 65533, 6558)
m,n = 3,2
print(main(m,n))
print('reminder:',consume(m, n, num=15))

'''

'''

for i in range(1000):
    s = divide(m, n, i)
print(s)

    if m == -1:
        return 1
    elif (num - 1) % n != 0:
        return -1
    elif (num - 1) % n == 0:
        num = (num - 1) * (n - 1) // n
        m -= 1
        print(m,n,num)
        return consume(m,n,num)
'''


