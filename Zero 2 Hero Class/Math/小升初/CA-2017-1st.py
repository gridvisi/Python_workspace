'''
# 1. Four cards are in a row. We can choose any two cards and swap
them. Which row of cards cannot be obtained?

2017

A.2710  B.0127   C.1027  D.0217  E.2071
'''

n = 2017
def swap_digit(n):
    comb = []
    num = list(str(n))
    for i in range(len(num)):
        for j in range(len(num)):
            if i != j:
                num[i],num[j] = num[j],num[i]
                comb.append(''.join(num))
            num = list(str(n)) # the key is to initialize num
    return comb
print(swap_digit(n))
# ['0217', '1207', '7201', '2701',
# '2071', '2170', '7120', '7210',
# '7201', '1207', '1702', '1720']


option = {'A':'2710','B':'0127','C':'1027','D':'0217','E':'2071'}
option = ['2710','0127','1027','0217','2071']

noSeen = []
for elem in option:
    if elem not in swap_digit(n):
        noSeen.append(elem)
print(noSeen)


## 20. Monica is asked to choose 5 different numbers.
# She multiplies some of them by 2
# and multiplies the other numbers by 3. Among the 5 results,
# what is the smallest number of different results that she can obtain?
'''
乘以2后的结果还是在原数组里，乘以3以后的结果
2*x = 3*y
2*m = 3*n
2*z in [3*y,3*n] = True
3*z in [2*x,2*m] = True
if 2*z == x:


1，2*3，4*3，6*3，9*2
3，6，12，18
'''

'''
#21 A bag contains only red marbles and green marbles. For any 5 marbles we pick, at least
one is red. For any 6 marbles we pick, at least one is green. What is the largest number of
marbles that the bag can contain?
'''