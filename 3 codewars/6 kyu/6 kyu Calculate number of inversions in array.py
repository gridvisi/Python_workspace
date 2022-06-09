'''
https://www.codewars.com/kata/537529f42993de0e0b00181f/train/python
Test.assert_equals(count_inversions([]), 0)
Test.assert_equals(count_inversions([1,2,3]), 0)
Test.assert_equals(count_inversions([2,1,3]), 1)
Test.assert_equals(count_inversions([6,5,4,3,2,1]), 15)
Test.assert_equals(count_inversions([6,5,4,3,3,3,3,2,1]), 30)
'''
city = {"chongqing":"重庆","北京":"beijing" }
city["shenzhen"] = "深圳"
print(city["chongqing"],city["北京"])
print(city)

key = [" 科学启蒙系列 "," 四大名著 "]
value1 = ["天气","地球","身体"]
value2 = ["四大名著 ","三国演义","西游记","水浒"]

books = {"科学启蒙系列": ["天气","地球","身体"],
            "四大名著": ["三国演义","西游记","水浒"]}
print(books["四大名著"])


array = [6,5,4,3,3,3,3,2,1] # 30
#array = [6,5,4,3,2,1]  # 15)
array = [2,1,3] #, 1)
array = [] #, 0)
array = [6,5,4,3,3,3,3,2,1]
#array = [6,5,4,3,2,1]
def count_inversions(array):
    i, j, step,cunt = 0, 1, 0,0
    while step < len(array):
        i, j = 0, 1
        while j < len(array):
            if array[i] > array[j]:
                cunt += 1
                array[i],array[j] = array[j],array[i]
            i+=1
            j+=1
        step += 1
    return cunt

def count_inversions(array):
    inv_count = 0
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[i] > array[j]:
                inv_count += 1
    return inv_count


count_inversions=lambda arr:sum(sum(k>j for k in arr[:i]) for i,j in enumerate(arr))

def count_inversions(array):
    return sum(x > y for i,x in enumerate(array) for y in array[i+1:])
print(count_inversions(array))

'''

def count_inversions(array):
    #arr,arrs = {},{}
    arr = sorted(array)
    print([f"{arr.index(i)}{' '}{array.index(i)}" for i in arr])
    pos = [arr.index(i) - array.index(i) for i in arr]
    total = [abs(arr.index(i) - array.index(i)) for i in arr]
    plus = len([x for x in pos if x < 0])
    return sum(total) - plus
'''


'''
from collections import Counter
def count_inversions(array):
    arr = Counter(array)    
    return arr
    
        arr,arrs = {},{}
    for i,e in enumerate(array):
        arr[i] = e
    for i,e in enumerate(sorted(array)):
        arrs[i] = e

'''