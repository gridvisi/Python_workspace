'''
https://www.codewars.com/kata/586ee462d0982081bf001f07/train/python
'''

def fillable(stock, merch, n):
    for key,value in stock.items():
        if key == merch and n <= value:
            return True
    return False

cq = ['hotpot','rabbit','noodle']
cd = ['hotpot','rabbit','chuanchuan']
#menu = [item for item in cq for in cd]
ans = []
for item in cq:
    for j in cd:
        print(item,j)
        if item == j:
            ans.append(item)
print(ans)

def abc(x):
    print(x**2)
x = 2
abc(x)

#time = 0
def abc(x,time=0):
    time += 1
    if time == 5:
        return x
    return (abc(x)**2,time)
x = 3
#print('recurtion',abc(x))

call = {110:'police',
        120:'hospital',
        119:'xiaofangche',
        112:'General Emergency Hotline'}

print(call[110])
print(call[120])
print(call[119])
print({110:'police'}[110])
print({120:'hospital'}[120])
print({119:'xiaofangche'}[119])
print({112:'General Emergency Hotline'})