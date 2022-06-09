ls = [99,89,94,100,92]
print(max(ls)) #maxium
print(min(ls))
print(sorted(ls)[::-1])
print(sorted(ls,reverse=False))

print('middle:',sorted(ls,reverse=True)[2])
print('middle:',sorted(ls)[2])

def mutiply(a,b=True):
    return a * b
a, b = 3, 5
print('a*b:',mutiply(a,b))
#a = 3
print('a*b:',mutiply(3,5))




arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#print(arr[0] > arr[1]) #accending
print(arr[:-1])
print(arr[1:])

for i in range(len(arr[:-1])):
    print(arr[i] < arr[i+1])  #IndexError：列表索引超出范围


end = len(arr)//2
print(end)
print(arr[end:],arr[:-end])
print(arr[end:-end])

print(len(arr)//2 == int(len(arr)/2))
print(len(arr)//2,int(len(arr)/2))

print(arr[:len(arr)//2],arr[len(arr)//2:])
arr_even = [0, 1, 2, -3, 4, 8, 5, 6, -7, 8]
print(len(arr_even)/2,int(len(arr_even)/2))
print('arr_even :',arr_even[:int(len(arr_even)/2)])


print(arr[0:4],arr[5:])
print(arr.index(8,5))
print(len(arr) , arr.index(8)+1)
print(len(arr) == arr.index(8)+1)

usa_president_name = '唐纳德特朗普'
print('1:',usa_president_name[3:6])
print('2:',usa_president_name[3:-1])
print('3:',usa_president_name[3:0:-1])
print('reverse:',usa_president_name[::-1])
