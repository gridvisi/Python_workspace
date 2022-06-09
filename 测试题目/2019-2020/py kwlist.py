
from keyword import kwlist
print(kwlist)

x,y,z = 1,2,3
def add(x,y):
    return x+y
print(add(x,add(y,z)))

print([i for i in range(1,100)])

#判断berry是否在水果fruit内：​
fruit_list = ['apple','orange','banana']
fruit = 'berry'
if fruit in fruit_list:
    print('yes,i have',f"{fruit}")
else: print('No,i have not',f"{fruit}")