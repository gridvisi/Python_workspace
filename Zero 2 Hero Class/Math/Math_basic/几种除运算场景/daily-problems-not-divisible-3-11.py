'''
https://brilliant.org/daily-problems/not-divisible-3-11/
'''

end = 100

three,eleven,common = [],[],[]
for i in range(end+1):
    if i%3:  three.append(i)
    if i%11: eleven.append(i)
    #res = three + eleven
    if i % 3 != 0 and i % 11 != 0:
        common.append(i)
ans = [i for i in three + eleven if i in common]
res = three + eleven
print(len(set(res)),len(res),res)
print(len(common),common)
print('ans:',len(set(ans)),len(ans))
print('set(ans):',set(ans))



three,eleven,common = [],[],[]
for i in range(end+1):
    #if not i%3 or not i%11:
    if i % 3 == 0 and i%11 !=0:
        three.append(i)

    if i % 11 == 0 and i%3 !=0:
        eleven.append(i)

    if i % 3 == 0 and i % 11 == 0:
        common.append(i)
#res = [i for i in three + eleven if i not in common]
res = three + eleven
print(len(three),len(eleven))
print(len(set(res)),common,res,len(res))