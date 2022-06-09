
name = input('what is your name：',)
print('hello ' + name)
print('hello' + "world")

name_1 = "zhou hong yu"
name_2 = "li zheng hao"
print('hello ' + name_2)

print(name_1 + ' and ' + name_2 + " is classmate")

#print(name[0])
#print(name.split(' '))
name = 'zhanghanqi'
def nick(name):
    new = name.split(' ')
    surname = new[0]
    res = [i[0] for i in new[1:]]
    #res = [i[0] for i in new]
    return surname +''.join(res)
print(nick(name))

def triange_area(base,high):
    return 0.5 * base * high

base,high = 10,5
print(triange_area(base,high))

# 不告诉底和高，三个边的长度，X,Y,Z
def triange_area(base,high):
    return 0.5 * base * high #

def add(x,y):
    return x+y
x,y = 10,10
print('add',add(x,y))

arr = [2,5,7,8,9]
print('sum:',sum(arr))

res = add(arr[0],arr[1])
res = arr[0] + arr[1]
print('1:',res)
res += arr[2]
print('2:',res)
res = res + arr[3]
print('3:',res)
res = res + arr[4]

print('res:',res)

#length
arr = [2,5,7,8,9]
print(len(arr))
print(range(len(arr)))
print([i for i in range(len(arr))])

res = 0
for i in range(len(arr)):
    res += arr[i]
print(res)