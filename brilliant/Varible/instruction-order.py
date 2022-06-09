ages = [9,10,13]
ages_new = []

total = 0
for i in ages: # len(ages)
    print(i+1)
    total += i
    print('f:',total)
    ages_new.append(i+1)
print(ages_new)
print(round(total / len(ages),2))
print(int(total / len(ages)))

'''

x = 3
y = 2

x = x - y
print('x_1:',x)

x = x + y
print('x_2:',x)

y = x - y
print('x_3:',x,y)

'''