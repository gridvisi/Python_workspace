'''
https://brilliant.org/daily-problems/how-many-marbles/


'''
print(round(1/3,5))
for i in range(17):
    pblue = (5/(i+6)) * (5/(i+6)) * (4/(i+5))
    pred = (i/(i+6)) * (i/(i+6)) * ((i-1)/(i+5))
    if round(pblue+pred,2) == 0.16:
        print('result:',i)