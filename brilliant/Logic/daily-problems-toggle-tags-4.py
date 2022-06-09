'''
https://brilliant.org/daily-problems/toggle-tags-4/
'''

statement_A = [True,False]
statement_B = [True,False]
chest_A = []
#Condition 3:
#
for a in statement_A:
    for b in statement_B:
        if a and not b:
            chest_A,chest_B = 'GOLDEN','GOLDEN'
        elif b and not a:
            chest_b,chest_A = 'NO GOLDEN','GOLDEN'
        elif a and b:
            pass
        elif not a and not b:
            chest_A, chest_B = 'NO GOLDEN', 'GOLDEN'
print(chest_A,chest_B)
