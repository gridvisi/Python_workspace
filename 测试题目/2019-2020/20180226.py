__author__ = 'Administrator'
#https://brilliant.org/weekly-problems/2018-02-26/intermediate/?p=3
'''
row_result = []
def time_couple(x):
    j = 0
    while j < (int(len(x))-1):
        row_result.append(x[j] * x[j + 1])
        j += 1
    else:
        return row_result

start = []
for i in range(1,9):
    start.append(i)
print(start)
print(time_couple(start))
x = time_couple(start)
print(x)
'''

x = [x for x in range(1,9)]   #正解
print (",".join(str(i) for i in x))
print(x)
y = []
while len(x) > 1:
    for k,i in enumerate(x[:-1]):
        y.append(x[k]*x[k+1])
    x = y
    y = []
    z = ",".join(str(i) for i in x)
    print (z)
print('Trailing zeros = %d' %(len(z) - len(z.rstrip('0'))))




