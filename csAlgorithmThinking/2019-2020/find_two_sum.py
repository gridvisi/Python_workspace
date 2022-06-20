
def find_two_sum(numbers,target_sum):
    visited = {}
    for i,item in enumerate(numbers):
        d = target_sum - item
        if d in visited:
            return i,visited[d],visited,d,item
        visited[item] = i

#solution 2
def find_two_sum(numbers,target_sum,re=[]):
    visited,rev,result = {},[],[]

    for i,item in enumerate(numbers):
        d = target_sum - item
        if d in visited:
            re.append([d,item])
            rev.append(d)
            rev.append(item)
            numbers = [i for i in numbers if i not in rev]
            print(re,numbers)
            if find_two_sum(numbers,target_sum,re=[]) == None:
                for s in re:
                    if s not in result:
                        result.append(s)
                return result   #re,rev
            return find_two_sum(numbers,target_sum) #i,visited[d],visited,d,item
        visited[item] = i


#solution 3
#d = Counter(numbers) print(d,d[8])

from collections import Counter

def find_two_sum(numbers,target_sum):
    visited,re = Counter(numbers),[]
    for i,item in enumerate(numbers):
        n = target_sum - item
        if n in visited and visited[n] == 1 :
            visited[n],visited[item] = 0,0
            re.append([n,item])
            #return re,i,visited[n],visited,n,item
        #visited[item] = i
    return re, i, visited[n], visited, n, item
numbers,target_sum = [0,2,4,4,5,5,8,6,9,10,12,12,17,3,7,3,14,1,15],17

def find_two_sum(numbers,target_sum):
    visited,re = [],[]
    for i,item in enumerate(numbers):
        d = target_sum - item
        if d in visited:
            #visited.append(item)
            re.append([d,item])
        else:visited.append(item)
    return re,visited

print('collection',find_two_sum(numbers,target_sum))

def factorial(n):
    f,n = 1,n
    for i in range(1,n+1):
        f += i
    return f
print(factorial(10))