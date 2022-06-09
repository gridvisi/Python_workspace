'''
https://www.codewars.com/kata/598c1bc6a04cd3b8dd000012/train/python
Output:
Return the total number of people the restaurant denies service to.

Examples:
(1, 2, [1, 2, 1, 1])  =>  0
(1, 1, [1, 1, 2, 1])  =>  2
'''

from collections import Counter
def restaurant(single_tables, double_tables, visitors):
    #v = Counter(visitors)
    cunt = 0
    table = {1:[single_tables,0],2:[double_tables,0]}
    double = 0
    for i in visitors:
        if table[i][0] >= 1:
            table[i][0] -= 1
            table[i][1] += i

        elif table[1][0] == 0 and table[2][1]//2 <= double_tables:
            if table[2][1]%2 == 1:
                table[2][1] += 1
        else:
            cunt += i
    return cunt
single_tables, double_tables, visitors = 2, 1, [2, 1, 2, 2, 2, 2, 1, 2, 1, 2] # 13)

#single_tables, double_tables, visitors = 4, 3, [2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 1, 2, 2, 1, 2, 2, 2, 1, 2] # 25)

#single_tables, double_tables, visitors = 1, 2, [1, 2, 1, 1]
print(restaurant(single_tables, double_tables, visitors))

def restaurant(single_tables, double_tables, visitors):
    s,g = '1'*single_tables + '2'*double_tables,0
    for i in visitors:
        if str(i) in s: s=s.replace(str(i),'0',1); g+=i
        elif i==1 and '2' in s: s=s.replace('2','i',1); g+=i
        elif i==1 and 'i' in s: s=s.replace('i','0',1); g+=i
        else: continue
    return sum(visitors)-g