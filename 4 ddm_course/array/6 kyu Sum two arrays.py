'''
https://www.codewars.com/kata/59c3e8c9f5d5e40cab000ca6/train/python

[3,2,9],[1,2] --> [3,4,1]
[4,7,3],[1,2,3] --> [5,9,6]
[1],[5,7,6] --> [5,7,7]
'''
#print(int('-9')*2)
#print(str(-101))
array1,array2 = [3,2,9],[1,2]

array1,array2 = [0],[]
#array1,array2 = [-9, 3],[-8]  #: should return [-1, 0, 1]


array1,array2 = [0],[-1,0]
array1,array2 = [],[]
array1,array2 = [-3,4,6],[3,4,4]
array1,array2 = [1],[5,7,6]
array1,array2 = [4,7,3],[1,2,3]
array1,array2 = [3,2,6,6],[-7,2,2,8] #[-3,9,6,2])
def sum_arrays(array1,array2):
    if not array1: return array2
    elif not array2: return array1
    ans = list(map(lambda x:''.join([str(i) for i in x]),(array1,array2)))
    print('ans:',ans)
    result = str(sum([int(i) for i in ans]))
    print(result)
    if str(result)[0] == '-':
        return [- int(result[1])] + [int(i) for i in result[2:]]
    return list(result)

def sum_arrays1(array1, array2):
    if not array1: return array2
    elif not array2: return array1
    res = str(int(''.join([str(i) for i in array1]))+int(''.join([str(i) for i in array2])))
    if int(res) > 0:
        return [int(i) for i in res]
    elif int(res) < 0:
        return [-int(res[1])]+[int(i) for i in res[2:]]
    else:
        return [0]
#[x for arr in ans for x in arr]
array1, array2 = [-1, 0, 0],[1, 0, 0]
print(sum_arrays(array1,array2))
'''
    if result[0] == '-':
        result[0] = -result[1]
        #result

'''

#print(sum_arrays(array1,array2))


'''
def sum_arrays(array1,array2):
    ans = []
    if not array1: return array2
    elif not array2: return array1
    ans = list(map(lambda x:''.join(x),([str(i) for i in array1],[str(i) for i in array2])))
    #print(sum([int(i) for i in ans]),[int(i) for i in ans])
    result = [i if i.isdigit() else i for i in str(sum([int(i) for i in ans]))]
    print(result)
    if result[0] == '-':
        ans = [-int(result[1])]
        for i in result[2:]:
            ans.append(int(i))
    else:
        ans = [int(i) for i in result]
    return ans

'''